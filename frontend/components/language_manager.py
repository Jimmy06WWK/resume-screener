
import streamlit as st

TEXTS = {
    "English": {
        # Navigation
        "nav_employee_db": "Employee Database",
        "nav_recruitment": "Recruitment Pipeline",
        "nav_dashboard": "HR Dashboard",
        "nav_resume_screener": "Resume Screener",
        
        # Landing Page
        "app_title": "AI HR Management System",
        "app_subtitle": "Intelligent Recruitment | Employee Management | HR Analytics",
        "key_features": "Key Features",
        "feature_ai_resume": "AI Resume Screener",
        "feature_ai_resume_desc": "Smart resume analysis with Gemini AI",
        "feature_employee_db": "Employee Database",
        "feature_employee_db_desc": "Centralized employee records management",
        "feature_recruitment": "Recruitment Pipeline",
        "feature_recruitment_desc": "Kanban-style candidate tracking",
        "feature_hr_analytics": "HR Analytics",
        "feature_hr_analytics_desc": "Real-time dashboard and insights",
        "quick_actions": "Quick Actions",
        "screen_resumes": "Screen Resumes",
        "manage_employees": "Manage Employees",
        "view_dashboard": "View Dashboard",
        
        # Employee Database
        "emp_title": "Employee Database",
        "emp_list": "Employee List",
        "emp_add": "Add Employee",
        "emp_stats": "Statistics",
        "emp_search": "Search Employee",
        "emp_total": "Total Employees",
        "emp_active": "Active",
        "emp_departments": "Departments",
        "emp_avg_salary": "Avg Salary",
        "emp_avg_score": "Average Score",
        "emp_no_data": "No employee data available",
        "emp_code": "Employee Code",
        "emp_first_name": "First Name",
        "emp_last_name": "Last Name",
        "emp_thai_name": "Thai Name",
        "emp_department": "Department",
        "emp_position": "Position",
        "emp_level": "Level",
        "emp_hire_date": "Hire Date",
        "emp_birth_date": "Birth Date",
        "emp_email": "Email",
        "emp_phone": "Phone",
        "emp_address": "Address",
        "emp_salary": "Salary (THB)",
        "emp_bank": "Bank",
        "emp_bank_account": "Bank Account Number",
        
        # Recruitment Pipeline
        "rec_title": "Recruitment Pipeline",
        "rec_new": "New",
        "rec_screening": "Screening",
        "rec_interview": "Interview",
        "rec_offer": "Offer",
        "rec_hired": "Hired",
        "rec_rejected": "Rejected",
        "rec_add_candidate": "Add New Candidate",
        "rec_upcoming": "Upcoming Interviews",
        "rec_candidate_name": "Name",
        "rec_candidate_email": "Email",
        "rec_candidate_phone": "Phone",
        "rec_position": "Position Applied",
        "rec_score": "AI Score",
        "rec_no_candidates": "No candidates in this stage",
        "rec_no_upcoming": "No upcoming interviews scheduled",
        
        # HR Dashboard
        "dashboard_title": "HR Dashboard",
        "dashboard_total_employees": "Total Employees",
        "dashboard_turnover": "Turnover Rate",
        "dashboard_open_positions": "Open Positions",
        "dashboard_upcoming": "Upcoming Interviews",
        "dashboard_by_dept": "Employees by Department",
        "dashboard_pipeline": "Candidate Pipeline",
        "dashboard_recent_hires": "Recent Hires",
        "dashboard_alerts": "Alerts",
        "dashboard_no_dept_data": "No department data",
        "dashboard_no_candidate_data": "No candidate data",
        "dashboard_no_recent_hires": "No recent hires",
        "dashboard_probation_alert": "{name} - Probation ends soon",
        "dashboard_no_alerts": "No pending probation endings",
        
        # Resume Screener
        "resume_title": "AI Resume Screener",
        "resume_subtitle": "Intelligent resume screening powered by Google Gemini AI",
        "resume_jd": "Job Description",
        "resume_upload": "Upload Resumes",
        "resume_start": "Start Analysis",
        "resume_results": "Results",
        "resume_ranking": "Ranking Overview",
        "resume_details": "Candidate Details",
        "resume_uploading": "Uploading files to server...",
        "resume_analyzing": "AI is analyzing resumes...",
        "resume_complete": "Analysis complete!",
        "resume_no_results": "No results yet. Upload resumes and click Start Analysis",
        "resume_error_connection": "Cannot connect to backend server",
        "resume_error_timeout": "Request timed out. Please try again",
        
        # Common
        "search": "Search...",
        "add": "Add",
        "edit": "Edit",
        "delete": "Delete",
        "cancel": "Cancel",
        "save": "Save",
        "confirm": "Confirm",
        "loading": "Loading...",
        "error": "Error",
        "success": "Success",
        "language": "Language",
        "filter_by": "Filter by",
        "status": "Status",
        "all": "All",
        "active": "Active",
        "resigned": "Resigned",
        "back_to_home": "Back to Home",
        "no_data": "No data available",
        
        # Pipeline status messages
        "status_new": "New",
        "status_screening": "Screening", 
        "status_interview": "Interview",
        "status_offer": "Offer",
        "status_hired": "Hired",
        "status_rejected": "Rejected"
    },
    "Thai": {
        # Navigation
        "nav_employee_db": "ฐานข้อมูลพนักงาน",
        "nav_recruitment": "ระบบสรรหาบุคลากร",
        "nav_dashboard": "แดชบอร์ด HR",
        "nav_resume_screener": "สแกนเรซูเม่",
        
        # Landing Page
        "app_title": "ระบบบริหารทรัพยากรบุคคล AI",
        "app_subtitle": "สรรหาอัจฉริยะ | จัดการพนักงาน | วิเคราะห์ HR",
        "key_features": "ฟีเจอร์หลัก",
        "feature_ai_resume": "สแกนเรซูเม่ด้วย AI",
        "feature_ai_resume_desc": "วิเคราะห์เรซูเม่อัจฉริยะด้วย Gemini AI",
        "feature_employee_db": "ฐานข้อมูลพนักงาน",
        "feature_employee_db_desc": "จัดการข้อมูลพนักงานแบบรวมศูนย์",
        "feature_recruitment": "ระบบสรรหาบุคลากร",
        "feature_recruitment_desc": "ติดตามผู้สมัครแบบ Kanban",
        "feature_hr_analytics": "วิเคราะห์ทรัพยากรบุคคล",
        "feature_hr_analytics_desc": "แดชบอร์ดและข้อมูลเชิงลึกแบบเรียลไทม์",
        "quick_actions": "คำสั่งด่วน",
        "screen_resumes": "สแกนเรซูเม่",
        "manage_employees": "จัดการพนักงาน",
        "view_dashboard": "ดูแดชบอร์ด",
        
        # Employee Database
        "emp_title": "ฐานข้อมูลพนักงาน",
        "emp_list": "รายชื่อพนักงาน",
        "emp_add": "เพิ่มพนักงาน",
        "emp_stats": "สถิติ",
        "emp_search": "ค้นหาพนักงาน",
        "emp_total": "พนักงานทั้งหมด",
        "emp_active": "กำลังทำงาน",
        "emp_departments": "แผนก",
        "emp_avg_salary": "เงินเดือนเฉลี่ย",
        "emp_avg_score": "คะแนนเฉลี่ย",
        "emp_no_data": "ไม่มีข้อมูลพนักงาน",
        "emp_code": "รหัสพนักงาน",
        "emp_first_name": "ชื่อ",
        "emp_last_name": "นามสกุล",
        "emp_thai_name": "ชื่อภาษาไทย",
        "emp_department": "แผนก",
        "emp_position": "ตำแหน่ง",
        "emp_level": "ระดับ",
        "emp_hire_date": "วันที่เริ่มงาน",
        "emp_birth_date": "วันเกิด",
        "emp_email": "อีเมล",
        "emp_phone": "เบอร์โทร",
        "emp_address": "ที่อยู่",
        "emp_salary": "เงินเดือน (บาท)",
        "emp_bank": "ธนาคาร",
        "emp_bank_account": "เลขที่บัญชี",
        
        # Recruitment Pipeline
        "rec_title": "ระบบสรรหาบุคลากร",
        "rec_new": "ใหม่",
        "rec_screening": "กำลังตรวจสอบ",
        "rec_interview": "สัมภาษณ์",
        "rec_offer": "เสนอ offer",
        "rec_hired": "รับงานแล้ว",
        "rec_rejected": "ไม่ผ่าน",
        "rec_add_candidate": "เพิ่มผู้สมัครใหม่",
        "rec_upcoming": "การสัมภาษณ์ที่จะถึง",
        "rec_candidate_name": "ชื่อ",
        "rec_candidate_email": "อีเมล",
        "rec_candidate_phone": "เบอร์โทร",
        "rec_position": "ตำแหน่งที่สมัคร",
        "rec_score": "คะแนน AI",
        "rec_no_candidates": "ไม่มีผู้สมัครในขั้นตอนนี้",
        "rec_no_upcoming": "ไม่มีการนัดสัมภาษณ์ที่กำลังจะถึง",
        
        # HR Dashboard
        "dashboard_title": "แดชบอร์ด HR",
        "dashboard_total_employees": "พนักงานทั้งหมด",
        "dashboard_turnover": "อัตราการออกงาน",
        "dashboard_open_positions": "ตำแหน่งว่าง",
        "dashboard_upcoming": "สัมภาษณ์ที่จะถึง",
        "dashboard_by_dept": "พนักงานแยกตามแผนก",
        "dashboard_pipeline": "สถานะผู้สมัคร",
        "dashboard_recent_hires": "พนักงานใหม่ล่าสุด",
        "dashboard_alerts": "การแจ้งเตือน",
        "dashboard_no_dept_data": "ไม่มีข้อมูลแผนก",
        "dashboard_no_candidate_data": "ไม่มีข้อมูลผู้สมัคร",
        "dashboard_no_recent_hires": "ไม่มีพนักงานใหม่",
        "dashboard_probation_alert": "{name} - กำลังจะหมดโปรเบชัน",
        "dashboard_no_alerts": "ไม่มีการแจ้งเตือน",
        
        # Resume Screener
        "resume_title": "สแกนเรซูเม่ด้วย AI",
        "resume_subtitle": "วิเคราะห์เรซูเม่อัจฉริยะด้วย Google Gemini AI",
        "resume_jd": "รายละเอียดงาน",
        "resume_upload": "อัปโหลดเรซูเม่",
        "resume_start": "เริ่มวิเคราะห์",
        "resume_results": "ผลการวิเคราะห์",
        "resume_ranking": "อันดับผู้สมัคร",
        "resume_details": "รายละเอียดผู้สมัคร",
        "resume_uploading": "กำลังส่งไฟล์ไปยังเซิร์ฟเวอร์...",
        "resume_analyzing": "AI กำลังวิเคราะห์เรซูเม่...",
        "resume_complete": "วิเคราะห์เสร็จสิ้น!",
        "resume_no_results": "ยังไม่มีผลลัพธ์ อัปโหลดเรซูเม่และคลิกเริ่มวิเคราะห์",
        "resume_error_connection": "ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ได้",
        "resume_error_timeout": "การเชื่อมต่อหมดเวลา กรุณาลองอีกครั้ง",
        
        # Common
        "search": "ค้นหา...",
        "add": "เพิ่ม",
        "edit": "แก้ไข",
        "delete": "ลบ",
        "cancel": "ยกเลิก",
        "save": "บันทึก",
        "confirm": "ยืนยัน",
        "loading": "กำลังโหลด...",
        "error": "เกิดข้อผิดพลาด",
        "success": "สำเร็จ",
        "language": "ภาษา",
        "filter_by": "ตัวกรอง",
        "status": "สถานะ",
        "all": "ทั้งหมด",
        "active": "กำลังทำงาน",
        "resigned": "ออกแล้ว",
        "back_to_home": "กลับหน้าแรก",
        "no_data": "ไม่มีข้อมูล",
        
        # Pipeline status messages
        "status_new": "ใหม่",
        "status_screening": "กำลังตรวจสอบ",
        "status_interview": "สัมภาษณ์",
        "status_offer": "เสนอ offer",
        "status_hired": "รับงานแล้ว",
        "status_rejected": "ไม่ผ่าน"
    },
    "Chinese": {
        # Navigation
        "nav_employee_db": "员工数据库",
        "nav_recruitment": "招聘流程",
        "nav_dashboard": "HR仪表板",
        "nav_resume_screener": "简历筛选器",
        
        # Landing Page
        "app_title": "AI人力资源管理系统",
        "app_subtitle": "智能招聘 | 员工管理 | 人力资源分析",
        "key_features": "主要功能",
        "feature_ai_resume": "AI简历筛选",
        "feature_ai_resume_desc": "使用Gemini AI智能分析简历",
        "feature_employee_db": "员工数据库",
        "feature_employee_db_desc": "集中式员工记录管理",
        "feature_recruitment": "招聘流程",
        "feature_recruitment_desc": "看板式候选人跟踪",
        "feature_hr_analytics": "人力资源分析",
        "feature_hr_analytics_desc": "实时仪表板和洞察",
        "quick_actions": "快速操作",
        "screen_resumes": "筛选简历",
        "manage_employees": "管理员工",
        "view_dashboard": "查看仪表板",
        
        # Employee Database
        "emp_title": "员工数据库",
        "emp_list": "员工列表",
        "emp_add": "添加员工",
        "emp_stats": "统计",
        "emp_search": "搜索员工",
        "emp_total": "员工总数",
        "emp_active": "在职",
        "emp_departments": "部门",
        "emp_avg_salary": "平均工资",
        "emp_avg_score": "平均分",
        "emp_no_data": "没有员工数据",
        "emp_code": "员工编号",
        "emp_first_name": "名",
        "emp_last_name": "姓",
        "emp_thai_name": "泰文名",
        "emp_department": "部门",
        "emp_position": "职位",
        "emp_level": "级别",
        "emp_hire_date": "入职日期",
        "emp_birth_date": "出生日期",
        "emp_email": "电子邮箱",
        "emp_phone": "电话",
        "emp_address": "地址",
        "emp_salary": "工资(泰铢)",
        "emp_bank": "银行",
        "emp_bank_account": "银行账号",
        
        # Recruitment Pipeline
        "rec_title": "招聘流程",
        "rec_new": "新候选人",
        "rec_screening": "筛选",
        "rec_interview": "面试",
        "rec_offer": "录用通知",
        "rec_hired": "已录用",
        "rec_rejected": "已拒绝",
        "rec_add_candidate": "添加新候选人",
        "rec_upcoming": "即将到来的面试",
        "rec_candidate_name": "姓名",
        "rec_candidate_email": "邮箱",
        "rec_candidate_phone": "电话",
        "rec_position": "申请职位",
        "rec_score": "AI评分",
        "rec_no_candidates": "此阶段没有候选人",
        "rec_no_upcoming": "没有即将到来的面试",
        
        # HR Dashboard
        "dashboard_title": "HR仪表板",
        "dashboard_total_employees": "员工总数",
        "dashboard_turnover": "离职率",
        "dashboard_open_positions": "空缺职位",
        "dashboard_upcoming": "即将到来的面试",
        "dashboard_by_dept": "按部门统计员工",
        "dashboard_pipeline": "候选人流程",
        "dashboard_recent_hires": "最近录用",
        "dashboard_alerts": "提醒",
        "dashboard_no_dept_data": "没有部门数据",
        "dashboard_no_candidate_data": "没有候选人数据",
        "dashboard_no_recent_hires": "没有最近录用",
        "dashboard_probation_alert": "{name} - 试用期即将结束",
        "dashboard_no_alerts": "没有提醒",
        
        # Resume Screener
        "resume_title": "AI简历筛选器",
        "resume_subtitle": "由Google Gemini AI驱动的智能简历筛选",
        "resume_jd": "职位描述",
        "resume_upload": "上传简历",
        "resume_start": "开始分析",
        "resume_results": "结果",
        "resume_ranking": "排名概览",
        "resume_details": "候选人详情",
        "resume_uploading": "正在上传文件到服务器...",
        "resume_analyzing": "AI正在分析简历...",
        "resume_complete": "分析完成！",
        "resume_no_results": "暂无结果。上传简历并点击开始分析",
        "resume_error_connection": "无法连接到后端服务器",
        "resume_error_timeout": "请求超时，请重试",
        
        # Common
        "search": "搜索...",
        "add": "添加",
        "edit": "编辑",
        "delete": "删除",
        "cancel": "取消",
        "save": "保存",
        "confirm": "确认",
        "loading": "加载中...",
        "error": "错误",
        "success": "成功",
        "language": "语言",
        "filter_by": "筛选",
        "status": "状态",
        "all": "全部",
        "active": "在职",
        "resigned": "已离职",
        "back_to_home": "返回首页",
        "no_data": "无数据",
        
        # Pipeline status messages
        "status_new": "新候选人",
        "status_screening": "筛选中",
        "status_interview": "面试中",
        "status_offer": "录用通知",
        "status_hired": "已录用",
        "status_rejected": "已拒绝"
    }
}

def get_text(key):
    """Get text for current language"""
    lang = st.session_state.get('language', 'English')
    return TEXTS.get(lang, TEXTS['English']).get(key, key)

def init_language():
    """Initialize language setting"""
    if 'language' not in st.session_state:
        st.session_state['language'] = 'English'

def set_language(lang):
    """Set language"""
    if lang != st.session_state.get('language'):
        st.session_state['language'] = lang
        st.rerun()

def render_language_selector():
    """Render language selector in sidebar"""
    st.markdown("---")
    st.markdown(get_text("language"))
    
    current_lang = st.session_state.get('language', 'English')
    
    lang_options = {
        "English": "English",
        "Thai": "ไทย",
        "Chinese": "中文"
    }
    
    selected_lang = st.radio(
        "",
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=list(lang_options.keys()).index(current_lang),
        key="lang_selector",
        label_visibility="collapsed",
        horizontal=True
    )
    
    if selected_lang != current_lang:
        set_language(selected_lang)
