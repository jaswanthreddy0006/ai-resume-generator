import streamlit as st
from transformers import pipeline, set_seed

st.set_page_config(page_title="GenAI Resume Builder", layout="wide")
st.title("📄 AI Resume Generator (Clean, No AI Sections)")
st.markdown("Fill in your details below. Resume sections will appear exactly as entered, without extra AI text.")

# 📥 Form Inputs
with st.form("resume_form"):
    st.subheader("👤 Personal Info")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    location = st.text_input("Location (City, Country)")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

    st.subheader("🎯 Job Role & Skills")
    job_title = st.text_input("Job Title")
    skills = st.text_area("Skills (comma-separated)")

    st.subheader("🎓 Education")
    edu_degree = st.text_input("Degree (e.g., B.Tech in CSE)")
    edu_institute = st.text_input("University/College")
    edu_year = st.text_input("Graduation Year")
    edu_score = st.text_input("CGPA or Percentage")

    st.subheader("💼 Experience / Projects")
    experience = st.text_area("Describe your experience")

    st.subheader("🏅 Achievements / Certifications")
    achievements = st.text_area("Mention your achievements")

    st.subheader("🗣️ Languages & Extras")
    languages = st.text_input("Languages Known")
    hobbies = st.text_input("Hobbies or Interests")
    custom_section = st.text_area("Custom Section (Optional)")

    submitted = st.form_submit_button("Generate Resume")

# 🧾 Resume Output
if submitted:
    st.title("📝 Generated Resume")
    st.markdown(f"## {full_name}")
    st.markdown(f"**{job_title}**")
    st.markdown(f"📧 {email} | 📞 {phone} | 🌍 {location}")
    if linkedin:
        st.markdown(f"[LinkedIn]({linkedin})", unsafe_allow_html=True)
    if github:
        st.markdown(f"[GitHub]({github})", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("🛠️ Skills")
    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    st.success(", ".join(skill_list[:10]))

    st.subheader("💼 Experience / Projects")
    st.write(experience)

    st.subheader("🎓 Education")
    st.write(f"{edu_degree}, {edu_institute} ({edu_year}) — CGPA: {edu_score}")

    st.subheader("🏅 Achievements / Certifications")
    st.write(achievements)

    st.subheader("🗣️ Languages Known")
    st.text(languages)

    st.subheader("🎨 Hobbies & Interests")
    st.text(hobbies)

    if custom_section.strip():
        st.subheader("📌 Additional Section")
        st.text(custom_section)

    st.success("✅ Resume generated successfully! You can copy this output into Word or PDF.")
