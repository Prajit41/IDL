from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv
import google.generativeai as genai
import os

# === Load API Key from .env ===
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# === Gemini Configuration ===
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-2.5-pro')

# === Flask App ===
app = Flask(__name__)

# === Gemini Prompt Handler ===
def get_gemini_prompt(user_input, age_group, task_type):
    if task_type == "feedback":
        return f"""You're a debate coach. A {age_group} student wrote: '{user_input}'.
        Give short feedback (2 lines), highlight any logical fallacies, and suggest one improvement."""

    elif task_type == "learn_rule":
        return f"""Explain the debate concept: '{user_input}' to a {age_group} student. Keep it short, fun, and easy to understand with a real-life example."""

    elif task_type == "generate_topic":
        return f"""Give an age-appropriate debate topic for a {age_group} student. Keep it interesting and balanced."""

    elif task_type == "score_argument":
        return f"""Score the student’s argument: '{user_input}' out of 10 and give a one-line reason."""

    return "Invalid task."

# === API Route ===
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message")
    task = data.get("task", "feedback")
    age_group = data.get("age_group", "middle_school")

    prompt = get_gemini_prompt(message, age_group, task)

    try:
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

# === Frontend Page ===
@app.route("/")
def index():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
  <title>Debate Buddy (AI Chat)</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    input, select, button { margin-top: 10px; padding: 8px; width: 100%; }
    #response { margin-top: 20px; background: #f0f0f0; padding: 10px; border-radius: 8px; }
  </style>
</head>
<body>
  <h2>🧠 Debate Learning AI</h2>
  <label>Age Group:</label>
  <select id="age_group">
    <option value="middle_school">Middle School</option>
    <option value="high_school">High School</option>
    <option value="college">College</option>
  </select>

  <label>Task:</label>
  <select id="task">
    <option value="feedback">Give Feedback</option>
    <option value="learn_rule">Learn Debate Rule</option>
    <option value="generate_topic">Generate Debate Topic</option>
    <option value="score_argument">Score My Argument</option>
  </select>

  <label>Your Message:</label>
  <input type="text" id="message" placeholder="Enter your argument or question here" />

  <button onclick="sendMessage()">Ask AI</button>

  <div id="response"><strong>Reply:</strong> <span id="replyText">...</span></div>

  <script>
    async function sendMessage() {
      const msg = document.getElementById("message").value;
      const task = document.getElementById("task").value;
      const age = document.getElementById("age_group").value;

      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg, task: task, age_group: age })
      });

      const data = await res.json();
      document.getElementById("replyText").innerText = data.reply || data.error;
    }
  </script>
</body>
</html>
    """)

# === Main Entry Point ===
if __name__ == "__main__":
    app.run(debug=True)
