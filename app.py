import streamlit as st
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# Ensure NLTK stopwords are downloaded
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# ------------------------------
# File Extraction
# ------------------------------
def extract_text(file):
    """
    Extract text from resume files based on file extension.
    Uses PyPDF2 for PDFs and docx2txt for DOCX files.
    """
    filename = file.name.lower()
    if filename.endswith('.pdf'):
        try:
            import PyPDF2
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
            return text.strip()
        except Exception as e:
            st.error(f"Error reading PDF file ({file.name}): {e}")
            return ""
    elif filename.endswith('.docx'):
        try:
            import docx2txt
            file.seek(0)
            text = docx2txt.process(file)
            return text.strip()
        except Exception as e:
            st.error(f"Error reading DOCX file ({file.name}): {e}")
            return ""
    else:
        # Fallback: try to decode as text
        try:
            content = file.read()
            try:
                text = content.decode("utf-8")
            except Exception:
                text = str(content)
            return text.strip()
        except Exception as e:
            st.error(f"Error reading file ({file.name}): {e}")
            return ""

# ------------------------------
# Preprocessing and Feature Extraction
# ------------------------------
def clean_text(text):
    """
    Clean text by:
    - Converting to lowercase
    - Removing numbers
    - Removing extra spaces
    - Removing stopwords
    """
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def vectorize_text(documents):
    """
    Convert a list of text documents into a TF-IDF matrix.
    Returns the TF-IDF matrix and feature names.
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    return tfidf_matrix, feature_names

def compute_similarity(tfidf_matrix):
    """
    Compute cosine similarity between each resume and the job description.
    Assumes the job description is the last document.
    """
    job_desc_vector = tfidf_matrix[-1]
    resume_vectors = tfidf_matrix[:-1]
    similarities = cosine_similarity(resume_vectors, job_desc_vector)
    return similarities.flatten()

def rank_candidates(similarities, top_n=10):
    """
    Rank resumes based on similarity scores and return the indices of the top candidates.
    """
    ranked_indices = np.argsort(similarities)[::-1]
    return ranked_indices[:top_n]

# ------------------------------
# Streamlit Application
# ------------------------------
def main():
    st.title("AI Resume Screening and Candidate Ranking")

    # File uploader for resumes
    uploaded_files = st.file_uploader("Upload Resumes", type=["pdf", "docx"], accept_multiple_files=True)
    
    # Text area for job description
    job_desc_text = st.text_area("Enter Job Description", placeholder="Paste job description here...")

    if st.button("Screen Candidates"):
        if uploaded_files and job_desc_text:
            resumes_text = []
            resume_names = []
            for file in uploaded_files:
                text = extract_text(file)
                if not text:
                    st.warning(f"No text extracted from {file.name}")
                cleaned_text = clean_text(text)
                resumes_text.append(cleaned_text)
                resume_names.append(file.name)

            # Preprocess the job description
            job_desc_clean = clean_text(job_desc_text)

            # Combine resume texts and job description (job description must be last)
            documents = resumes_text + [job_desc_clean]
            if all(doc == "" for doc in documents):
                st.error("No valid text extracted from the provided documents.")
                return

            tfidf_matrix, _ = vectorize_text(documents)
            similarities = compute_similarity(tfidf_matrix)

            # Create a DataFrame to display results
            results = []
            for i, score in enumerate(similarities):
                results.append({
                    "Resume": resume_names[i],
                    "Similarity Score": round(score, 4)
                })
            df_results = pd.DataFrame(results)
            
            # Optionally, sort the table by score in descending order
            df_results = df_results.sort_values(by="Similarity Score", ascending=False).reset_index(drop=True)
            
            st.write("### Candidate Ranking")
            st.dataframe(df_results)
        else:
            st.error("Please upload at least one resume and provide a job description.")

if __name__ == "__main__":
    main()
