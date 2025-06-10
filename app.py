import streamlit as st
import base64

# Encode the background image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Replace 'Untitled design.png' with the correct path if it's not in the same directory
bg_image = get_base64_image("Untitled design.png")

# PAGE CONFIG
st.set_page_config(page_title="Tanmay Dhar | Portfolio", page_icon="🎓", layout="wide")

# --- CUSTOM CSS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('data:image/png;base64,{bg_image}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #FFFFFF;
    }}
    [data-testid="stSidebar"] {{
        background-color: rgba(26, 60, 94, 0.5); /* 50% transparent based on #1A3C5E */
    }}
    [data-testid="stSidebar"] * {{
        color: #FFFFFF !important;
    }}
    [data-testid="stSidebar"] h2 {{
        font-size: 28px !important;
    }}
    [data-testid="stSidebar"] a {{
        color: #E0F7FA !important;
        text-decoration: none;
    }}
    [data-testid="stSidebar"] a:hover {{
        color: #B2EBF2 !important;
        text-decoration: underline;
    }}
    [data-testid="stSidebar"] a[href*="data:application/pdf"] {{
        background-color: #4A90E2;
        padding: 8px 16px;
        border-radius: 5px;
        color: #FFFFFF !important;
        font-weight: bold;
        display: inline-block;
        margin-top: 20px;
    }}
    [data-testid="stSidebar"] a[href*="data:application/pdf"]:hover {{
        background-color: #2E6DA4;
        text-decoration: none;
    }}
    .social-icons {{
        display: flex;
        align-items: center;
        gap: 20px;
        margin-top: 10px;
    }}
    .social-icons a {{
        display: flex;
        align-items: center;
        gap: 6px;
        font-weight: bold;
        color: #FFFFFF !important;
    }}
    .social-icons img {{
        width: 24px;
        height: 24px;
    }}
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {{
        background-color: transparent;
        border-bottom: 2px solid #4A90E2;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: #FFFFFF;
        background-color: transparent;
        padding: 10px 20px;
        margin-right: 5px;
        border-radius: 8px 8px 0 0;
    }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background-color: #2E6DA4; /* Deep blue for active tab */
        color: #FFFFFF;
        font-weight: bold;
    }}

    /* Content area */
    .stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown a {{
        color: #FFFFFF; /* White text for all content */
    }}
    h1, h2, h3, h4 {{
        color: #FFFFFF; /* White headers */
    }}

    /* Main content links */
    a {{
        color: #FFFFFF; /* White for links */
        text-decoration: none;
    }}
    a:hover {{
        color: #E0F7FA; /* Light cyan on hover for contrast */
        text-decoration: underline;
    }}

    /* Button for resume download in main content (if any) */
    .stMarkdown a[href*="data:application/pdf"] {{
        background-color: #4A90E2; /* Vibrant blue button */
        padding: 8px 16px;
        border-radius: 5px;
        color: #FFFFFF;
        font-weight: bold;
    }}
    .stMarkdown a[href*="data:application/pdf"]:hover {{
        background-color: #2E6DA4; /* Darker blue on hover */
        text-decoration: none;
    }}

    /* Pill styling for skills */
    .skills-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }}
    .skill-pill {{
        background-color: #D1E8F2; /* Light blue pill background */
        color: #1A3C5E; /* Dark blue text for readability */
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 14px;
        display: inline-block;
        margin: 3px;
    }}

    /* Certification highlight */
    .cert-highlight {{
        background-color: #FFFFFF;
        color: #000000; /* Black text for contrast */
        padding: 2px 6px;
        border-radius: 3px;
        display: inline;
    }}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("Tanmay_Dhar_optimized.jpg")
    st.title("Tanmay Dhar")
    st.markdown("**Data Analyst | Business Analyst | Data Science Enthusiast**")
    st.markdown("📍 Kolkata, India")

    st.markdown("---")
    st.subheader("Contacts:")
    st.markdown("tanmaydhar36@gmail.com")
    st.markdown("+91 6290255794")

    # Social Links with Icons
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/tanmay-dhar-business-analyst-data-scientist-data-analyst" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"> LinkedIn
        </a>
        <a href="https://github.com/TanmayDhar36" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"> GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Download Resume Button
    with open("TanmayDharCV.pdf", "rb") as f:
        pdf = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(
            f'<a href="data:application/pdf;base64,{pdf}" download="Tanmay_Dhar_Resume.pdf">📄 Download Resume</a>',
            unsafe_allow_html=True)

# --- MAIN SECTION ---
st.title("🎓 Tanmay Dhar's Portfolio")
st.markdown(
    "Welcome to my professional portfolio showcasing my work, skills, and experience in **Business Analytics and Data Science**.")

# --- TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Experience", "Education", "Skills & Tools", "Certifications", "Projects"])

# Experience Tab
with tab1:
    st.subheader("Experience")
    st.markdown("""
    **AI Intern – StarApp Solution (Bengaluru, India)**  
    *May 2024 – Present*  
    - Worked with Flask and Django to develop and deploy AI-powered web applications.  
    - Contributed to building intelligent systems by leveraging backend development and AI model integration.
    - Collaborated with cross-functional teams to enhance product scalability and automation. 
    
    **Data Analyst Intern – Afame Technologies (Remote)**  
    *Apr 2024 – Jun 2024*  
    - Built interactive Tableau dashboards  
    - Delivered insights for sales and HR teams
    - [*View Certificate*](https://drive.google.com/file/d/1a2S1fNxoKLonjdkRecfFHMTo-QdU1b--/view)

    **Data Analyst Intern – Abhyaz-MTAB (Remote)**  
    *Jan 2024 – Mar 2024*  
    - Cleaned & visualized datasets  
    - Helped optimize decision-making
    - [*View Certificate*](https://drive.google.com/file/d/1pefF0znffT1BKM70ezj7gAZCBOUG3C3R/view)

    **Production Engineer – Landis Gyr Ltd (Kolkata, India)**  
    *Oct 2019 – Apr 2023*  
    - Oversaw production operations
    """)

# Education Tab
with tab2:
    st.subheader("Education")
    st.markdown("""
    **Bengal Institute Of Business Studies (BIBS)**  
    MBA + PGP Business Analytics & Data Science, *2024 – Present*, 86% (PGP Sem 1)

    **Gargi Memorial Institute Of Technology**  
    B.Tech in Electronics & Communication Engineering, *2020 – 2023*, 82%

    **Jnan Chandra Ghosh Polytechnic**  
    Diploma in Electronics & Tele-Communication Engineering, *2016 – 2019*, 74%
    """)

# Skills Tab
with tab3:
    st.subheader("Skills & Tools")
    st.markdown("""
    <div>
        <strong>Programming Language:</strong>
        <div class="skills-container">
            <span class="skill-pill">Python</span>
            <span class="skill-pill">SQL</span>
        </div>
        <strong>Databases:</strong>
        <div class="skills-container">
            <span class="skill-pill">MySQL</span>
            <span class="skill-pill">PostgreSQL</span>
        </div>
        <strong>Tools:</strong>
        <div class="skills-container">
            <span class="skill-pill">Tableau</span>
            <span class="skill-pill">Power BI</span>
            <span class="skill-pill">Excel</span>
            <span class="skill-pill">MS Office</span>
            <span class="skill-pill">Zoho Analytics</span>
            <span class="skill-pill">Zoho CRM</span>
        </div>
        <strong>General Skills:</strong>
        <div class="skills-container">
            <span class="skill-pill">Data Manipulation</span>
            <span class="skill-pill">Data Visualization</span>
            <span class="skill-pill">Machine Learning</span>
            <span class="skill-pill">Statistical Analysis</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Certifications Tab
with tab4:
    st.subheader("Certifications")
    st.markdown("""
    - <span class="cert-highlight">Full Stack Data Science Program</span> *(Jul–Dec 2023)* [View Certificate](https://verified.sertifier.com/en/verify/95034435667164/) 
    - <span class="cert-highlight">Machine Learning with Python – IIT Kanpur</span> *(Dec 2024)* [View Certificate](https://verify.eicta.digitalcredentials.in/fa37245d-31b3-46d4-a09b-ff55b476fcd1?utm_source=direct_link&utm_medium=portal)  
    - [🗂️ View All](https://drive.google.com/drive/folders/1DABdoTV6QMZd0nt0D5vj3HiHhNzExNn6?usp=drive_link)
    """, unsafe_allow_html=True)

# Projects Tab
with tab5:
    st.subheader("Projects")
    project_data = [
        {
            "title": "Play Store App Review Analysis",
            "desc": "EDA on app reviews using Python",
            "link": "https://github.com/TanmayDhar36/Google_Play_Store_App_Review_Analysis"
        },
        {
            "title": "Play Store Dashboard (Tableau)",
            "desc": "Dashboard to explore user feedback",
            "link": "https://github.com/TanmayDhar36/Transfer-EDA-To-Dashboard"
        },
        {
            "title": "ML Case Study – Water Quality",
            "desc": "Built ML model to predict water potability",
            "link": "https://github.com/TanmayDhar36/ML-Case-Study-on-Water-Quality-Analysis"
        },
        {
            "title": "Bike Sharing Demand Prediction",
            "desc": "Regression model for demand forecasting",
            "link": "https://github.com/TanmayDhar36/ML_Bike_Sharing_Demand_Prediction_Regression_Project"
        },
    ]
    for i, p in enumerate(project_data, 1):
        st.markdown(f"""
        **{i}. [{p['title']}]({p['link']})**  
        *{p['desc']}*
        """)
