from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/")
def home():
    return jsonify({
        "message": "EMP-22 Backend is working!"
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    resume = data.get("resume", "")
    role = data.get("role", "")
    job_description = data.get("jobDescription", "")

    prompt = f"""
You are a professional resume improvement assistant.

Analyze the following resume for the target job role.

Target Role:
{role}
Job Description:
{job_description}
Resume:
{resume}

Give a simple analysis with:
1. Resume score out of 100
2. Strengths
3. Weak or vague content
4. Improved versions of weak statements
5. Relevant keywords
6. Suggestions for improvement
7. If a job description is provided, compare it with the resume.
8. Show matching skills.
9. Show missing or weakly represented skills.
10. Give a job match percentage.

IMPORTANT:
Do not invent or fabricate any skills, achievements, experience,
certifications, companies, or numbers that are not present in the resume.
Only improve the user's existing information.
Only identify missing skills from the job description.
Do not tell the user to claim a skill they do not actually have.
"""


    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result = response.output_text

    return jsonify({
        "analysis": result
    })


if __name__ == "__main__":
    app.run(debug=True)