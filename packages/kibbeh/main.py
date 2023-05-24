from sanic import Sanic
from sanic.response import text, file 
from sanic.log import logger
from sanic import response
from sanic_cors import CORS

from pdfminer.high_level import extract_text
from fpdf import FPDF

import os
import uuid

from io import BytesIO, StringIO

import redis
import spacy

app = Sanic("Summarizer")
CORS(app)

def read_pdf(file_path):
    text = extract_text(file_path)
    return text


def summarize_pdf(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    summarized_text = ' '.join(sentences)  # Extract the sentences
    return summarized_text


def remove_non_latin1_chars(text):
    return text.encode('latin-1', 'ignore').decode('latin-1')


def write_pdf(file_path, title, text):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", style="B", size=22)
    pdf.cell(0, 10, txt=title, ln=True, align="C")

    pdf.ln(20)

    pdf.set_font("Arial", size=12)

    text = remove_non_latin1_chars(text)

    lines = []
    for line in text.split('\n'):
        lines.extend(pdf.multi_cell(0, 10, txt=line))

    total_lines = sum(lines)
    line_height = 10  # Adjust line height

    pdf.ln(total_lines * line_height)

    if pdf.get_y() > 260:
        pdf.add_page()

    output_path = os.path.join("output", file_path)
    pdf.output(output_path)


@app.route('/summarize', methods=['POST'])
async def summarize(request):
    if not request.files or 'pdf_file' not in request.files:
        return response.text('No pdf file uploaded!', 400)

    pdf_file = request.files.get('pdf_file')
    file_type = pdf_file.name.rsplit(".", 1)[1].lower()

    if not pdf_file or file_type != "pdf":
        return response.text('File uploaded is not a pdf file', 400)

    try:
        text = read_pdf(BytesIO(pdf_file.body))
        summary = summarize_pdf(text)

        unique_id = str(uuid.uuid4())
        output_pdf_path = f"{unique_id}.pdf"
    
        write_pdf(output_pdf_path, "Summarized File", summary)

        return response.json({"id": unique_id}, 200)

    except Exception as e:
        logger.error(f"Error during processing: {e}")
        return response.text("An error occured durring processing", 500)

@app.route('/pdf/<id>', methods=['GET'])
async def get_pdf(request, id):
    try:
        # decode bytes to string
        output_pdf_path = f"output/{id}.pdf"

        return await file(output_pdf_path, headers={"Content-Disposition": "inline"})

    except FileNotFoundError as e:
        return response.text('File not found. It may have been deleted.', 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)