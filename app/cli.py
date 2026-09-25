from pathlib import Path

from .extractor import extract_text
from .analyzer import analyze_resume
from .recommendations import (
    generate_recommendations
)
from .report import generate_report


def clean_path(raw_path):
    """
    Terminals like PowerShell/cmd keep surrounding quotes when a path
    is pasted or drag-and-dropped in. Strip those, plus stray
    whitespace, so "C:\\...\\file.pdf" and C:\\...\\file.pdf both work.
    """

    return raw_path.strip().strip('"').strip("'").strip()


def run():

    resume = clean_path(
        input("Resume path: ")
    )

    job_description = clean_path(
        input("Job description path: ")
    )

    if not Path(resume).exists():
        print(f"Resume file not found: {resume}")
        return

    if not Path(job_description).exists():
        print(f"Job description file not found: {job_description}")
        return

    resume_text = extract_text(
        resume
    )

    job_text = Path(
        job_description
    ).read_text(
        encoding="utf-8"
    )

    analysis = analyze_resume(
        resume_text,
        job_text
    )

    recommendations = (
        generate_recommendations(
            analysis
        )
    )

    print("\n==============================")
    print("RESUME ANALYSIS")
    print("==============================")

    print(
        f"Match Score: "
        f"{analysis['score']}%"
    )

    print("\nMatched Skills:")

    for item in analysis[
        "matched_skills"
    ]:

        print(
            f"  [x] {item['skill']}"
        )

    print("\nMissing Skills:")

    for item in analysis[
        "missing_skills"
    ]:

        print(
            f"  [ ] {item['skill']}"
        )

    print("\nRecommendations:")

    for recommendation in recommendations:

        print(
            f"  - {recommendation}"
        )

    generate_report(
        analysis,
        recommendations
    )

    print(
        "\nReport generated: "
        "resume_report.pdf"
    )
