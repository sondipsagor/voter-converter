
import pdfplumber,re

def extract_from_pdf(pdf_path):
    text=""
    with pdfplumber.open(pdf_path) as pdf:
        for p in pdf.pages:
            text += (p.extract_text() or "") + "\n"

    data=[]
    serials=re.finditer(r'(\d{3})\.', text)
    for m in serials:
        data.append({
            "Serial Number": m.group(1),
            "Name":"",
            "Voter Number":"",
            "Birth Date":"",
            "Occupation":"",
            "Address":""
        })
    return data
