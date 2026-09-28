from flask import Flask, render_template, request
from analyzer import analyze_resume_and_jd
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files.get("resume")
    jd = request.files.get("jd")

    if not resume or not jd:
        return "Please upload both Resume and Job Description."

    # Create upload folder
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    # Keep original file extensions
    resume_ext = os.path.splitext(resume.filename)[1]
    jd_ext = os.path.splitext(jd.filename)[1]

    resume_path = os.path.join(
        upload_folder,
        "resume" + resume_ext
    )

    jd_path = os.path.join(
        upload_folder,
        "job_description" + jd_ext
    )

    resume.save(resume_path)
    jd.save(jd_path)

    try:

        result = analyze_resume_and_jd(
            resume_path,
            jd_path
        )

    except Exception as error:

        return f"""
        <h2>❌ Error during analysis</h2>
        <p>{str(error)}</p>
        <br>
        <a href="/">Go Back</a>
        """

    return render_results(result)


def render_results(result):

    matched = ""

    for skill in result["matched_skills"]:
        matched += f"<li>{skill}</li>"

    missing = ""

    for skill in result["missing_skills"]:
        missing += f"<li>{skill}</li>"

    courses = ""

    for skill in result["recommendations"]:

        courses += f"<h4>{skill}</h4><ul>"

        for course in result["recommendations"][skill]:
            courses += f"<li>{course}</li>"

        courses += "</ul>"

    certifications = ""

    for skill in result["certifications"]:

        certifications += f"<h4>{skill}</h4><ul>"

        for certification in result["certifications"][skill]:
            certifications += f"<li>{certification}</li>"

        certifications += "</ul>"

    suggestions = ""

    for suggestion in result["suggestions"]:
        suggestions += f"<li>{suggestion}</li>"

    return f"""
    <!DOCTYPE html>

    <html>

    <head>

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>Resume-JD Analysis</title>

        <style>

            body {{
                font-family: Arial;
                background: #e5ddd5;
                margin: 0;
            }}

            .header {{
                background: #075e54;
                color: white;
                padding: 18px;
                text-align: center;
                font-size: 22px;
                font-weight: bold;
            }}

            .container {{
                max-width: 700px;
                margin: auto;
                padding: 20px;
            }}

            .card {{
                background: white;
                padding: 20px;
                margin-bottom: 15px;
                border-radius: 12px;
            }}

            .score {{
                font-size: 35px;
                font-weight: bold;
                text-align: center;
                color: #075e54;
            }}

            li {{
                margin: 8px;
            }}

            button {{
                width: 100%;
                padding: 14px;
                background: #128c7e;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 17px;
            }}

        </style>

    </head>

    <body>

        <div class="header">
            🤖 Resume-JD Analysis Chatbot
        </div>

        <div class="container">

            <div class="card">

                <h2>📊 Matching Score</h2>

                <div class="score">
                    {result["score"]}%
                </div>

            </div>


            <div class="card">

                <h2>✅ Matched Skills</h2>

                <ul>
                    {matched}
                </ul>

            </div>


            <div class="card">

                <h2>❌ Missing Skills</h2>

                <ul>
                    {missing}
                </ul>

            </div>


            <div class="card">

                <h2>📚 Recommended Courses</h2>

                {courses}

            </div>


            <div class="card">

                <h2>🏆 Recommended Certifications</h2>

                {certifications}

            </div>


            <div class="card">

                <h2>💡 Resume Suggestions</h2>

                <ul>
                    {suggestions}
                </ul>

            </div>


            <div class="card">

                <a href="/">
                    <button>🔄 Analyze Another Resume</button>
                </a>

            </div>

        </div>

    </body>

    </html>
    """


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )