import streamlit as st
from components.language_manager import get_text, init_language, set_language
from pathlib import Path

init_language()

st.set_page_config(
    page_title=get_text("app_title"),  # Changed to use translation
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load premium CSS
css_path = Path(__file__).parent / "assets" / "style.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero Section
st.markdown(f"""
    <div class="hero-section">
        <div class="hero-glow"></div>
        <div class="hero-content">
            <div class="hero-icon">AI</div>
            <div class="hero-title">{get_text('app_title')}</div>
            <div class="hero-subtitle">{get_text('app_subtitle')}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Language Selection Card
st.markdown(f"""
    <div class="language-card">
        <div class="language-card-title">{get_text('select_language')}</div>
        <div class="language-buttons">
    </div>
""", unsafe_allow_html=True)

# Language buttons
current_lang = st.session_state.get('language', 'Thai')  # Changed default to Thai if you prefer

# Define language options with proper display names
lang_options = [
    {"code": "English", "name": get_text('lang_english'), "local": "🇬🇧 English"},
    {"code": "Thai", "name": get_text('lang_thai'), "local": "🇹🇭 ภาษาไทย"},
    {"code": "Chinese", "name": get_text('lang_chinese'), "local": "🇨🇳 中文"}
]

cols = st.columns(3)
for idx, lang in enumerate(lang_options):
    with cols[idx]:
        is_active = current_lang == lang["code"]
        # Style the active language button differently
        button_label = f"✅ {lang['local']}" if is_active else lang['local']
        if st.button(
            button_label, 
            key=f"lang_{lang['code']}",
            use_container_width=True
        ):
            if not is_active:
                set_language(lang["code"])
                st.rerun()

st.markdown('</div></div>', unsafe_allow_html=True)

# Navigation Cards
st.markdown('<div class="nav-grid">', unsafe_allow_html=True)

nav_items = [
    {"title": get_text('feature_ai_resume'), "desc": get_text('feature_ai_resume_desc'), "page": "pages/4_Resume_Screener.py", "color": "#5b8caf"},
    {"title": get_text('feature_employee_db'), "desc": get_text('feature_employee_db_desc'), "page": "pages/1_Employee_Database.py", "color": "#6fb398"},
    {"title": get_text('feature_recruitment'), "desc": get_text('feature_recruitment_desc'), "page": "pages/2_Recruitment_Pipeline.py", "color": "#d4a45a"},
    {"title": get_text('feature_hr_analytics'), "desc": get_text('feature_hr_analytics_desc'), "page": "pages/3_HR_Dashboard.py", "color": "#d48474"}
]

cols = st.columns(4)
for idx, item in enumerate(nav_items):
    with cols[idx]:
        st.markdown(f"""
            <div class="nav-card" style="border-top: 3px solid {item['color']};">
                <div class="nav-card-title">{item['title']}</div>
                <div class="nav-card-desc">{item['desc']}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"{get_text('launch')} {item['title']}", key=f"nav_{idx}", use_container_width=True):
            st.switch_page(item["page"])

st.markdown('</div>', unsafe_allow_html=True)

# Stats Preview
st.markdown("---")
st.markdown('<div class="stats-preview">', unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #7a9bb0;'>{get_text('footer_text')}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
    <div class="premium-footer">
        <p>{get_text('footer_powered_by')}</p>
    </div>
""", unsafe_allow_html=True)