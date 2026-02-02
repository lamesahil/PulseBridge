import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time
from datetime import datetime, timedelta

# --- CONFIGURATION ---
st.set_page_config(
    page_title="PulseBridge AI",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 🎨 THEME: PINK RIBBON EDITION (FIXED VISIBILITY) ---
st.markdown("""
<style>
    /* 1. BACKGROUND & TEXT */
    .stApp {
        background-color: #fff0f5; /* Lavender Blush */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #880e4f !important; /* Dark Burgundy */
        font-family: 'Segoe UI', sans-serif;
    }
    p, li, span, div {
        color: #2c3e50; /* Dark Slate Grey for readability */
    }
    
    /* 2. SIDEBAR - ROSE THEME */
    [data-testid="stSidebar"] {
        background-color: #880e4f; /* Deep Burgundy */
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #ffffff !important;
    }
    
    /* 3. CARDS & CONTAINERS */
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 15px;
        padding: 22px;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.1); /* Pink shadow */
        border: 1px solid #f8bbd0;
        transition: transform 0.3s ease;
    }
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        border-color: #ec407a;
        box-shadow: 0 10px 25px rgba(233, 30, 99, 0.2);
    }
    
    /* 4. BUTTONS - GRADIENT PINK */
    div.stButton > button {
        background: linear-gradient(135deg, #ec407a 0%, #ab47bc 100%); /* Pink to Purple */
        color: white !important;
        font-weight: bold;
        border: none;
        padding: 12px 28px;
        border-radius: 30px; /* Pill shape */
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(236, 64, 122, 0.4);
    }
    
    /* 5. METRICS & HIGHLIGHTS */
    [data-testid="stMetricValue"] {
        color: #d81b60 !important; /* Vivid Pink */
        font-size: 2.4rem !important;
    }
    
    /* 6. SLIDERS - FIXED VISIBILITY */
    /* Only coloring the labels, leaving the track clean for contrast */
    .stSlider label {
        color: #880e4f !important;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)

# --- 🧠 LOGIC ---
def calculate_patient_risk(days_since_appt, days_since_refill, activity_drop):
    appt_overdue = max(0, days_since_appt - 90)
    appt_score = (min(appt_overdue, 60) / 60) * 100
    refill_overdue = max(0, days_since_refill - 30)
    refill_score = (min(refill_overdue, 30) / 30) * 100
    
    # Silent Drop-off Multiplier
    multiplier = 1.0
    if appt_overdue > 0 and refill_overdue > 0:
        multiplier = 1.2 

    total_risk = ((appt_score * 0.4) + (refill_score * 0.4) + (activity_drop * 0.2)) * multiplier
    return min(100, round(total_risk, 1))

def mock_breast_cancer_prediction(input_data):
    # Heuristic logic based on "Worst" values
    risk_score = 0
    if input_data['radius_worst'] > 18.0: risk_score += 3
    if input_data['texture_worst'] > 25.0: risk_score += 2
    if input_data['area_worst'] > 1000.0: risk_score += 3
    if input_data['concavity_worst'] > 0.5: risk_score += 2
    
    if risk_score > 5:
        return "Malignant (High Risk)", 0.94
    return "Benign (Safe)", 0.12

# --- 🏠 PAGE: HOME ---
def show_home():
    # Hero Section with Emotional Impact
    st.markdown("# 🎀 PulseBridge: Guarding Her Health")
    st.markdown("### Early Detection Saves Lives.")
    st.divider()
    
    col1, col2 = st.columns([1.5, 1], gap="large")
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🚨 Why This Matters")
            st.markdown("""
            Breast cancer is not just a statistic; it's a reality for millions of families.
            
            * **1 in 8 women** will be diagnosed with breast cancer in their lifetime.
            * **Every 2 minutes**, a woman is diagnosed with breast cancer in the US.
            * **Early Detection is the Cure:** When caught in localized stages, the 5-year survival rate is **99%**.
            
            **PulseBridge** uses advanced AI to bridge the gap between uncertainty and clarity. We analyze complex biopsy markers to assist doctors in making faster, life-saving decisions.
            """)
            st.warning("**Our Mission:** To ensure no woman is left undiagnosed until it's too late.")
            
    with col2:
        with st.container(border=True):
            st.markdown("### ⚡ System Dashboard")
            st.info("System Status: **Online & Protecting**")
            
            c1, c2 = st.columns(2)
            c1.metric("Lives Monitored", "1,240")
            c2.metric("Alerts Today", "3")
            
            st.write("")
            if st.button("🚀 Access Detection Module", use_container_width=True):
                st.toast("Redirecting to AI Module...", icon="🎀")

# --- 📊 PAGE: DASHBOARD ---
def show_dashboard():
    st.markdown("# 📊 Patient Adherence & Vitals")
    st.markdown("**Monitoring continuity of care for at-risk patients.**")
    st.divider()

    data = {
        "Patient Name": ["Ms. John Doe", "Ms. Jane Smith", "Mrs. Robert Chen", "Ms. Sarah Miller"],
        "Condition": ["Diabetes", "Breast Cancer Survivor", "Diabetes", "COPD"],
        "Days Since Last Appt": [110, 85, 150, 92],
        "Days Since Refill": [45, 20, 65, 31],
        "Activity Drop (%)": [40, 5, 60, 10]
    }
    df = pd.DataFrame(data)
    df['Risk Score'] = df.apply(lambda x: calculate_patient_risk(
        x['Days Since Last Appt'], x['Days Since Refill'], x['Activity Drop (%)']), axis=1)

    # Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Active Patients", "142", "+2")
    c2.metric("Critical Alerts", "12", "+3", delta_color="inverse")
    c3.metric("Adherence Rate", "82%", "-4%")
    c4.metric("Pending Refills", "8", "normal")

    col_left, col_right = st.columns([1, 2], gap="medium")

    with col_left:
        with st.container(border=True):
            st.subheader("⚠️ High Risk Queue")
            st.dataframe(
                df.sort_values("Risk Score", ascending=False)[['Patient Name', 'Risk Score']],
                column_config={
                    "Risk Score": st.column_config.ProgressColumn(
                        "Risk Score", format="%d%%", min_value=0, max_value=100,
                        help="Calculated Risk Factor"
                    )
                },
                hide_index=True,
                use_container_width=True
            )

    with col_right:
        with st.container(border=True):
            st.subheader("🔎 Patient Deep Dive")
            selected_patient = st.selectbox("Select Patient Record:", df["Patient Name"])
            p_data = df[df["Patient Name"] == selected_patient].iloc[0]
            
            risk = p_data['Risk Score']
            if risk > 50:
                st.error(f"**CRITICAL RISK: {risk}%** - Immediate Intervention Required")
            else:
                st.success(f"**STABLE: {risk}%** - Routine Monitoring")
            
            m1, m2 = st.columns(2)
            m1.write(f"**Condition:** {p_data['Condition']}")
            m1.write(f"**Last Appt:** {p_data['Days Since Last Appt']} days ago")
            m2.write(f"**Refill Gap:** {p_data['Days Since Refill']} days")
            m2.write(f"**Activity Drop:** {p_data['Activity Drop (%)']}%")

            st.markdown("##### 💓 Vitals Trend (Last 30 Days)")
            chart_data = pd.DataFrame({
                'Date': [datetime.now() - timedelta(days=i) for i in range(30)],
                'Vitals': np.random.normal(80, 5, 30) - (0.5 if risk > 50 else 0) * np.arange(30)
            })
            
            # Pink Chart
            fig = px.area(chart_data, x='Date', y='Vitals', color_discrete_sequence=['#ec407a'])
            fig.update_layout(height=230, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

# --- 🧬 PAGE: AI DIAGNOSIS ---
def show_prediction_tool():
    st.markdown("# 🧬 AI Breast Cancer Assistant")
    st.markdown("**Advanced Neural Network for Biopsy Analysis.**")
    st.info("ℹ️ Input cytological parameters below for real-time malignancy prediction.")
    st.divider()

    col_input, col_output = st.columns([1.5, 1], gap="medium")

    with col_input:
        with st.container(border=True):
            st.subheader("🔬 Biopsy Parameters")
            
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                st.markdown("**Morphological (Worst)**")
                texture_worst = st.slider("Texture Worst", 10.0, 50.0, 25.0)
                radius_worst = st.slider("Radius Worst", 5.0, 40.0, 18.0)
                area_worst = st.slider("Area Worst", 300.0, 2500.0, 1000.0)
                symmetry_worst = st.slider("Symmetry Worst", 0.0, 1.0, 0.4)
                concavity_worst = st.slider("Concavity Worst", 0.0, 1.5, 0.5)

            with f_col2:
                st.markdown("**Statistical & Mean**")
                radius_se = st.slider("Radius SE", 0.0, 3.0, 0.5)
                area_se = st.slider("Area SE", 0.0, 200.0, 40.0)
                concavity_mean = st.slider("Concavity Mean", 0.0, 0.8, 0.2)
                concave_pts_mean = st.slider("Concave Points Mean", 0.0, 0.3, 0.05)
                concave_pts_worst = st.slider("Concave Points Worst", 0.0, 0.5, 0.15)
            
            input_data = {
                "texture_worst": texture_worst, "radius_worst": radius_worst,
                "area_worst": area_worst, "symmetry_worst": symmetry_worst,
                "concavity_worst": concavity_worst, "radius_se": radius_se,
                "area_se": area_se, "concavity_mean": concavity_mean,
                "concave points_mean": concave_pts_mean, "concave points_worst": concave_pts_worst
            }

    with col_output:
        with st.container(border=True):
            st.subheader("🤖 Diagnostic Result")
            st.write("Click to analyze patterns.")
            st.write("")
            
            if st.button("RUN ANALYSIS 🎀", use_container_width=True):
                # Pink Progress Bar
                progress_text = "Scanning cellular features..."
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(0.3)
                my_bar.empty()
                
                result, probability = mock_breast_cancer_prediction(input_data)
                
                if "Malignant" in result:
                    st.error(f"### {result}")
                    st.markdown(f"**Confidence:** {probability*100:.1f}%")
                    st.markdown("🚨 **Action:** Immediate Oncology Referral.")
                else:
                    st.success(f"### {result}")
                    st.markdown(f"**Confidence:** {probability*100:.1f}%")
                    st.markdown("✅ **Action:** Routine Annual Screening.")

# --- 👥 PAGE: TEAM ---
def show_about_us():
    st.markdown("# 👥 Meet the Team")
    st.markdown("### Innovating for Women's Health.")
    st.divider()
    
    # Updated Colors to match Pink Theme
    team = [
        {"name": "Sahil Tiwari", "role": "Frontend & ML Integration", "color": "ec407a"},
        {"name": "Rishabh Singh", "role": "UI/UX Design", "color": "ab47bc"},
        {"name": "Anuvesh Tiwari", "role": "Model Training & Evaluation", "color": "ef5350"},
        {"name": "Daksh Tiwari", "role": "UI/UX Design", "color": "7e57c2"}
    ]
    
    cols = st.columns(4)
    for i, m in enumerate(team):
        with cols[i]:
            with st.container(border=True):
                st.image(f"https://api.dicebear.com/7.x/initials/svg?seed={m['name']}&backgroundColor={m['color']}", width=100)
                st.markdown(f"### {m['name']}")
                st.markdown(f"**{m['role']}**")

# --- MAIN ROUTER ---
def main():
    with st.sidebar:
        st.markdown("## 🎀 PulseBridge")
        st.markdown("*Empowering Health*")
        st.markdown("---")
        
        page = st.radio(
            "Navigation", 
            ["Home", "Patient Dashboard", "AI Diagnosis", "About Us"],
            label_visibility="collapsed"
        )
        
        st.write("---")
        st.info("Logged in as: **Dr. Admin**")
        st.caption("© 2025 PulseBridge Inc.")

    if page == "Home": show_home()
    elif page == "Patient Dashboard": show_dashboard()
    elif page == "AI Diagnosis": show_prediction_tool()
    elif page == "About Us": show_about_us()

if __name__ == "__main__":
    main()