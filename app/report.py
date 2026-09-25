from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(
    analysis,
    recommendations,
    output="resume_report.pdf"
):

    document = SimpleDocTemplate(
        str(output),
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Overall Match: {analysis['score']}%",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Semantic Similarity: "
            f"{analysis['semantic_similarity']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Fuzzy Similarity: "
            f"{analysis['fuzzy_similarity']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Matched Skills",
            styles["Heading2"]
        )
    )

    matched = ", ".join(
        item["skill"]
        for item in analysis["matched_skills"]
    )

    content.append(
        Paragraph(
            matched or "None",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    missing = ", ".join(
        item["skill"]
        for item in analysis["missing_skills"]
    )

    content.append(
        Paragraph(
            missing or "None",
            styles["BodyText"]
        )
    )

    document.build(
        content
    )
