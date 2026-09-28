from resume_parser import read_file
from jd_parser import read_job_description

from matcher import extract_skills
from matcher import calculate_score
from matcher import find_missing_skills

from recommender import get_recommendations
from suggestions import get_suggestions
from certification_recommender import get_certification_recommendations


print("========================================")
print("     RESUME - JD MATCHING CHATBOT")
print("========================================")


# ----------------------------------------
# 1. GET FILE PATHS
# ----------------------------------------

resume_path = input("\nEnter resume file path: ")

jd_path = input("Enter job description file path: ")


# ----------------------------------------
# 2. READ RESUME AND JD
# ----------------------------------------

resume_text = read_file(resume_path)

jd_text = read_job_description(jd_path)


# ----------------------------------------
# 3. EXTRACT SKILLS
# ----------------------------------------

resume_skills = extract_skills(resume_text)

jd_skills = extract_skills(jd_text)


# ----------------------------------------
# 4. FIND MATCHED SKILLS
# ----------------------------------------

matched_skills = list(
    set(resume_skills) & set(jd_skills)
)


# ----------------------------------------
# 5. FIND MISSING SKILLS
# ----------------------------------------

missing_skills = find_missing_skills(
    resume_skills,
    jd_skills
)


# ----------------------------------------
# 6. CALCULATE SCORE
# ----------------------------------------

score = calculate_score(
    resume_skills,
    jd_skills
)


# ----------------------------------------
# 7. RECOMMENDED COURSES
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
# 9. RECOMMENDED CERTIFICATIONS
# ----------------------------------------

certifications = get_certification_recommendations(
    missing_skills
)


# ========================================
# RESULT
# ========================================

print("\n========================================")
print("              RESULT")
print("========================================")


# ----------------------------------------
# MATCHING SCORE
# ----------------------------------------

print("\nMatching Score:", score, "%")


# ----------------------------------------
# MATCHED SKILLS
# ----------------------------------------

print("\nMatched Skills:")

for skill in matched_skills:
    print("-", skill)


# ----------------------------------------
# MISSING SKILLS
# ----------------------------------------

print("\nMissing Skills:")

for skill in missing_skills:
    print("-", skill)


# ----------------------------------------
# RECOMMENDED COURSES
# ----------------------------------------

print("\nRecommended Courses:")

for skill in recommendations:

    print("\n", skill)

    for course in recommendations[skill]:
        print("  -", course)


# ----------------------------------------
# RESUME SUGGESTIONS
# ----------------------------------------

print("\nResume Suggestions:")

for suggestion in suggestions:
    print("-", suggestion)


# ----------------------------------------
# RECOMMENDED CERTIFICATIONS
# ----------------------------------------

print("\nRecommended Certifications:")

for skill in certifications:

    print("\n", skill)

    for certification in certifications[skill]:
        print("  -", certification)


print("\n========================================")
print("          ANALYSIS COMPLETE")
print("========================================")