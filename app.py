from flask import Flask, render_template, request, send_file
import pandas as pd
from parser import extract_from_pdf
from pathlib import Path
import uuid

app = Flask(__name__)

UPLOAD = Path("uploads")
OUTPUT = Path("output")
UPLOAD.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    file = request.files["pdf"]

    uid = str(uuid.uuid4())
    path = UPLOAD / f"{uid}.pdf"
    file.save(path)

    data = extract_from_pdf(path)

    df = pd.DataFrame(data)
    out = OUTPUT / f"{uid}.xlsx"
    df.to_excel(out, index=False)

    return send_file(out, as_attachment=True)

if __name__ == "__main__":
    app.run()
