from resume_parser import read_file
from jd_parser import read_job_description

from matcher import extract_skills
from matcher import calculate_score
from matcher import find_missing_skills

from recommender import get_recommendations
from suggestions import get_suggestions
from certification_recommender import get_certification_recommendations


def analyze_resume_and_jd(resume_path, jd_path):

    # ----------------------------------------
    # 1. READ RESUME
    # ----------------------------------------

    resume_text = read_file(resume_path)

    # ----------------------------------------
    # 2. READ JOB DESCRIPTION
    # ----------------------------------------

    jd_text = read_job_description(jd_path)

    # ----------------------------------------
    # 3. EXTRACT SKILLS
    # ----------------------------------------

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(jd_text)

    # ----------------------------------------
    # 4. MATCHED SKILLS
    # ----------------------------------------

    matched_skills = list(
        set(resume_skills) & set(jd_skills)
    )

    # ----------------------------------------
    # 5. MISSING SKILLS
    # ----------------------------------------

    missing_skills = find_missing_skills(
        resume_skills,
        jd_skills
    )

    # ----------------------------------------
    # 6. MATCH SCORE
    # ----------------------------------------

    score = calculate_score(
        resume_skills,
        jd_skills
    )

    # ----------------------------------------
    # 7. COURSE RECOMMENDATIONS
    # ----------------------------------------

    recommendations = get_recommendations(
        missing_skills
    )

    # ----------------------------------------
    # 8. RESUME SUGGESTIONS
    # ----------------------------------------

    suggestions = get_suggestions(
        missing_skills
    )

    # ----------------------------------------
    # 9. CERTIFICATION RECOMMENDATIONS
    # ----------------------------------------

    certifications = get_certification_recommendations(
        missing_skills
    )

    # ----------------------------------------
    # RETURN ALL RESULTS
    # ----------------------------------------

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations,
        "suggestions": suggestions,
        "certifications": certifications
    }