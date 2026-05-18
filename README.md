# Smart Resume Analyzer

📄 **Smart Resume Analyzer** is a Streamlit web app that analyzes a resume PDF against a target job role and shows which required skills are matched or missing.

## Features

- Upload a resume in PDF format
- Enter any supported job role (e.g. Data Analyst, Backend Engineer)
- Get an instant match score (%) based on skills found in the resume
- See a breakdown of matched ✅ and missing ❌ skills
- Receive suggested skills to add to improve your resume

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/your-username/smart-resume-analyzer.git
cd smart-resume-analyzer
pip install -r requirements.txt
```

### Requirements

The main dependencies are:

- `streamlit`
- `PyPDF2`

Make sure these are listed in `requirements.txt`.

## Running the App

From the project folder, run:

```bash
streamlit run app.py
```

The app will open in your browser at:

- `http://localhost:8501`

## Usage

1. Upload your resume as a `.pdf` file using the file uploader.
2. Type the job role you're targeting in the text field (e.g. `Data Scientist`).
3. Click **Analyze Resume**.
4. Review your match score and the list of matched vs. missing skills.

## Project Structure

```text
smart-resume-analyzer/
├── app.py          # Main Streamlit application
├── skills.py       # skills_dict mapping roles to required skills
└── requirements.txt
```

## `skills.py`

This file contains a dictionary mapping job role names (lowercase) to a list of required skills.

Example:

```python
skills_dict = {
    "data analyst": ["python", "sql", "excel", "tableau", "statistics"],
    "backend engineer": ["python", "rest api", "docker", "postgresql", "git"],
    # add more roles here
}
```

To add support for a new role, add a new entry to `skills_dict`.

## Limitations

- Skill matching is keyword-based — it checks whether a skill string appears anywhere in the resume text.
- Variations in phrasing (e.g. `PostgreSQL` vs `Postgres`) may not match.
- Only PDF resumes are supported.
- The app only recognizes roles defined in `skills_dict`.

## Contributing

Pull requests are welcome.

To add new roles or improve skill detection accuracy, edit `skills.py` or open an issue describing the improvement.
