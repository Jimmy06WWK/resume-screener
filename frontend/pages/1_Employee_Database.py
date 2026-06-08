import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from components.language_manager import get_text, init_language

init_language()

st.set_page_config(page_title=get_text("emp_title"), layout="wide", page_icon="👥", initial_sidebar_state="collapsed")

# Load CSS
css_path = Path(__file__).parent.parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hide sidebar
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    button[data-testid="baseButton-header"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# Back button
if st.button("Back to Home", use_container_width=False):
    st.switch_page("app.py")

st.markdown(f"""
    <div class="premium-header" style="padding: 1.5rem;">
        <div class="premium-title">{get_text('emp_title')}</div>
        <div class="premium-subtitle">Manage employee records efficiently</div>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab_list, tab_add, tab_stats = st.tabs([
    get_text("emp_list"), 
    get_text("emp_add"), 
    get_text("emp_stats")
])

API_URL = "http://localhost:8000/api"

with tab_list:
    col1, col2 = st.columns([3, 1])
    with col2:
        status_filter = st.selectbox(get_text("filter_by"), [get_text("active"), get_text("all"), get_text("resigned")])
    with col1:
        search = st.text_input(get_text("emp_search"), placeholder=get_text("search"))
    
    status_map = {get_text("active"): "active", get_text("all"): "all", get_text("resigned"): "resigned"}
    status_value = status_map.get(status_filter, "active")
    
    try:
        response = requests.get(f"{API_URL}/employees", params={"status": status_value})
        if response.status_code == 200:
            employees = response.json()
            if search:
                employees = [e for e in employees if search.lower() in e['first_name'].lower() or search.lower() in e['last_name'].lower() or search.lower() in e['employee_code'].lower()]
            st.markdown(f"**{get_text('emp_total')}: {len(employees)}**")
            for emp in employees:
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
                    with col1:
                        st.markdown(f"**{emp['first_name']} {emp['last_name']}**\n{emp['employee_code']}")
                    with col2:
                        st.write(f"**{emp['position']}**\n{emp['department']}")
                    with col3:
                        st.write(f"{emp['email']}\n{emp['phone']}")
                    with col4:
                        status_text = get_text("active") if emp['status'] == 'active' else get_text("resigned")
                        st.markdown(f'<span style="background: {"#6fb398" if emp["status"] == "active" else "#d48474"}20; color: {"#6fb398" if emp["status"] == "active" else "#d48474"}; padding: 4px 12px; border-radius: 20px;">{status_text}</span>', unsafe_allow_html=True)
                    with st.expander("View Details"):
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.write(f"**Level:** {emp.get('level', '-')}")
                            st.write(f"**Hire Date:** {emp.get('hire_date', '-')}")
                        with col_b:
                            st.write(f"**Salary:** ฿{emp.get('salary', 0):,.2f}")
                            st.write(f"**Bank:** {emp.get('bank_name', '-')}")
                    st.divider()
    except Exception as e:
        st.error(f"Error: {e}")

with tab_add:
    with st.form("add_employee_form"):
        col1, col2 = st.columns(2)
        with col1:
            emp_code = st.text_input("Employee Code*")
            first_name = st.text_input("First Name*")
            last_name = st.text_input("Last Name*")
            department = st.selectbox("Department*", ["Engineering", "HR", "Sales", "Marketing", "Finance"])
            position = st.text_input("Position*")
            level = st.selectbox("Level*", ["Junior", "Senior", "Manager", "Director"])
        with col2:
            email = st.text_input("Email*")
            phone = st.text_input("Phone*")
            hire_date = st.date_input("Hire Date*", datetime.now())
            salary = st.number_input("Salary (THB)", min_value=0, step=1000)
            bank_name = st.selectbox("Bank", ["Kasikorn", "SCB", "Bangkok Bank", "Krungsri"])
            bank_account = st.text_input("Bank Account")
        submitted = st.form_submit_button("Add Employee", use_container_width=True)
        if submitted and emp_code and first_name and last_name and email and phone:
            data = {"employee_code": emp_code, "first_name": first_name, "last_name": last_name, "department": department, "position": position, "level": level, "hire_date": hire_date.isoformat(), "email": email, "phone": phone, "salary": salary, "bank_name": bank_name, "bank_account": bank_account}
            try:
                r = requests.post(f"{API_URL}/employees", json=data)
                if r.status_code == 200:
                    st.success("Employee added!")
                    st.rerun()
            except: st.error("Error")
        elif submitted: st.error("Please fill required fields")

with tab_stats:
    try:
        response = requests.get(f"{API_URL}/employees", params={"status": "all"})
        if response.status_code == 200:
            employees = response.json()
            df = pd.DataFrame(employees)
            if not df.empty:
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Total", len(df))
                with col2: st.metric("Active", len(df[df['status'] == 'active']))
                with col3: st.metric("Departments", df['department'].nunique())
                dept_stats = df[df['status'] == 'active']['department'].value_counts()
                fig = px.bar(x=dept_stats.index, y=dept_stats.values, title="Employees by Department", color=dept_stats.values, color_continuous_scale='Blues')
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
            else: st.info("No data")
    except: st.error("Error loading stats")
