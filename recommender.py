import json


def get_recommendations(missing_skills):

    with open("courses.json", "r") as file:
        courses = json.load(file)

    recommendations = {}

    for skill in missing_skills:

        skill_key = skill.lower()

        if skill_key in courses:
            recommendations[skill] = courses[skill_key]

    return recommendations