from ats_engine.ats_scorer import calculate_score

def test_ats():
    candidate = {"skills": ["Python"]}
    job = {"skills": ["Python", "React"]}

    score = calculate_score(candidate, job)

    assert score == 10