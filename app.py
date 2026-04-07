<<<<<<< HEAD
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "AI is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "comment" not in data:
        return jsonify({"error": "No comment"}), 400

    text = data["comment"]

    result = model.predict([text])[0]

    return jsonify({
        "result": str(result)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
=======
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "AI is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    comment = data["comment"]

    vec = vectorizer.transform([comment])
    result = model.predict(vec)[0]

    return jsonify({"result": result})

app.run(host="0.0.0.0", port=10000)
>>>>>>> 22f980f1ed9b18f8daedda3bee189e6df3240e60
