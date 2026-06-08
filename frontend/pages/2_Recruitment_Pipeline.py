import streamlit as st
import requests
from datetime import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from components.language_manager import get_text, init_language

init_language()

st.set_page_config(page_title=get_text("rec_title"), layout="wide", page_icon="🎯", initial_sidebar_state="collapsed")

css_path = Path(__file__).parent.parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<style>[data-testid="stSidebar"] { display: none; } button[data-testid="baseButton-header"] { display: none; }</style>""", unsafe_allow_html=True)

if st.button(get_text("back_to_home")): 
    st.switch_page("app.py")

st.markdown(f"""<div class="premium-header" style="padding: 1.5rem;"><div class="premium-title">{get_text('rec_title')}</div><div class="premium-subtitle">{get_text('rec_subtitle')}</div></div>""", unsafe_allow_html=True)

API_URL = "http://localhost:8000/api"

stages = [
    {"name": get_text("rec_new"), "key": "new", "color": "#7a9bb0"},
    {"name": get_text("rec_screening"), "key": "screening", "color": "#6ba3b8"},
    {"name": get_text("rec_interview"), "key": "interview", "color": "#d4a45a"},
    {"name": get_text("rec_offer"), "key": "offer", "color": "#6fb398"},
    {"name": get_text("rec_hired"), "key": "hired", "color": "#5b8caf"},
    {"name": get_text("rec_rejected"), "key": "rejected", "color": "#d48474"}
]

try:
    response = requests.get(f"{API_URL}/candidates")
    if response.status_code == 200:
        candidates = response.json()
        cols = st.columns(len(stages))
        for idx, stage in enumerate(stages):
            with cols[idx]:
                st.markdown(f"<div style='background:{stage['color']}12; border-radius:16px; padding:1rem; margin-bottom:1rem;'><h4 style='color:{stage['color']}; margin:0;'>{stage['name']}</h4><p style='margin:0.5rem 0 0; font-size:0.8rem;'>{len([c for c in candidates if c['status'] == stage['key']])} {get_text('candidates_lower')}</p></div>", unsafe_allow_html=True)
                for cand in [c for c in candidates if c['status'] == stage['key']]:
                    st.markdown(f"<div style='background:white; border-radius:16px; padding:1rem; margin-bottom:0.5rem; border:1px solid #d4e4ed;'><b>{cand['name']}</b><br><small>{cand['position_applied']}</small><br><small>{get_text('rec_score')}: {cand['score']}%</small></div>", unsafe_allow_html=True)
                    if stage['key'] not in ['rejected', 'hired'] and idx + 1 < len(stages) - 1:
                        if st.button(f"{get_text('rec_move_to')} {stages[idx+1]['name']}", key=f"move_{cand['id']}"):
                            requests.put(f"{API_URL}/candidates/{cand['id']}/status", json={"status": stages[idx+1]['key']})
                            st.rerun()
                    st.divider()
        with st.expander(get_text("rec_add_candidate")):
            with st.form("add_candidate"):
                col1, col2 = st.columns(2)
                with col1: 
                    name = st.text_input(get_text("rec_candidate_name"))
                    email = st.text_input(get_text("rec_candidate_email"))
                with col2: 
                    phone = st.text_input(get_text("rec_candidate_phone"))
                    position = st.text_input(get_text("rec_position"))
                score = st.slider(get_text("rec_score"), 0, 100, 50)
                if st.form_submit_button(get_text("add")):
                    try:
                        requests.post(f"{API_URL}/candidates", json={"name": name, "email": email, "phone": phone, "position_applied": position, "score": score})
                        st.success(get_text("success"))
                        st.rerun()
                    except:
                        st.error(get_text("error"))
    else: 
        st.error(get_text("error"))
except: 
    st.error(get_text("resume_error_connection"))