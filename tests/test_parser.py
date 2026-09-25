import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.skills import extract_skills


def test_extract_skills_finds_known_terms():
    text = "We need a candidate skilled in Python, SQL and Docker."
    skills = extract_skills(text)
    found = {item["skill"] for item in skills}
    assert "python" in found
    assert "sql" in found
    assert "docker" in found


def test_extract_skills_empty_text():
    assert extract_skills("") == []
