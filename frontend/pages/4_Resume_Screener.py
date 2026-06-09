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

if st.button(get_text("back_to_home")): 
    st.switch_page("app.py")

st.markdown(f"""<div class="premium-header"><div class="premium-title">{get_text('resume_title')}</div><div class="premium-subtitle">{get_text('resume_subtitle')}</div></div>""", unsafe_allow_html=True)

if 'results' not in st.session_state: st.session_state['results'] = None
if 'processing' not in st.session_state: st.session_state['processing'] = False

col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown(f"### {get_text('resume_jd')}")
    jd_input = st.text_area(
        "Job Description", 
        height=250, 
        placeholder=get_text("resume_jd_placeholder"), 
        key="jd_input", 
        label_visibility="hidden"
    )
    st.markdown(f"### {get_text('resume_upload')}")
    uploaded_files = st.file_uploader(
        "Resume Files", 
        type=["pdf"], 
        accept_multiple_files=True, 
        key="file_uploader", 
        label_visibility="hidden"
    )
    if uploaded_files: 
        st.success(f"{len(uploaded_files)} {get_text('files_selected')}")
    start_button = st.button(get_text("resume_start"), use_container_width=True, type="primary", disabled=st.session_state['processing'])

with col_right:
    if start_button and jd_input and uploaded_files:
        st.session_state['processing'] = True
        progress_bar = st.progress(0)
        status = st.empty()
        files = [("resumes", (f.name, f.getvalue(), "application/pdf")) for f in uploaded_files]
        payload = {"jd_text": jd_input, "output_lang": st.session_state.get('language', 'English')}
        try:
            status.info(get_text("resume_uploading")); 
            progress_bar.progress(25)
            res = requests.post("http://localhost:8000/screen", data=payload, files=files, timeout=120)
            status.info(get_text("resume_analyzing")); 
            progress_bar.progress(75)
            if res.status_code == 200:
                st.session_state['results'] = res.json()
                progress_bar.progress(100)
                status.success(get_text("resume_complete"))
                st.balloons() 
                time.sleep(1)
                st.rerun()
            else: 
                st.error(f"{get_text('error')}: {res.status_code}")
        except requests.exceptions.ConnectionError:
            st.error(get_text("resume_error_connection"))
        except requests.exceptions.Timeout:
            st.error(get_text("resume_error_timeout"))
        except Exception as e: 
            st.error(f"{get_text('error')}: {e}")
        finally: 
            progress_bar.empty()
            status.empty()
            st.session_state['processing'] = False
    elif start_button and not jd_input: 
        st.error(get_text("resume_jd_required"))
    elif start_button and not uploaded_files: 
        st.error(get_text("resume_files_required"))
    
    tab1, tab2 = st.tabs([get_text("resume_results"), get_text("statistics")])
    with tab1:
        if st.session_state['results']:
            results = st.session_state['results']
            render_metric_cards(results)
            st.subheader(get_text("resume_ranking"))
            df = pd.DataFrame(results)
            if not df.empty:
                fig = px.bar(df, x='score', y='candidate_name', orientation='h', color='score', text='score', title=get_text("resume_ranking"))
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                for idx, c in enumerate(results): 
                    render_candidate_card(c, idx)
        else: 
            st.info(get_text("resume_no_results"))
    with tab2:
        if st.session_state['results']:
            results = st.session_state['results']
            scores = [r['score'] for r in results]
            fig = px.histogram(x=scores, nbins=10, title=get_text("score_distribution"))
            fig.update_layout(xaxis_title=get_text("resume_score"), yaxis_title=get_text("chart_count"))
            st.plotly_chart(fig, use_container_width=True)
            all_skills = [s for r in results for s in r.get('matched_skills', [])]
            if all_skills:
                skills_df = pd.DataFrame(Counter(all_skills).most_common(10), columns=['Skill', 'Count'])
                fig2 = px.bar(skills_df, x='Count', y='Skill', orientation='h', color='Count', title=get_text("top_skills"))
                st.plotly_chart(fig2, use_container_width=True)
        else: 
            st.info(get_text("no_data"))