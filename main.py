from parsers.resume_parser import parse_resume
from ats_engine.ats_scorer import calculate_score
from scoring.decision_engine import final_decision
from utils.logger import logger

def run_pipeline():
    logger.info("Pipeline started")

    resume_text = "Sample resume text"
    job = {"skills": ["Python", "React"]}

    candidate = parse_resume(resume_text)
    score = calculate_score(candidate, job)
    decision = final_decision(score)

    logger.info(f"Score: {score}, Decision: {decision}")

    print("Final Result:")
    print("Score:", score)
    print("Decision:", decision)

if __name__ == "__main__":
    run_pipeline()