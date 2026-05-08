def calculate_score(candidate, job):
    score = 0

    for skill in job["skills"]:
        if skill in candidate["skills"]:
            score += 10

    return score