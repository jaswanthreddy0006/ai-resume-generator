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

## 📈 Project Flowchart

This shows how data flows from user input to resume output:

![Flowchart](public/flowchart.png)

---

## 🔁 Sequence Diagram

This shows how the user, frontend, backend, model, and PDF generator interact:

![Sequence Diagram](public/sequence.png)

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

## 🏗️ System Architecture (Text Overview)

1. **Frontend**: Accepts user input via Gradio  
2. **Backend**: Sends data to the LLM for structured output  
3. **Model**: GPT model formats content into resume layout  
4. **PDF Generator**: Converts final content into a downloadable file  
5. **Output**: PDF preview/download enabled

---

## 📜 Code Sample

```python
resume_data = {
  "name": "Jaswanth Reddy",
  "education": "B.Tech in CSE",
  "skills": ["Python", "Machine Learning", "AI"],
  "experience": "Intern at ABC Corp",
  "projects": "Chatbot, Resume Generator",
}

formatted_resume = generate_resume(resume_data)
```

---

## 🛠 Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/jaswanthreddy0006/genai-resume-builder.git
cd genai-resume-builder

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

---

## 📁 Project Structure

```
genai-resume-builder/
├── app.py               # Main application file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── public/              # Static assets
│   ├── flowchart.png
│   └── sequence.png
├── .gradio/             # Interface files (optional)
```

---

## 📝 Supported Resume Sections

- Full Name
- Contact Details
- Objective (optional)
- Education
- Projects
- Work Experience
- Skills
- Certifications / Achievements
- Languages Known
- Hobbies and Interests

---

## 📦 PDF Output Features

- Clean formatting with section headings
- Auto-wrap text with bullet points
- Downloadable in one click
- Print-ready and shareable

---

## 📱 Deployment Options

- **Local**: Run with Python
- **HuggingFace Spaces**: Upload as a hosted app
- **Streamlit Cloud**: Deploy with one click

---

## 🔮 Future Enhancements

- Multiple resume templates
- Light/Dark theme toggle
- LinkedIn scraper to autofill resume
- Export to `.docx`, `.json`
- Resume score analysis using AI
- Multi-language support

---

## 👨‍💻 Author

**Name:** Jaswanth Reddy  
**GitHub:** [jaswanthreddy0006](https://github.com/jaswanthreddy0006)  
**Email:** jaswanth9985834977@gmail.com

---

## 📜 License

This project is for educational purposes only.  
Licensed under the MIT License.

---

## 🙌 Acknowledgements

- [OpenAI](https://openai.com)  
- [Gradio](https://gradio.app)  
- [HuggingFace](https://huggingface.co)  
- [Python](https://www.python.org)
