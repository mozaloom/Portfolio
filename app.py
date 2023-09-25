from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Mohammed Zaloom"
PAGE_ICON = current_dir / "assets" / "profile-pic (19).png"
NAME = "Mohammed Zaloom"
DESCRIPTION = """
Artificial Intelligence and Robotics student at Al- Balqa' Applied University (BAU), passion for learning. I aim to keep learning and become a better version of myself every day.
"""
EMAIL = "mohammedzaloomai@gmail.com"
SOCIAL_MEDIA = {

    "LinkedIn": "https://www.linkedin.com/in/mozaloom/",
    "GitHub": "https://github.com/mozaloom",
    "X": "https://twitter.com/mozaloom",
    "Kaggle":"https://www.kaggle.com/mohammedzaloom",
}
PROJECTS = {
    " Duality in Optimization": "https://drive.google.com/file/d/1MpGN4Uv2_pqylcYAx2myOGCIQivDJDRv/view",

}
CERITIFICATIONS = {
    "   Thingworkx Platform Hands-on Training": "https://drive.google.com/file/d/1sKUghtP3XCZJr6SFPYktOrrYN52B_0t2/view?usp=sharing",
    "   Introduction to the Internet of Things and Embedded Systems" :"https://www.coursera.org/account/accomplishments/certificate/LLQHGR9TRP2M",
    "   The Arduino Platform and C Programming" :"https://www.coursera.org/account/accomplishments/certificate/ZDXA96NU4HJA",
    "   Introduction to Embedded Systems Software and Development Environments" :"https://www.coursera.org/account/accomplishments/certificate/H5YMCRC3ESX4",
    "   MATLAB Onramp" :"https://matlabacademy.mathworks.com/progress/share/certificate.html?id=4cb61c4b-8e29-450b-a51c-3632cf5b332e&",
    "   Neural Networks and Deep Learning" :"https://www.coursera.org/account/accomplishments/certificate/D8YKHJV4HPQE",
    "   Artificial Neural Networks (ANN) with Keras in python and R" :"https://www.udemy.com/certificate/UC-556da70e-923b-4e95-8b71-72a42613bed9/",
    "   Convolutional Neural Networks" :"https://www.coursera.org/account/accomplishments/certificate/MGR4CKG5RWZZ",
    "   NLP Course for Beginner" :"https://www.udemy.com/certificate/UC-fb17dd37-be94-41fa-a4e7-6a56173ab94f/",
    "   Structuring Machine Learning Projects" :"https://www.coursera.org/account/accomplishments/certificate/GHKYJACQ7ML4",
    "   Aerial Robotics" : "https://www.coursera.org/account/accomplishments/certificate/2QALABRA9SBT",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("🙋‍ About me")
st.write(
    """
As a student in AI and Robotics at Balqa Applied University in Jordan, I am passionate about using modern technology like robotics, machine learning, and NLP to make a positive impact in the world. I've took many certificates in courses that related to my major. I am also a productive person who can work efficient, I aim to keep learning and become a better version of myself every day.
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("🎓 Education")
st.write("---")

# --- JOB 1
st.write( "**Al- Balqa' Applied University (BAU) 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 | 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 󠁪󠁪 2021 - 2025**")
st.write("")
st.write(
    """
          🧠 Majoring in AI and Robotics 󠁪󠁪 󠁪󠁪 󠁪󠁪 - 󠁪󠁪 󠁪󠁪 󠁪󠁪 GPA: 󠁪󠁪 3.77 / 4.0
"""
)
# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
1. Robotics (Arduino, Planning, Raspberry Pi, Vision Robot, Sensors)
2. Programming: Python (Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Tensorflow)
3. Mathematics for Machine Learning: Linear Algebra, Multivariate Calculus, Probability, Statistics
4. Machine Learning: Supervised Learning, Unsupervised Learning, Reinforcement Learning
5. Deep Learning: Convolutional Neural Networks, Recurrent Neural Networks
6. Computer Vision: Image Processing, Object Detection, Image Recognition
7. Natural Language Processing: Text Processing, Text Classification
8. TensorFlow: Keras, Tensorflow Hub, Tensorflow Datasets

"""
)
# --- SKILLS ---
st.write('\n')
st.subheader("Soft Skills")
st.write("---")
st.write(
    """
1. Communication
2. Teamwork
3. Leadership
4. Time Management
5. Creativity

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Experience 🧑‍💻")
st.write("---")
st.write(
    """ 
    Undergraduate student.
    """
    )
    
st.write('\n')
st.subheader("Certifications 🎖️")
st.write("---")
for project, link in CERITIFICATIONS.items():
    st.write(f"[{project}]({link})")

st.write('\n')
st.subheader("Volunteering 🤝")
st.write("---")
st.write(
    """ 
            1. Police friends – PSD 2019
            2. Anausharek – CPF 2022
    """
    )
