def generate_recommendations(
    analysis
):

    recommendations = []

    for skill in analysis[
        "missing_skills"
    ]:

        recommendations.append(
            f"Consider adding experience or projects demonstrating "
            f"{skill['skill']}."
        )

    if analysis["score"] < 50:

        recommendations.append(
            "The resume has relatively low textual alignment "
            "with this job description."
        )

    if not recommendations:

        recommendations.append(
            "No major keyword gaps were detected."
        )

    return recommendations
