from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai  # Google Gemini API

app = Flask(__name__)
CORS(app)

# 🔹 Google Gemini API Setup (Replace with your actual API Key)
API_KEY = "AIzaSyBI_6DGp_Ja_qEdhITwrhPYuhUAPMZBQ8I"
genai.configure(api_key=API_KEY)

# 🎯 Predefined responses with emojis
custom_responses = {
    "who are you": "I am MittBot 🤖! I work with MittSure Technology to assist you. 🚀",
    "what is your name": "I am MittBot 🤖, your AI assistant from MittSure Technology! 😊",
    "tell me about yourself": "I am MittBot, designed to help with your queries as part of Mittsure Technology! 🚀",
    "who is manoj mittal": "Manoj Mittal is a visionary leader and business tycoon. 🌟 He leads Mittsure Technologies with a mission to empower education. 📚",
    "who is yash mittal": "Yash Mittal 🎓 is the youngest director of Mittsure Technologies, specializing in Computer Systems Engineering. 💡",
    "who is ishita mittal": "Ishita Mittal 🚀, a Computer Science graduate, is shaping Mittsure Technologies' future with innovation. 💻",
    "what is mittsure technologies": "Mittsure Technologies is revolutionizing education 📚 with cutting-edge solutions. 🌍",
    "what is anand international college of engineering": "Anand International College of Engineering 🏫 is a top-ranked institution offering world-class education. 🎓",
    "what is lumalearn": "LumaLearn is a play-based early education program integrating interactive activities with NCERT-inspired Jaadui Pitara for holistic child development. 📖🎨",
    "what is thinktrail": "ThinkTrail is a NEP 2020-aligned learning program by Mittsure for Grades 1-8, integrating AR, AI (Mittsure Lens by Embibe), and interactive tools (TeachLite) to enhance education through storytelling, 3D content, and immersive learning. 📚🚀"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").strip().lower()  # Convert input to lowercase

    # ✅ Check predefined responses first
    if user_message in custom_responses:
        return jsonify({"response": custom_responses[user_message]})

    # ✅ If no predefined response, call Google Gemini AI
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Use a supported model
        response = model.generate_content(user_message)

        if hasattr(response, "text"):  # Ensure response has text
            return jsonify({"response": response.text + " 🤖✨"}) 
        else:
            return jsonify({"error": "No valid response from AI 😞"}), 500

    except Exception as e:
        print("🔥 ERROR:", str(e))  # Debugging
        return jsonify({"error": "AI model error 😞"}), 500

if __name__ == "__main__":
    app.run(debug=True)
