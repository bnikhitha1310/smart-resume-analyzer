import streamlit as st
import PyPDF2
from skills import skills_dict

# Function to extract text from PDF
def extract_text(file):
    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        return text.lower()

    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""


# Function to analyze resume
def analyze_resume(resume_text, role):

    required_skills = skills_dict.get(role.lower(), [])

    if not required_skills:
        return 0, [], [], "Role not found"

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(required_skills)) * 100

    return score, matched, missing, None


# Streamlit UI
st.set_page_config(page_title="Smart Resume Analyzer")

st.title("📄 Smart Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

role = st.text_input(
    "Enter Job Role",
    placeholder="Example: Data Analyst"
)

if st.button("Analyze Resume"):

    if uploaded_file and role:

        resume_text = extract_text(uploaded_file)

        score, matched, missing, error = analyze_resume(
            resume_text,
            role
        )

        if error:
            st.warning("Job role not found in skills database.")

        else:
            st.subheader(f"🎯 Match Score: {score:.2f}%")

            st.success(
                f"✅ Matched Skills: {', '.join(matched) if matched else 'None'}"
            )

            st.error(
                f"❌ Missing Skills: {', '.join(missing) if missing else 'None'}"
            )

            if missing:
                st.info("💡 Suggested Skills to Add")

                for skill in missing:
                    st.write(f"• {skill}")

    else:
        st.warning("Please upload a resume and enter a job role.")