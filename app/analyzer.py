from .skills import extract_skills
from .matcher import (
    semantic_similarity,
    fuzzy_similarity
)
from .scorer import calculate_score


def analyze_resume(
    resume_text,
    job_description
):

    required_skills = extract_skills(
        job_description
    )

    resume_lower = resume_text.lower()

    matched = []
    missing = []

    for item in required_skills:

        if item["skill"] in resume_lower:

            matched.append(item)

        else:

            missing.append(item)

    semantic = semantic_similarity(
        resume_text,
        job_description
    )

    fuzzy = fuzzy_similarity(
        resume_text,
        job_description
    )

    score = calculate_score(
        semantic,
        fuzzy,
        len(matched),
        len(required_skills)
    )

    return {
        "score": score,
        "semantic_similarity": round(
            semantic * 100,
            2
        ),
        "fuzzy_similarity": round(
            fuzzy * 100,
            2
        ),
        "matched_skills": matched,
        "missing_skills": missing
    }
