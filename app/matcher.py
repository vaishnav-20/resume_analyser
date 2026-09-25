from rapidfuzz import fuzz

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def semantic_similarity(
    resume,
    job_description
):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform([
        resume,
        job_description
    ])

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )

    return float(
        similarity[0][0]
    )


def fuzzy_similarity(
    resume,
    job_description
):

    return fuzz.token_set_ratio(
        resume,
        job_description
    ) / 100
