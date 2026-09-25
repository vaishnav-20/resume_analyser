def calculate_score(
    semantic_score,
    fuzzy_score,
    matched_skills,
    total_skills
):

    skill_score = (
        matched_skills / total_skills
        if total_skills
        else 0
    )

    final_score = (
        semantic_score * 0.45
        +
        fuzzy_score * 0.20
        +
        skill_score * 0.35
    )

    return round(
        final_score * 100,
        2
    )
