import streamlit as st
from PIL import Image

# --- Sidebar ---
image = Image.open("Tanmay Dhar.JPG")
st.sidebar.image(image)
st.sidebar.title("Tanmay Dhar")
st.sidebar.markdown("**Data Analyst | Business Analyst | Data Scientist**")
st.sidebar.markdown("📍 Kolkata, India")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/tanmay-dhar-business-analyst-data-scientist-data-analyst)")
st.sidebar.markdown("[GitHub](https://github.com/TanmayDhar36)")
st.sidebar.markdown("📧 tanmaydhar24-26@bibs.co.in")
st.sidebar.markdown("📞 +91 6290255794")

# --- Main Area ---
st.title("Tanmay Dhar")
st.subheader("Business Analytics & Data Science | MBA @ BIBS")
st.markdown("""
A passionate **Data Enthusiast** with experience in **data analysis**, **machine learning**, and **data visualization**. 
Currently pursuing an MBA in Business Analytics & Data Science. Always eager to learn and grow in the field of data.
""")

st.header("💼 Work Experience")
st.markdown("""
**Data Analyst Intern @ Afame Technologies (Remote)**  
_04/2024 - 06/2024_  
- Built Tableau dashboards to uncover business insights.  
- Aided Sales & HR in strategic decision-making.

**Data Analyst Intern @ Abhyaz-MTAB (Remote)**  
_01/2024 - 03/2024_  
- Cleaned and organized datasets.  
- Collaborated with Sales & HR to derive insights.  

**Production Engineer @ Landis Gyr Ltd**  
_10/2019 - 04/2023 (Kolkata)_  
- Hands-on production engineering experience.
""")

st.header("📊 Projects")
st.markdown("""
- [Google Play Store App Review Analysis - EDA](https://github.com/TanmayDhar36/Google_Play_Store_App_Review_Analysis)  
- [Google Play Store Dashboard using Tableau](https://github.com/TanmayDhar36/Transfer-EDA-To-Dashboard)  
- [ML Case Study - Water Quality Analysis](https://github.com/TanmayDhar36/ML-Case-Study-on-Water-Quality-Analysis)  
- [Regression Project - Bike Sharing Demand](https://github.com/TanmayDhar36/ML_Bike_Sharing_Demand_Prediction_Regression_Project)
""")

st.header("🎓 Education")
st.markdown("""
**MBA + PGPBA&DS** - Bengal Institute of Business Studies (08/2024 - Present)  
_86% in Semester 1_

**B.Tech - Electronics & Communication** - Gargi Memorial Institute (08/2020 - 07/2023)  
_82%_

**Diploma - Electronics & Telecommunication** - JCG Polytechnic (08/2016 - 07/2019)  
_74%_
""")

st.header("🛠️ Skills & Tools")
st.markdown("""
- **Languages:** Python, SQL  
- **Databases:** MySQL, PostgreSQL  
- **Tools:** Tableau, Power BI, Excel, MS Office, Zoho Analytics, Zoho CRM  
- **Concepts:** Data Visualization, Machine Learning, Data Manipulation, Statistical Analysis
""")

st.header("📜 Certifications")
st.markdown("""
- **Full Stack Data Science Program** (Jul 2023 - Dec 2023)  
- **Machine Learning with Python - IIT Kanpur** (Dec 2024)  
- [View All Certifications](https://drive.google.com/drive/folders/1DABdoTV6QMZd0nt0D5vj3HiHhNzExNn6?usp=drive_link)
""")
