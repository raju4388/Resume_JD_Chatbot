def find_missing_skills(resume_skills, jd_skills):

    missing = []

    for skill in jd_skills:

        if skill not in resume_skills:
            missing.append(skill)

    return missing