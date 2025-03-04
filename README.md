# AI Resume Screening and Candidate Ranking

This project is a simple AI-powered resume screening and candidate ranking system implemented in a single Python file using Streamlit. It extracts text from resumes (PDF and DOCX), preprocesses the text, computes TF-IDF features, calculates cosine similarity with a provided job description, and displays the results in a sortable table.

## Features

- **Resume Upload:**  
  Upload one or more resumes in PDF or DOCX format.

- **Job Description Input:**  
  Enter the job description directly into a text area.

- **Text Extraction & Preprocessing:**  
  Extract text from resumes and clean the text by converting to lowercase, removing numbers, extra spaces, and stopwords.

- **TF-IDF Vectorization:**  
  Transform text into numerical features using TF-IDF.

- **Cosine Similarity Calculation:**  
  Compute similarity between each resume and the job description.

- **Candidate Ranking:**  
  Display the similarity scores and rank the resumes in a table format.

## Installation

1. **Clone the repository** (if applicable) or download the `app.py` and `README.md` files.

2. **Install Dependencies:**  
   Use `pip` to install the required packages:
   ```bash
   pip install streamlit scikit-learn nltk PyPDF2 docx2txt numpy pandas
