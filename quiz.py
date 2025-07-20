from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

@app.route("/")
def serve_html():
    return send_file("quiz.html")

@app.route("/quiz.css")
def serve_css():
    return send_file("quiz.css")

@app.route("/quiz.js")
def serve_js():
    return send_file("quiz.js")

@app.route("/learn.html")
def serve_learn():
    return send_file("learn.html")

@app.route("/generate-quiz", methods=["POST"])
def generate_quiz():
    data = request.get_json()
    topic = data.get("topic")
    age = data.get("age")

    prompt = f"Create 3 multiple choice questions for the topic '{topic}' for students aged {age}. Include 4 options and mark the correct answer clearly."

    model = genai.GenerativeModel("models/gemini-2.5-pro")
    response = model.generate_content(prompt)

    return jsonify({"quiz": response.text})

if __name__ == "__main__":
    app.run(debug=True)
