import streamlit as st
import pandas as pd
from datetime import datetime, time as dt_time, timedelta, date

# Page configuration
st.set_page_config(
    page_title="MedTimer - Medicine Reminder",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'medicines' not in st.session_state:
    st.session_state.medicines = []
if 'taken_medicines' not in st.session_state:
    st.session_state.taken_medicines = {}
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'welcome'
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''
if 'selected_turtle' not in st.session_state:
    st.session_state.selected_turtle = '🐢'
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# Theme colors
def get_theme_colors():
    if st.session_state.theme == 'dark':
        return {
            'bg': '#1a1a1a',
            'card_bg': '#2a2a2a',
            'text': '#ffffff',
            'secondary_text': '#cccccc',
            'border': '#444444'
        }
    elif st.session_state.theme == 'high-contrast':
        return {
            'bg': '#000000',
            'card_bg': '#000000',
            'text': '#ffff00',
            'secondary_text': '#ffff00',
            'border': '#ffff00'
        }
    else:
        return {
            'bg': 'linear-gradient(135deg, #a8e6cf 0%, #dcedc8 50%, #b2dfdb 100%)',
            'card_bg': '#ffffff',
            'text': '#333333',
            'secondary_text': '#666666',
            'border': '#dddddd'
        }

colors = get_theme_colors()

# CSS
st.markdown(f"""
<style>
    .stApp {{
        background: {colors['bg']};
    }}
    
    /* Labels */
    label, .stMarkdown {{
        color: {colors['text']} !important;
    }}
    
    /* ALL Input Fields - Force White Background */
    input {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
        -webkit-text-fill-color: #000000 !important;
    }}
    
    textarea {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Text Input */
    .stTextInput > div > div > input {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Time Input */
    .stTimeInput > div > div > input {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Number Input */
    .stNumberInput > div > div > input {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Select Box - Main Container */
    .stSelectbox > div > div {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Select Box - Inner Div */
    [data-baseweb="select"] {{
        background-color: #ffffff !important;
    }}
    
    [data-baseweb="select"] > div {{
        background-color: #ffffff !important;
        color: #000000 !important;
    }}
    
    /* Select Box Text */
    [data-baseweb="select"] span {{
        color: #000000 !important;
    }}
    
    /* Dropdown Arrow */
    [data-baseweb="select"] svg {{
        fill: #000000 !important;
    }}
    
    /* Dropdown Menu */
    [data-baseweb="popover"] {{
        background-color: #ffffff !important;
    }}
    
    [role="listbox"] {{
        background-color: #ffffff !important;
    }}
    
    [role="option"] {{
        background-color: #ffffff !important;
        color: #000000 !important;
    }}
    
    [role="option"]:hover {{
        background-color: #e0e0e0 !important;
        color: #000000 !important;
    }}
    
    /* Buttons - Force White Background */
    .stButton > button {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #667eea !important;
        font-weight: bold !important;
    }}
    
    .stButton > button:hover {{
        background-color: #667eea !important;
        color: #ffffff !important;
    }}
    
    /* Download Button */
    .stDownloadButton > button {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #667eea !important;
    }}
    
    .stDownloadButton > button:hover {{
        background-color: #667eea !important;
        color: #ffffff !important;
    }}
    
    .medicine-card {{
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }}
    .taken {{ background: #c8e6c9; color: #000; border-left: 5px solid #4caf50; }}
    .upcoming {{ background: #fff9c4; color: #000; border-left: 5px solid #ffeb3b; }}
    .missed {{ background: #ffcdd2; color: #000; border-left: 5px solid #f44336; }}
    
    .badge {{
        display: inline-block;
        padding: 15px 25px;
        border-radius: 30px;
        margin: 10px;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .badge-gold {{ 
        background: linear-gradient(135deg, #ffd700, #ffed4e); 
        color: #333;
        border: 3px solid #b8860b;
    }}
    .badge-silver {{ 
        background: linear-gradient(135deg, #e8e8e8, #c0c0c0); 
        color: #333;
        border: 3px solid #888888;
    }}
    .badge-bronze {{ 
        background: linear-gradient(135deg, #cd7f32, #b8860b); 
        color: white;
        border: 3px solid #8b4513;
    }}
    
    .header-btn {{
        padding: 10px 20px;
        border-radius: 10px;
        background: white;
        border: 2px solid #667eea;
        color: #667eea;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
    }}
    
    .header-btn:hover {{
        background: #667eea;
        color: white;
    }}
    
    /* Sidebar styling - Force white background and black text */
    [data-testid="stSidebar"] {{
        background-color: #ffffff !important;
    }}
    
    [data-testid="stSidebar"] * {{
        color: #000000 !important;
    }}
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div {{
        color: #000000 !important;
    }}
    
    [data-testid="stSidebar"] .stMarkdown {{
        color: #000000 !important;
    }}
    
    /* Sidebar inputs */
    [data-testid="stSidebar"] input,
    [data-testid="stSidebar"] select,
    [data-testid="stSidebar"] textarea {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #888888 !important;
    }}
    
    /* Sidebar select boxes */
    [data-testid="stSidebar"] [data-baseweb="select"] {{
        background-color: #ffffff !important;
    }}
    
    [data-testid="stSidebar"] [data-baseweb="select"] > div {{
        background-color: #ffffff !important;
        color: #000000 !important;
    }}
    
    [data-testid="stSidebar"] [data-baseweb="select"] span {{
        color: #000000 !important;
    }}
    
    /* Sidebar buttons */
    [data-testid="stSidebar"] .stButton > button {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #667eea !important;
    }}
    
    [data-testid="stSidebar"] .stButton > button:hover {{
        background-color: #667eea !important;
        color: #ffffff !important;
    }}
    
    [data-testid="stSidebar"] .stDownloadButton > button {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #667eea !important;
    }}
    
    [data-testid="stSidebar"] .stDownloadButton > button:hover {{
        background-color: #667eea !important;
        color: #ffffff !important;
    }}
    
    /* Sidebar checkbox */
    [data-testid="stSidebar"] .stCheckbox {{
        color: #000000 !important;
    }}
    
    [data-testid="stSidebar"] .stCheckbox label {{
        color: #000000 !important;
    }}
    
    /* Sidebar info boxes */
    [data-testid="stSidebar"] .stAlert {{
        background-color: #e3f2fd !important;
        color: #000000 !important;
    }}
    
    h1, h2, h3, h4, h5, h6, p, span, div {{
        color: {colors['text']};
    }}
</style>
""", unsafe_allow_html=True)

# Helper functions
def get_medicine_status(medicine, med_time):
    today = datetime.now().strftime('%Y-%m-%d')
    day_name = datetime.now().strftime('%A')
    now = datetime.now()
    
    if medicine['frequency'] == 'specific':
        if day_name not in medicine.get('specific_days', []):
            return 'not-today'
    elif medicine['frequency'] == 'monthly':
        if datetime.now().day != 1:
            return 'not-today'
    
    med_datetime = datetime.combine(datetime.now().date(), med_time)
    med_key = f"{medicine['name']}_{med_time}"
    
    if today in st.session_state.taken_medicines:
        if med_key in st.session_state.taken_medicines[today]:
            return 'taken'
    
    if now > med_datetime:
        return 'missed'
    else:
        return 'upcoming'

def calculate_adherence():
    today = datetime.now().strftime('%Y-%m-%d')
    today_medicines = [m for m in st.session_state.medicines 
                       if get_medicine_status(m, m['time']) != 'not-today']
    
    total = len(today_medicines)
    if total == 0:
        return 0
    
    taken = len(st.session_state.taken_medicines.get(today, []))
    return int((taken / total) * 100)

def calculate_streak():
    streak = 0
    for i in range(365):
        date_check = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        if date_check in st.session_state.taken_medicines:
            day_meds = len(st.session_state.medicines)
            taken = len(st.session_state.taken_medicines[date_check])
            if taken == day_meds and day_meds > 0:
                streak += 1
            else:
                break
        else:
            if i > 0:
                break
    return streak

def mark_as_taken(medicine, med_time):
    today = datetime.now().strftime('%Y-%m-%d')
    med_key = f"{medicine['name']}_{med_time}"
    
    if today not in st.session_state.taken_medicines:
        st.session_state.taken_medicines[today] = []
    
    if med_key not in st.session_state.taken_medicines[today]:
        st.session_state.taken_medicines[today].append(med_key)
        st.success(f"✅ Marked {medicine['name']} as taken!")
        st.rerun()

def get_motivational_quote(percentage):
    quotes = {
        0: "🌱 Every journey begins with a single step. Let's start today!",
        10: "💫 You've taken the first step! Your health journey has begun!",
        20: "🌟 Building momentum! Consistency is the key to success!",
        30: "⭐ You're making real progress! Keep this energy going!",
        40: "🎯 Almost halfway there! You're doing wonderfully!",
        50: "🏆 Halfway champion! Your dedication is inspiring!",
        60: "💪 Excellence is within reach! Keep pushing forward!",
        70: "🚀 You're soaring high! Almost at the finish line!",
        80: "💎 Excellence zone! Your commitment is remarkable!",
        90: "🎖️ Nearly perfect! Just one more push to greatness!",
        100: "🏅✨ PERFECT DAY! You're a medicine management superstar!"
    }
    
    for threshold in range(100, -1, -10):
        if percentage >= threshold:
            return quotes[threshold]
    return quotes[0]

def create_circular_progress(percentage):
    """Create circular progress with CSS"""
    return f"""
    <div style="display: flex; justify-content: center; align-items: center; margin: 30px 0;">
        <div style="position: relative; width: 250px; height: 250px;">
            <svg width="250" height="250" style="transform: rotate(-90deg);">
                <!-- Background circle -->
                <circle cx="125" cy="125" r="100" fill="none" stroke="#e0e0e0" stroke-width="25"/>
                <!-- Progress circle -->
                <circle cx="125" cy="125" r="100" fill="none" stroke="#4caf50" stroke-width="25"
                        stroke-dasharray="{percentage * 6.28} 628" stroke-linecap="round"/>
            </svg>
            <!-- Turtle in center -->
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 5em;">
                {st.session_state.selected_turtle}
            </div>
        </div>
    </div>
    <div style="text-align: center; margin-top: -30px;">
        <div style="font-size: 3em; font-weight: bold; color: #667eea;">{percentage}%</div>
    </div>
    """

# Welcome Page
def show_welcome_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center;'>🐢 MedTimer</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Your friendly companion for never missing a dose!</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("📅 **Daily Checklist**\n\nTrack medicines with color codes")
            st.info("📊 **Weekly Reports**\n\nMonitor your adherence")
        with col_b:
            st.info("⏰ **Smart Reminders**\n\nCustomizable notifications")
            st.info("🏆 **Achievements**\n\nEarn badges")
        
        st.markdown("---")
        st.subheader("⭐ What Our Users Say")
        st.success("⭐⭐⭐⭐⭐\n\n*Game-changer for my medications!* - Sarah, 62")
        st.success("⭐⭐⭐⭐⭐\n\n*Simple and effective!* - Michael, 45")
        
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.current_page = 'login'
            st.rerun()

# Login Page
def show_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center;'>🐢 Welcome!</h1>", unsafe_allow_html=True)
        st.markdown("---")
        name = st.text_input("Full Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        
        if st.button("Continue", use_container_width=True):
            if name and email:
                st.session_state.user_name = name
                st.session_state.user_email = email
                st.session_state.current_page = 'add_medicine'
                st.rerun()
            else:
                st.error("Please enter both name and email!")

# Add Medicine Page
def show_add_medicine_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center;'>➕ Add Medicine</h1>", unsafe_allow_html=True)
        
        medicine_name = st.text_input("Medicine Name", placeholder="e.g., Aspirin")
        dose = st.text_input("Dose", placeholder="e.g., 1 tablet")
        med_time = st.time_input("Time", value=dt_time(8, 0))
        frequency = st.selectbox("Frequency", ["daily", "specific", "monthly"])
        
        specific_days = []
        if frequency == "specific":
            st.write("**Select Days:**")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            cols = st.columns(4)
            for i, day in enumerate(days):
                with cols[i % 4]:
                    if st.checkbox(day, key=f"day_{day}"):
                        specific_days.append(day)
            st.info("💡 For alternate days, select Mon/Wed/Fri/Sun or Tue/Thu/Sat")
        
        multiple_times = st.checkbox("Take multiple times per day")
        additional_times = []
        
        if multiple_times:
            times_per_day = st.number_input("How many times?", min_value=2, max_value=10, value=2)
            for i in range(2, times_per_day + 1):
                add_time = st.time_input(f"Time {i}", value=dt_time(8 + i * 4, 0), key=f"time_{i}")
                additional_times.append(add_time)
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("Add Medicine", use_container_width=True):
                if medicine_name and dose:
                    medicine = {
                        'name': medicine_name,
                        'dose': dose,
                        'time': med_time,
                        'frequency': frequency,
                        'specific_days': specific_days
                    }
                    st.session_state.medicines.append(medicine)
                    
                    if multiple_times:
                        for add_time in additional_times:
                            med_copy = medicine.copy()
                            med_copy['time'] = add_time
                            st.session_state.medicines.append(med_copy)
                    
                    st.success("Medicine added!")
                else:
                    st.error("Please fill all fields!")
        
        with col_b:
            if st.button("Continue", use_container_width=True):
                if len(st.session_state.medicines) > 0:
                    st.session_state.current_page = 'confirmation'
                    st.rerun()
                else:
                    st.error("Please add at least one medicine!")

# Confirmation Page
def show_confirmation_page():
    st.markdown("<h1 style='text-align: center;'>📋 Confirm Your Medicines</h1>", unsafe_allow_html=True)
    
    if len(st.session_state.medicines) == 0:
        st.warning("No medicines added.")
    else:
        df_data = []
        for i, med in enumerate(st.session_state.medicines):
            freq_display = med['frequency']
            if med['frequency'] == 'specific' and med['specific_days']:
                freq_display += f" ({', '.join(med['specific_days'])})"
            
            df_data.append({
                '#': i + 1,
                'Medicine': med['name'],
                'Dose': med['dose'],
                'Time': med['time'].strftime('%H:%M'),
                'Frequency': freq_display
            })
        
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        med_to_delete = st.selectbox("Delete medicine (optional)", 
                                      ["None"] + [f"{i+1}. {m['name']}" for i, m in enumerate(st.session_state.medicines)])
        
        if med_to_delete != "None":
            if st.button("🗑️ Delete"):
                idx = int(med_to_delete.split('.')[0]) - 1
                st.session_state.medicines.pop(idx)
                st.rerun()
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("➕ Add More", use_container_width=True):
            st.session_state.current_page = 'add_medicine'
            st.rerun()
    
    with col2:
        if st.button("✅ Confirm & Start", use_container_width=True):
            if len(st.session_state.medicines) > 0:
                st.session_state.current_page = 'main_app'
                st.rerun()
            else:
                st.error("Add at least one medicine!")

# Main App
def show_main_app():
    # Header with buttons
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    
    with col1:
        st.markdown("<h2>🐢 MedTimer</h2>", unsafe_allow_html=True)
    
    with col2:
        streak = calculate_streak()
        if st.button(f"🔥 {streak} Day Streak", use_container_width=True):
            pass
    
    with col3:
        if st.button("📥 Report", use_container_width=True, key="report_btn"):
            st.session_state.show_report = not st.session_state.get('show_report', False)
            st.session_state.show_settings = False
            st.rerun()
    
    with col4:
        if st.button("⚙️ Settings", use_container_width=True, key="settings_btn"):
            st.session_state.show_settings = not st.session_state.get('show_settings', False)
            st.session_state.show_report = False
            st.rerun()
    
    # Sidebar for Settings
    if st.session_state.get('show_settings', False):
        with st.sidebar:
            st.markdown("### ⚙️ Settings")
            st.markdown("---")
            
            st.markdown("**🎨 Theme**")
            theme = st.selectbox("Choose theme", ["light", "dark", "high-contrast"], 
                                index=["light", "dark", "high-contrast"].index(st.session_state.theme),
                                label_visibility="collapsed")
            if theme != st.session_state.theme:
                st.session_state.theme = theme
                st.rerun()
            
            st.markdown("---")
            st.markdown("**🐾 Companion**")
            st.session_state.selected_turtle = st.selectbox("Pick your buddy", 
                                                             ["🐢", "🐶", "🐱", "🐼", "🦊", "🐰"],
                                                             index=["🐢", "🐶", "🐱", "🐼", "🦊", "🐰"].index(st.session_state.selected_turtle),
                                                             label_visibility="collapsed")
            
            st.markdown("---")
            st.markdown("**⏰ Reminders**")
            reminder_mins = st.number_input("Minutes before", 0, 60, 10, label_visibility="collapsed")
            audio_alert = st.checkbox("🔔 Audio Alert", True)
            
            st.markdown("---")
            if st.button("✓ Apply Settings", use_container_width=True):
                st.session_state.show_settings = False
                st.rerun()
    
    # Sidebar for Report Download
    if st.session_state.get('show_report', False):
        with st.sidebar:
            st.markdown("### 📥 Download Report")
            st.markdown("---")
            
            report_period = st.selectbox("Select period", ["Last 7 Days", "Last 30 Days"])
            
            if report_period == "Last 7 Days":
                days = 7
            else:
                days = 30
            
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=days)
            
            st.info(f"📅 {start_date} to {end_date}")
            
            report_data = f"MedTimer Report\n{'='*40}\n"
            report_data += f"Period: {start_date} to {end_date}\n"
            report_data += f"User: {st.session_state.user_name}\n\n"
            
            for single_date in pd.date_range(start_date, end_date):
                date_str = single_date.strftime('%Y-%m-%d')
                if date_str in st.session_state.taken_medicines:
                    taken = len(st.session_state.taken_medicines[date_str])
                    report_data += f"{date_str}: {taken} medicines taken\n"
            
            st.download_button("💾 Download Report", 
                             report_data, 
                             f"medtimer_report_{start_date}_{end_date}.txt",
                             use_container_width=True)
            
            st.markdown("---")
            if st.button("✕ Close", use_container_width=True):
                st.session_state.show_report = False
                st.rerun()
    
    # Progress
    st.markdown("<h2 style='text-align: center;'>📊 Today's Progress</h2>", unsafe_allow_html=True)
    
    adherence = calculate_adherence()
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        progress_html = create_circular_progress(adherence)
        st.markdown(progress_html, unsafe_allow_html=True)
        
        st.markdown("<h3 style='text-align: center; margin-top: 20px;'>💬 Motivation</h3>", unsafe_allow_html=True)
        st.info(get_motivational_quote(adherence))
    
    st.markdown("---")
    
    # Medicines
    st.markdown("<h2>📋 Today's Medicines</h2>", unsafe_allow_html=True)
    
    today_meds = [(m, get_medicine_status(m, m['time'])) for m in st.session_state.medicines]
    today_meds = [(m, s) for m, s in today_meds if s != 'not-today']
    
    if not today_meds:
        st.info("No medicines for today!")
    else:
        for med, status in today_meds:
            icon = "🟢" if status == "taken" else "🟡" if status == "upcoming" else "🔴"
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.markdown(f"""
                <div class='medicine-card {status}'>
                    <h3>{icon} {med['name']} ({med['time'].strftime('%H:%M')})</h3>
                    <p>💊 {med['dose']} | ⏰ {med['time'].strftime('%H:%M')}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if status != 'taken':
                    if st.button("✓", key=f"take_{med['name']}_{med['time']}"):
                        mark_as_taken(med, med['time'])
                else:
                    st.success("✓")
    
    st.markdown("---")
    
    # Badges
    st.markdown("<h2 style='text-align: center;'>🏆 Achievements</h2>", unsafe_allow_html=True)
    
    badges = []
    if adherence >= 100:
        badges.append(("🏆 Perfect Day Master!", "gold"))
    elif adherence >= 80:
        badges.append(("🥈 Great Adherence!", "silver"))
    elif adherence >= 50:
        badges.append(("🥉 Halfway Hero!", "bronze"))
    
    if streak >= 30:
        badges.append(("🔥 30-Day Legend!", "gold"))
    elif streak >= 14:
        badges.append(("⚡ 2-Week Warrior!", "silver"))
    elif streak >= 7:
        badges.append(("🌟 Week Champion!", "bronze"))
    elif streak >= 3:
        badges.append(("💫 3-Day Starter!", "silver"))
    
    total_taken = sum(len(v) for v in st.session_state.taken_medicines.values())
    if total_taken >= 100:
        badges.append(("💯 Century Club!", "gold"))
    elif total_taken >= 50:
        badges.append(("🎯 Half Century!", "silver"))
    elif total_taken >= 10:
        badges.append(("🌱 Getting Started!", "bronze"))
    
    if badges:
        cols = st.columns(min(len(badges), 3))
        for i, (text, type_) in enumerate(badges):
            with cols[i % 3]:
                st.markdown(f"<div style='text-align: center;'><div class='badge badge-{type_}'>{text}</div></div>", unsafe_allow_html=True)
    else:
        st.info("🎁 Complete your medicines to unlock amazing badges and achievements!")
    
    st.markdown("---")
    if st.button("🔄 Reset & Update", use_container_width=True):
        st.session_state.current_page = 'confirmation'
        st.rerun()

# Main
def main():
    if st.session_state.current_page == 'welcome':
        show_welcome_page()
    elif st.session_state.current_page == 'login':
        show_login_page()
    elif st.session_state.current_page == 'add_medicine':
        show_add_medicine_page()
    elif st.session_state.current_page == 'confirmation':
        show_confirmation_page()
    elif st.session_state.current_page == 'main_app':
        show_main_app()

if __name__ == "__main__":
    main()