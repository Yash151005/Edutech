from flask import Flask, request, jsonify
import google.generativeai as genai

<<<<<<< HEAD
# Gemini API
=======
# Configure Gemini API
>>>>>>> d0ff156 (Added Flask API files)
genai.configure(api_key="AIzaSyAsMZiC9bUCqC2D4h0aHUUK3e8QpSMiUQE")
model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request, 'message' field missing"}), 400
    
    user_message = data["message"]
    
<<<<<<< HEAD
    # for Generateing AI response
=======
    # Generate AI response
>>>>>>> d0ff156 (Added Flask API files)
    ai_response = model.generate_content(user_message).text

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
