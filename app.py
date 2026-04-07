from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép các trình duyệt gọi API từ domain khác

# ===== LOAD MODEL =====
try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print("Model & Vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading files: {e}")

# ===== HOME =====
@app.route("/")
def home():
    return "AI Sentiment Analysis Server is running!"

# ===== API PREDICT =====
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data or "comment" not in data:
            return jsonify({"error": "Missing 'comment' field"}), 400

        comment = data.get("comment")
        
        # Chuyển đổi văn bản thành vector
        X = vectorizer.transform([comment])
        
        # Dự đoán
        prediction = model.predict(X)[0]

        return jsonify({
            "status": "success",
            "comment": comment,
            "prediction": str(prediction)
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)