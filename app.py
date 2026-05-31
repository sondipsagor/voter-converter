
from flask import Flask, render_template, request, send_file, jsonify
from parser import extract_from_pdf
import pandas as pd
from pathlib import Path
import uuid

app = Flask(__name__)
UPLOADS=Path("uploads"); OUTPUT=Path("output")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    f=request.files["pdf"]
    uid=str(uuid.uuid4())
    pdf_path=UPLOADS/f"{uid}.pdf"
    f.save(pdf_path)

    rows=extract_from_pdf(pdf_path)

    excel_path=OUTPUT/f"{uid}.xlsx"
    pd.DataFrame(rows).to_excel(excel_path,index=False)

    return send_file(excel_path,as_attachment=True,download_name="voter_list.xlsx")

if __name__=="__main__":
    app.run()
