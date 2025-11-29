from flask import Flask, render_template, request
import requests
import os  # <-- for getting PORT from environment

app = Flask(__name__)

# Live FastAPI URL
FASTAPI_URL = "https://crypto-predict-api-zl1q.onrender.com/predict"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Collect data from form
    data = {
        "total_vol": float(request.form["total_vol"]),
        "price": float(request.form["price"]),
        "volume_24h": float(request.form["volume_24h"]),
        "change_7d": float(request.form["change_7d"]),
        "marketcap": float(request.form["marketcap"]),
        "price_to_mc": float(request.form["price_to_mc"]),
        "vol_to_mc": float(request.form["vol_to_mc"]),
        "vol_to_price": float(request.form["vol_to_price"]),
        "log_price": float(request.form["log_price"]),
        "log_vol": float(request.form["log_vol"]),
        "log_marketcap": float(request.form["log_marketcap"]),
        "abs_change_7d": float(request.form["abs_change_7d"]),
        "diff_change": float(request.form["diff_change"]),
        "name_encodedr": int(request.form["name_encodedr"]),
        "symbol_encoder": int(request.form["symbol_encoder"])
    }

    try:
        # Call FastAPI backend
        response = requests.post(FASTAPI_URL, json=data)
        prediction_json = response.json()

        prediction = prediction_json["prediction"]
        prob_down = prediction_json["probability_down"]
        prob_up = prediction_json["probability_up"]

        # Display result on webpage
        return render_template(
            "result.html",
            prediction=prediction,
            prob_down=prob_down,
            prob_up=prob_up
        )
    except Exception as e:
        return f"Error: {e}"

# ✅ Updated for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default 5000 locally
    app.run(host="0.0.0.0", port=port, debug=True)
