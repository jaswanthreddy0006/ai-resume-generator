# 🎯 GenAI Resume Builder

An AI-powered resume builder that uses Generative AI (like GPT) to automatically create professional, well-structured resumes from user input. Built with Python and Gradio for a seamless and interactive experience.

---

## 🚀 Overview

The GenAI Resume Builder simplifies the resume creation process by guiding users through a set of fields (like name, education, skills, etc.), then using a language model to format and generate a polished, downloadable resume.

It offers real-time preview, customization, and one-click PDF export. Ideal for students, job seekers, and professionals.

---

## ✨ Key Features

### 🤖 AI-Powered Resume Writing
- Uses GPT or other LLMs to generate smart resume content
- Automatically formats input into proper resume sections
- Supports dynamic paragraph generation based on role

### 🧠 Context-Aware Content
- Understands and relates sections like skills to experience
- Generates job descriptions and summaries automatically

### 🎨 Interactive UI
- Gradio-based interface for fast data entry
- Real-time preview of resume content
- Fully responsive and mobile-friendly

### 📄 PDF Generation
- Resume content is rendered and exported as a clean PDF
- Option to re-edit and regenerate instantly

---

## 🧰 Tech Stack

| Layer          | Technology               |
|----------------|---------------------------|
| Language       | Python 3.10+              |
| UI Framework   | Gradio                    |
| AI Engine      | OpenAI API / Local GPT    |
| PDF Export     | ReportLab / xhtml2pdf     |
| Deployment     | HuggingFace / Streamlit Cloud |

---

## 🏗️ System Architecture

### 🧩 Architecture Diagram

![Flowchart](public/flowchart.png)

---

## 🔁 Sequence of Operations

1. User inputs personal info (name, education, etc.)
2. Data is sent to LLM for formatting
3. Model returns structured resume text
4. Resume is displayed and downloadable as PDF

### 📄 Sequence Diagram

![Sequence Diagram](public/sequence.png)

---

## 🎯 How It Works

### Basic Flow:
```text
User Input ➜ Processed by LLM ➜ Output Resume Text ➜ Generate PDF ➜ Download
Example JSON Input:
resume_data = {
  "name": "Jaswanth Reddy",
  "education": "B.Tech in CSE",
  "skills": ["Python", "Machine Learning", "AI"],
  "experience": "Intern at ABC Corp",
  "projects": "Chatbot, Resume Generator",
}
📦 Installation & Setup

# Clone the repo
git clone https://github.com/jaswanthreddy0006/genai-resume-builder.git

cd genai-resume-builder

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
📁 Project Structure
genai-resume-builder/
├── app.py               # Main application file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── public/              # Static assets
│   ├── flowchart.png
│   └── sequence.png
├── .gradio/             # Interface files (optional)
📖 Supported Resume Fields
Full Name

Email / Phone

Objective (optional)

Education

Projects

Experience

Skills

Certifications / Achievements

Languages Known

💾 PDF Customization Options
Choose layout template (future update)

Change fonts, section order (planned)

Export to .docx or .json (in roadmap)

📱 Deployment Options
Local: Run python app.py

HuggingFace Spaces: One-click deploy

Streamlit Cloud: For live hosting

🔮 Future Improvements
Multiple resume templates

Auto-save drafts

LinkedIn scraping for auto-fill

AI-powered objective/summary suggestions

Export to .docx and .json

👨‍💻 Author
Name: Jaswanth Reddy
GitHub: jaswanthreddy0006
Email: youremail@example.com

📜 License
This project is intended for educational use only. No commercial use without permission.

🙌 Acknowledgements
OpenAI

Gradio

HuggingFace

Streamlit