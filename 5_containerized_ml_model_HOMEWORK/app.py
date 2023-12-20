from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# load ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def hello():
    return "<h1>HELLO</h1>"


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"ping": "success"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data)
    result = model.predict(input_data).tolist()
    return jsonify({"Result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
