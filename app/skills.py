SKILL_DATABASE = {

    "Programming": [
        "python",
        "java",
        "c++",
        "javascript",
        "typescript"
    ],

    "Data": [
        "sql",
        "pandas",
        "numpy",
        "power bi",
        "tableau",
        "excel"
    ],

    "Backend": [
        "fastapi",
        "flask",
        "django",
        "rest api",
        "sqlalchemy"
    ],

    "AI/ML": [
        "machine learning",
        "deep learning",
        "nlp",
        "scikit-learn",
        "tensorflow",
        "pytorch"
    ],

    "Cloud": [
        "azure",
        "aws",
        "gcp",
        "microsoft fabric"
    ],

    "Engineering": [
        "git",
        "github",
        "docker",
        "pytest",
        "linux",
        "unit testing"
    ]
}


def extract_skills(text):

    text = text.lower()

    result = []

    for category, skills in SKILL_DATABASE.items():

        for skill in skills:

            if skill in text:

                result.append({
                    "skill": skill,
                    "category": category
                })

    return result
