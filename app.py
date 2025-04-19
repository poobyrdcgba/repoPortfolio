import streamlit as st
import base64
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Robert David Cala | Portfolio",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #4169E1 !important;
    }
    .sub-header {
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        color: #1E3A8A !important;
    }
    .highlight {
        background-color: #F0F7FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4169E1;
    }
    .skill-badge {
        display: inline-block;
        background-color: #E0E7FF;
        color: #3B4FDB;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 15px;
        font-weight: 500;
    }
    .contact-box {
        background-color: #F3F4F6;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .project-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- PROFILE INFO ---
name = "Robert David Cala"
title = "Audio Technician & Aspiring Developer"
description = """
I was working student with experience in basic sound system setup and operation, along with a growing interest in software development.
Currently pursuing my computer science degree while gaining practical skills in both audio work and programming.
"""
email = "robertdavid.cala@cit.edu"
phone = "09631668797"
github = "https://github.com/poobyrdcgba"
streamlit_app = "https://robertfirstsl.streamlit.app/"
location = "Philippines"

# --- SKILLS ---
audio_skills = ["Basic Sound System Setup", "Mixer Operation", "Audio Cables & Connections", "Speaker Placement"]
tech_skills = ["Python", "JavaScript", "HTML/CSS", "Streamlit"]
tools = ["Basic Mixing Console", "Audio Equipment", "Git", "VS Code"]

# --- PROJECTS ---
projects = [
    {
        "title": "Sound System Setup",
        "description": "Set up and operated basic sound equipment for small events and gatherings.",
        "tech": ["PA System", "Basic Mixer", "Speakers"],
        "link": "#"
    },
    {
        "title": "Simple Audio Recording",
        "description": "Assisted with basic recording setups for small projects.",
        "tech": ["Basic Recording Equipment", "Microphone Setup"],
        "link": "#"
    },
    {
        "title": "Personal Portfolio Website",
        "description": "Developed this interactive portfolio using Streamlit to showcase my experience and projects.",
        "tech": ["Python", "Streamlit", "Web Design"],
        "github": "https://github.com/poobyrdcgba/portfolio"
    }
]

# --- EDUCATION ---
education = [
    {
        "degree": "Bachelor of Science in Computer Science",
        "institution": "Cebu Institute of Technology University",
        "duration": "2020 - Present"
    }
]

# --- EXPERIENCE ---
experiences = [
    {
        "position": "Sound System Assistant",
        "company": "Local Events",
        "duration": "2022 - Present",
        "description": "Set up basic sound equipment including speakers, microphones, and cables. Operate simple mixing consoles to adjust volume levels during events."
    },
    {
        "position": "Audio Helper",
        "company": "Community Events",
        "duration": "2021 - Present",
        "description": "Assist with connecting audio equipment and basic troubleshooting. Help with speaker placement and running cables for optimal sound."
    }
]

# Function to generate download link for resume
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}" class="download-button">Download {file_label}</a>'
    return href

# Function to send email
def send_email(name, email, message):
    sender_email = "rdcpooby@gmail.com"  # Replace with your email
    receiver_email = "rdcpooby@gmail.com"  # Replace with your email or recipient email
    password = "sheu kspg lrqq npxd"  # Replace with your Gmail app password
    
    subject = f"New Message from {name}"
    body = f"""
    You have received a new message from {name} ({email}):
    
    {message}
    """
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Setup the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# --- SIDEBAR ---
with st.sidebar:
    try:
        st.image("assets/profile.jpg", width=300)
    except:
        st.info("Profile image not found. Add your image as 'assets/profile.jpg'")

    st.markdown(f"# {name}")
    st.markdown(f"### {title}")
    
    st.markdown("---")
    st.markdown("### 📞 Contact Information")
    st.markdown(f"📧 **Email:** {email}")
    st.markdown(f"📱 **Phone:** {phone}")
    st.markdown(f"📍 **Location:** {location}")
    
    st.markdown("---")
    st.markdown("### 🔗 Links")
    st.markdown(f"[GitHub Profile]({github})")
    st.markdown(f"[Streamlit App]({streamlit_app})")
    
    try:
        resume_path = "assets/ResumeCHUCHU.pdf"
        st.markdown(get_binary_file_downloader_html(resume_path, 'Resume'), unsafe_allow_html=True)
    except:
        st.warning("Resume file not found. Add your resume to assets folder.")

# --- MAIN CONTENT ---
st.markdown('<p class="main-header">Welcome to My Portfolio</p>', unsafe_allow_html=True)

# About Me Section
st.markdown('<p class="sub-header">About Me</p>', unsafe_allow_html=True)
st.markdown(f'<div class="highlight">{description}</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<p class="sub-header">Skills</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Audio Skills")
    for skill in audio_skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

with col2:
    st.markdown("#### Technical Skills")
    for skill in tech_skills:
        st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

with col3:
    st.markdown("#### Tools & Equipment")
    for tool in tools:
        st.markdown(f'<span class="skill-badge">{tool}</span>', unsafe_allow_html=True)

# Experience Section
st.markdown('<p class="sub-header">Basic Experience</p>', unsafe_allow_html=True)
for exp in experiences:
    st.markdown(f"""
    #### {exp['position']} at {exp['company']}
    *{exp['duration']}*
    
    {exp['description']}
    """)
    st.markdown("---")

# Education Section
st.markdown('<p class="sub-header">Education</p>', unsafe_allow_html=True)
for edu in education:
    st.markdown(f"""
    #### {edu['degree']}
    **{edu['institution']}** | {edu['duration']}
    """)

# Development Interests Section
st.markdown('<p class="sub-header">Development Interests</p>', unsafe_allow_html=True)
st.write("""
As a computer science student, I'm developing skills in software development alongside my audio work.
I'm particularly interested in:
- Web application development
- Python programming
- Creating interactive user interfaces
- Learning about new technologies
""")

# --- CONTACT FORM SECTION ---
st.markdown('<p class="sub-header">Get In Touch</p>' , unsafe_allow_html=True) 
st.write("""
This is a simple email sender. This is working it's from my gmail to my gmail only. I can see your emails but in my end only.
""")

contact_form = st.form("contact_form")
name_input = contact_form.text_input("Name")
email_input = contact_form.text_input("Email")
message_input = contact_form.text_area("Message", height=150) 
submit = contact_form.form_submit_button("Send")

if submit: 
    if not re.match(r"[^@]+@[^@]+.[^@]+", email_input): st.error("Invalid email address.") 
    elif name_input and email_input and message_input: 
        if send_email(name_input, email_input, message_input): st.success("Your message has been sent successfully!") 
    else: st.error("There was an error sending your message. Please try again.")
    
else: st.warning("Please fill in all fields.")
