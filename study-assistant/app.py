import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# GROQ API SETUP
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# AI RESPONSE FUNCTION
def generate_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# HOME PAGE
@app.route("/")
def index():
    return render_template("index.html")


# EXPLAIN CONCEPT
@app.route("/api/explain", methods=["POST"])
def explain():
    data = request.get_json()

    topic = data.get("topic", "")
    level = data.get("level", "Beginner")

    prompt = f"""
    Explain the concept of {topic} for a {level} student.
    Use simple language and real-world analogy.
    """

    result = generate_ai_response(prompt)

    return jsonify({"result": result})


# GENERATE QUIZ
@app.route("/api/quiz", methods=["POST"])
def quiz():
    data = request.get_json()

    topic = data.get("topic", "")

    prompt = f"""
    Generate 3 MCQ quiz questions on {topic}.
    Include options and correct answers.
    """

    result = generate_ai_response(prompt)

    return jsonify({"result": result})


# SUMMARISE TEXT
@app.route("/api/summarise", methods=["POST"])
def summarise():
    data = request.get_json()

    text = data.get("text", "")

    prompt = f"""
    Summarise the following text into bullet points:

    {text}
    """

    result = generate_ai_response(prompt)

    return jsonify({"result": result})


# LEARNING ROADMAP
@app.route("/api/roadmap", methods=["POST"])
def roadmap():
    data = request.get_json()

    topic = data.get("topic", "")

    prompt = f"""
    Create a beginner-friendly 4-week roadmap for learning {topic}.
    """

    result = generate_ai_response(prompt)

    return jsonify({"result": result})


# RUN FLASK
if __name__ == "__main__":
    app.run(debug=True)