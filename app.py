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