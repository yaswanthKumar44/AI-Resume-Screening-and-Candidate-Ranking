🤖 AI Resume Screening and Candidate Ranking System
Welcome to the AI Resume Screening and Candidate Ranking System! This project leverages artificial intelligence to streamline the hiring process by automating resume screening and ranking candidates based on their suitability for a given job description.​

🌟 Features
📤 Resume Upload:
Easily upload multiple resumes in PDF or DOCX formats.​

📝 Job Description Input:
Input the job description directly into a text area for analysis.​
GitHub
+2
Resume Screening AI
+2
CVViZ
+2

🔍 Text Extraction & Preprocessing:
Automatically extract and clean text from resumes, including converting to lowercase and removing numbers, extra spaces, and stopwords.​

📊 TF-IDF Vectorization:
Transform textual data into numerical features using Term Frequency-Inverse Document Frequency (TF-IDF).​

📈 Cosine Similarity Calculation:
Compute the similarity between each resume and the job description to assess relevance.​

🏆 Candidate Ranking:
Display similarity scores and rank resumes in a sortable table for easy comparison.​

🛠️ Installation
📂 Clone the Repository:
Download the app.py and README.md files from the repository.

📦 Install Dependencies:
Use pip to install the required packages:

bash
Copy
Edit
pip install streamlit scikit-learn nltk PyPDF2 docx2txt numpy pandas
🚀 Usage
▶️ Run the Application:
Execute the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📄 Upload Resumes:
Use the file uploader to select one or more resumes in PDF or DOCX formats.

🖊️ Enter Job Description:
Input the job description into the provided text area.

📈 View Results:
The application will process the resumes and display a ranked list based on similarity to the job description.

🧰 Dependencies
Python 3.x​

Streamlit​
The Enterprisers Project
+5
Resume Screening AI
+5
CVViZ
+5

scikit-learn​
GitHub

nltk​

PyPDF2​

docx2txt​

numpy​

pandas​

📚 How It Works
Text Extraction:
The system extracts text from uploaded resumes, supporting both PDF and DOCX formats.

Preprocessing:
The extracted text is cleaned by converting to lowercase, removing numbers, extra spaces, and stopwords to ensure uniformity.

Vectorization:
Utilizing TF-IDF, the textual data is transformed into numerical vectors, facilitating quantitative analysis.

Similarity Calculation:
Cosine similarity is computed between the job description and each resume to determine relevance.

Ranking:
Resumes are ranked based on similarity scores, providing a clear view of the most suitable candidates.

🎯 Purpose
This project aims to demonstrate the application of natural language processing (NLP) techniques in automating the resume screening process, thereby enhancing efficiency and objectivity in candidate selection.​
GitHub
+1
Resume Screening AI
+1

⚠️ Disclaimer
This tool is intended for educational and demonstration purposes. It provides a basic implementation of AI-driven resume screening and may not encompass all factors considered in a comprehensive hiring process.​

By integrating AI into recruitment, this system offers a glimpse into the potential of automating candidate evaluation, streamlining the hiring process, and reducing manual workload.
