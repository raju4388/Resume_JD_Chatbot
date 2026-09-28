import json


def get_certification_recommendations(missing_skills):

    with open("certifications.json", "r") as file:
        certifications = json.load(file)

    recommendations = {}

    for skill in missing_skills:

        skill_key = skill.lower()

        if skill_key in certifications:
            recommendations[skill] = certifications[skill_key]

    return recommendations