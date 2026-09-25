# Resume Analyzer

An offline resume-to-job-description matching tool.

## Stack
- Python
- PDF/DOCX extraction (pypdf, python-docx)
- Regex-based skill detection
- TF-IDF + cosine similarity (scikit-learn)
- Fuzzy string matching (RapidFuzz)
- Pandas
- ReportLab (PDF reports)

## Setup
```bash
pip install -r requirements.txt
python main.py
```
You'll be prompted for a resume file path (PDF/DOCX/TXT) and a job description
text file path.

## How it works
1. **Extraction** — pulls raw text out of PDF, DOCX, or TXT resumes.
2. **Skill detection** — scans the job description against a curated skill
   dictionary (`app/skills.py`) grouped by category (Programming, Data,
   Backend, AI/ML, Cloud, Engineering).
3. **Matching** — computes a TF-IDF/cosine semantic similarity score and a
   RapidFuzz token-set fuzzy similarity score between resume and job text.
4. **Scoring** — blends semantic similarity (45%), fuzzy similarity (20%),
   and skill-coverage (35%) into one explainable 0-100 match score.
5. **Recommendations** — lists missing skills and general suggestions.
6. **Reporting** — generates a PDF report (`resume_report.pdf`) with the
   score breakdown and matched/missing skills.

## Project layout
```
Resume_Analyzer/
├── main.py
├── app/
│   ├── extractor.py        # PDF/DOCX/TXT text extraction
│   ├── skills.py            # skill keyword database + detector
│   ├── matcher.py            # TF-IDF cosine + fuzzy similarity
│   ├── scorer.py              # weighted final score
│   ├── analyzer.py             # orchestrates the above
│   ├── recommendations.py       # gap analysis suggestions
│   ├── report.py                 # PDF report generation
│   └── cli.py                     # command-line entry point
├── data/
│   ├── skills.json (optional, for future expansion)
│   └── job_descriptions/
└── reports/
```

## Next steps to make it portfolio-grade
- Tkinter or web (Flask/FastAPI) UI instead of CLI
- Section-aware parsing (Experience, Education, Skills sections)
- Support for batch-analyzing multiple resumes against one job description
- Export match results to CSV/Excel for recruiter workflows
