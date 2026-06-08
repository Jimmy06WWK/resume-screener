import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from pathlib import Path
import sys
import time
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent))
from components.ui_parts import render_candidate_card, render_metric_cards
from components.language_manager import get_text, init_language

init_language()

st.set_page_config(page_title=get_text("resume_title"), layout="wide", page_icon="📄", initial_sidebar_state="collapsed")

css_path = Path(__file__).parent.parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<style>[data-testid="stSidebar"] { display: none; } button[data-testid="baseButton-header"] { display: none; }</style>""", unsafe_allow_html=True)

if st.button("Back to Home"): st.switch_page("app.py")

st.markdown(f"""<div class="premium-header"><div class="premium-title">{get_text('resume_title')}</div><div class="premium-subtitle">{get_text('resume_subtitle')}</div></div>""", unsafe_allow_html=True)

if 'results' not in st.session_state: st.session_state['results'] = None
if 'processing' not in st.session_state: st.session_state['processing'] = False

col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown("### Job Description")
    jd_input = st.text_area("", height=250, placeholder="Paste job description here...", key="jd_input", label_visibility="collapsed")
    st.markdown("### Upload Resumes")
    uploaded_files = st.file_uploader("", type=["pdf"], accept_multiple_files=True, key="file_uploader", label_visibility="collapsed")
    if uploaded_files: st.success(f"{len(uploaded_files)} file(s) selected")
    start_button = st.button("Start Analysis", use_container_width=True, type="primary", disabled=st.session_state['processing'])

with col_right:
    if start_button and jd_input and uploaded_files:
        st.session_state['processing'] = True
        progress_bar = st.progress(0)
        status = st.empty()
        files = [("resumes", (f.name, f.getvalue(), "application/pdf")) for f in uploaded_files]
        payload = {"jd_text": jd_input, "output_lang": st.session_state.get('language', 'English')}
        try:
            status.info("Uploading..."); progress_bar.progress(25)
            res = requests.post("http://localhost:8000/screen", data=payload, files=files, timeout=120)
            status.info("AI Analyzing..."); progress_bar.progress(75)
            if res.status_code == 200:
                st.session_state['results'] = res.json(); progress_bar.progress(100); status.success("Complete!"); st.balloons(); time.sleep(1); st.rerun()
            else: st.error(f"Error: {res.status_code}")
        except Exception as e: st.error(f"Error: {e}")
        finally: progress_bar.empty(); status.empty(); st.session_state['processing'] = False
    elif start_button and not jd_input: st.error("Please enter job description")
    elif start_button and not uploaded_files: st.error("Please upload resumes")
    
    tab1, tab2 = st.tabs(["Results", "Statistics"])
    with tab1:
        if st.session_state['results']:
            results = st.session_state['results']
            render_metric_cards(results)
            st.subheader("Ranking")
            df = pd.DataFrame(results)
            if not df.empty:
                fig = px.bar(df, x='score', y='candidate_name', orientation='h', color='score', text='score')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                for idx, c in enumerate(results): render_candidate_card(c, idx)
        else: st.info("No results yet")
    with tab2:
        if st.session_state['results']:
            results = st.session_state['results']
            scores = [r['score'] for r in results]
            fig = px.histogram(x=scores, nbins=10)
            st.plotly_chart(fig, use_container_width=True)
            all_skills = [s for r in results for s in r.get('matched_skills', [])]
            if all_skills:
                skills_df = pd.DataFrame(Counter(all_skills).most_common(10), columns=['Skill', 'Count'])
                fig2 = px.bar(skills_df, x='Count', y='Skill', orientation='h', color='Count')
                st.plotly_chart(fig2, use_container_width=True)
        else: st.info("No data")
