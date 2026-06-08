import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from components.language_manager import get_text, init_language

init_language()

st.set_page_config(page_title=get_text("dashboard_title"), layout="wide", page_icon="📊", initial_sidebar_state="collapsed")

css_path = Path(__file__).parent.parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<style>[data-testid="stSidebar"] { display: none; } button[data-testid="baseButton-header"] { display: none; }</style>""", unsafe_allow_html=True)

if st.button("Back to Home"): st.switch_page("app.py")

st.markdown(f"""<div class="premium-header" style="padding: 1.5rem;"><div class="premium-title">{get_text('dashboard_title')}</div><div class="premium-subtitle">Real-time HR analytics and insights</div></div>""", unsafe_allow_html=True)

API_URL = "http://localhost:8000/api"

try:
    response = requests.get(f"{API_URL}/dashboard/stats")
    if response.status_code == 200:
        stats = response.json()
        col1, col2, col3, col4 = st.columns(4)
        with col1: st.metric("Total Employees", stats.get('total_employees', 0))
        with col2: st.metric("Turnover Rate", f"{stats.get('turnover_rate', 0)}%")
        with col3: st.metric("Open Positions", stats.get('candidates_by_status', {}).get('new', 0))
        with col4: st.metric("Upcoming Interviews", stats.get('upcoming_interviews', 0))
        col1, col2 = st.columns(2)
        with col1:
            dept_data = stats.get('employees_by_dept', {})
            if dept_data:
                df = pd.DataFrame(list(dept_data.items()), columns=['Department', 'Count'])
                fig = px.pie(df, values='Count', names='Department', hole=0.4)
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
        with col2:
            cand_data = stats.get('candidates_by_status', {})
            if cand_data:
                df = pd.DataFrame(list(cand_data.items()), columns=['Stage', 'Count'])
                fig = px.bar(df, x='Stage', y='Count', color='Count', color_continuous_scale='Blues')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
    else: st.error("Failed to load")
except: st.error("Cannot connect to backend")
