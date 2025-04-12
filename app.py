import streamlit as st
import base64

# PAGE CONFIG
st.set_page_config(page_title="Tanmay Dhar | Portfolio", page_icon="🎓", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #E6F3FA; /* Light blue background */
        color: #1A3C5E; /* Dark blue text for contrast */
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1A3C5E; /* Dark blue for sidebar */
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important; /* White for all sidebar text */
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important; /* White for sidebar headers */
    }
    /* Increase Contact subheader size */
    [data-testid="stSidebar"] h2 {
        font-size: 28px !important; /* Larger font size for Contact */
    }
    /* Sidebar links */
    [data-testid="stSidebar"] a {
        color: #E0F7FA !important; /* Light cyan for sidebar links */
        text-decoration: none;
    }
    [data-testid="stSidebar"] a:hover {
        color: #B2EBF2 !important; /* Slightly darker cyan on hover */
        text-decoration: underline;
    }
    /* Sidebar resume button */
    [data-testid="stSidebar"] a[href*="data:application/pdf"] {
        background-color: #4A90E2; /* Vibrant blue button */
        padding: 8px 16px;
        border-radius: 5px;
        color: #FFFFFF !important; /* White text for button */
        font-weight: bold;
    }
    [data-testid="stSidebar"] a[href*="data:application/pdf"]:hover {
        background-color: #2E6DA4; /* Darker blue on hover */
        text-decoration: none;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #D1E8F2;
        border-bottom: 2px solid #4A90E2; /* Vibrant blue for tab border */
    }
    .stTabs [data-baseweb="tab"] {
        color: #1A3C5E;
        background-color: #E6F3FA;
        padding: 10px 20px;
        margin-right: 5px;
        border-radius: 8px 8px 0 0;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #4A90E2; /* Vibrant blue for active tab */
        color: #FFFFFF; /* White text for active tab */
        font-weight: bold;
    }

    /* Content area */
    .stMarkdown, .stMarkdown p, .stMarkdown li {
        color: #1A3C5E; /* Dark blue text for content */
    }
    h1, h2, h3, h4 {
        color: #2E6DA4; /* Medium blue for headers */
    }

    /* Main content links */
    a {
        color: #D81B60; /* Pink for links to stand out */
        text-decoration: none;
    }
    a:hover {
        color: #F06292; /* Lighter pink on hover */
        text-decoration: underline;
    }

    /* Button for resume download in main content (if any) */
    .stMarkdown a[href*="data:application/pdf"] {
        background-color: #4A90E2; /* Vibrant blue button */
        padding: 8px 16px;
        border-radius: 5px;
        color: #FFFFFF;
        font-weight: bold;
    }
    .stMarkdown a[href*="data:application/pdf"]:hover {
        background-color: #2E6DA4; /* Darker blue on hover */
        text-decoration: none;
    }

    /* Pill styling for skills */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }
    .skill-pill {
        background-color: #D1E8F2; /* Light blue pill background */
        color: #1A3C5E; /* Dark blue text */
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 14px;
        display: inline-block;
        margin: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("Tanmay Dhar.JPG")
    st.title("Tanmay Dhar")
    st.markdown("**Data Analyst | Business Analyst | Data Science Enthusiast**")
    st.markdown("📍 Kolkata, India")

    st.markdown("---")
    st.subheader("Contacts:")
    st.markdown("tanmaydhar24-26@bibs.co.in")
    st.markdown("+91 6290255794")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/tanmay-dhar-business-analyst-data-scientist-data-analyst)")
    st.markdown("[GitHub](https://github.com/TanmayDhar36)")

    with open("Tanmay_Dhar.pdf", "rb") as f:
        pdf = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(f'<a href="data:application/pdf;base64,{pdf}" download="Tanmay_Dhar_Resume.pdf">📄 Download Resume</a>', unsafe_allow_html=True)

# --- MAIN SECTION ---
st.title("🎓 Tanmay Dhar's Portfolio")
st.markdown("Welcome to my professional portfolio showcasing my work, skills, and experience in **Business Analytics and Data Science**.")

# --- TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["💼 Experience", "🎓 Education", "🧠 Skills & Tools", "📜 Certifications", "📁 Projects"])

# Experience Tab
with tab1:
    st.subheader("💼 Experience")
    st.markdown("""
    **Data Analyst Intern – Afame Technologies (Remote)**  
    *Apr 2024 – Jun 2024*  
    - Built interactive Tableau dashboards  
    - Delivered insights for sales and HR teams
    
    [*Certificate*](https://drive.google.com/file/d/1a2S1fNxoKLonjdkRecfFHMTo-QdU1b--/view)

    **Data Analyst Intern – Abhyaz-MTAB (Remote)**  
    *Jan 2024 – Mar 2024*  
    - Cleaned & visualized datasets  
    - Helped optimize decision-making
    
    [*Certificate*](https://drive.google.com/file/d/1pefF0znffT1BKM70ezj7gAZCBOUG3C3R/view)

    **Production Engineer – Landis Gyr Ltd (Kolkata)**  
    *Oct 2019 – Apr 2023*  
    - Oversaw production operations
    """)

# Education Tab
with tab2:
    st.subheader("🎓 Education")
    st.markdown("""
    **MBA + PGPBA&DS – BIBS**  
    *2024 – Present*  
    - 86% in Sem 1  

    **B.Tech – Electronics & Communication**  
    Gargi Memorial Institute, *2020 – 2023*  
    - 82%

    **Diploma – E&TC**  
    JCG Polytechnic, *2016 – 2019*  
    - 74%
    """)

# Skills Tab
with tab3:
    st.subheader("🧠 Skills & Tools")
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
    st.subheader("📜 Certifications")
    st.markdown("""
    - [Full Stack Data Science Program *(Jul–Dec 2023)*](https://verified.sertifier.com/en/verify/95034435667164/) 
    - [Machine Learning with Python – IIT Kanpur *(Dec 2024)*](https://verify.eicta.digitalcredentials.in/fa37245d-31b3-46d4-a09b-ff55b476fcd1?utm_source=direct_link&utm_medium=portal)  
    - [🗂️ View All](https://drive.google.com/drive/folders/1DABdoTV6QMZd0nt0D5vj3HiHhNzExNn6?usp=drive_link)
    """)

# Projects Tab
with tab5:
    st.subheader("📁 Projects")
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
    for p in project_data:
        st.markdown(f"""
        **[{p['title']}]({p['link']})**  
        *{p['desc']}*
        """)
