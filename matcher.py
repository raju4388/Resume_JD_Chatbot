import json
import re


# ========================================
# LOAD SKILLS
# ========================================

def load_skills():

    with open("skills.json", "r") as file:
        data = json.load(file)

    skills = []

    for category in data:
        skills.extend(data[category])

    return skills


# ========================================
# CLEAN TEXT
# ========================================

def clean_text(text):

    text = text.lower()

    # Replace special characters with spaces
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text


# ========================================
# EXTRACT SKILLS
# ========================================

def extract_skills(text):

    text = clean_text(text)

    skills = load_skills()

    found_skills = []

    for skill in skills:

        skill_clean = clean_text(skill)

        # Direct search
        if skill_clean in text:
            found_skills.append(skill)

    return found_skills


# ========================================
# CALCULATE SCORE
# ========================================

def calculate_score(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    jd_set = set(
        skill.lower()
        for skill in jd_skills
    )

    matched = resume_set & jd_set

    score = (
        len(matched) / len(jd_set)
    ) * 100

    return round(score, 2)


# ========================================
# FIND MISSING SKILLS
# ========================================

def find_missing_skills(
    resume_skills,
    jd_skills
):

    resume_set = set(
        skill.lower()
        for skill in resume_skills
    )

    missing = []

    for skill in jd_skills:

        if skill.lower() not in resume_set:
            missing.append(skill)

    return missing