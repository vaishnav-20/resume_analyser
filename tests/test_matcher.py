import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.scorer import calculate_score


def test_calculate_score_perfect_match():
    score = calculate_score(1.0, 1.0, 5, 5)
    assert score == 100.0


def test_calculate_score_no_skills_required():
    score = calculate_score(0.5, 0.5, 0, 0)
    assert round(score, 2) == round((0.5 * 0.45 + 0.5 * 0.20) * 100, 2)
