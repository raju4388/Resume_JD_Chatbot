def get_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if skill == "Counselling":
            suggestions.append(
                "Add counselling or student guidance experience if you have it."
            )

        elif skill == "Email outreach":
            suggestions.append(
                "Add professional email communication experience."
            )

        elif skill == "Networking":
            suggestions.append(
                "Mention networking activities, events, or student interactions."
            )

        elif skill == "Sales":
            suggestions.append(
                "Add sales, business development, or customer interaction experience if applicable."
            )

        elif skill == "Lead generation":
            suggestions.append(
                "Mention lead generation or outreach activities if you have experience."
            )

        elif skill == "Relationship building":
            suggestions.append(
                "Mention teamwork and relationship-building experience."
            )

        elif skill == "Negotiation":
            suggestions.append(
                "Add negotiation or communication activities if applicable."
            )

        elif skill == "Reporting":
            suggestions.append(
                "Mention reports, documentation, or project reporting experience."
            )

        elif skill == "Documentation":
            suggestions.append(
                "Mention project documentation or technical documentation experience."
            )

    return suggestions