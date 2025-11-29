
---

### ** Flask Frontend Repo (`flask_frontend`) README.md**

```markdown
# Crypto Prediction Web UI (Flask)

This repository contains the **Flask frontend** for interacting with the FastAPI crypto prediction backend.

## Features
- User-friendly web interface for crypto price prediction
- Auto-fills sample values for easier testing
- Sends input data to FastAPI backend and displays results
- Deployed on cloud (Render)

## Folder Structure


flask_frontend/
│
├── templates/ # HTML templates
│ ├── index.html # Main input form
│ └── result.html # Prediction results
├── static/ # CSS/JS (optional)
├── app.py # Flask app entry point
├── requirements.txt
└── README.md


## Installation
```bash
git clone repo
cd flask_frontend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

Run Locally
python app.py


Web app will be available at: http://127.0.0.1:5000

Enter crypto data or use autofill and click Predict to see results from FastAPI backend.

Configuration

Update the FASTAPI_URL in app.py to point to your deployed FastAPI service:

Deployment

Deployed on Render by setting root directory to flask_frontend/.

Ensure the FastAPI backend URL is live for predictions.

Notes

Frontend communicates with FastAPI via POST requests.

Uses Flask templates for rendering pages.

Auto-fill form fields are included for fast testing.
