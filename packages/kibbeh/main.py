from sanic import Sanic
from sanic.response import text, file 
from sanic.log import logger

from pdfminer.high_level import extract_text
from fpdf import FPDF
from io import StringIO
from tempfile import NamedTemporaryFile

import spacy

app = Sanic("Summarizer")

def read_pdf(file_path):
  text = extract_text(file_path)
  return text

def summarize(text):
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

    pdf.output(file_path)

@app.route('/upload', methods=['POST'])
async def upload(request):  
  if not request.files or 'pdf_file' not in request.files:
    return sanic.response.text('No pdf file uploaded!', 400)

  pdf_file = request.files.get('pdf_file') 
  file_type = pdf_file.filename.rsplit(".", 1)[1].lower()

  if not pdf_file or file_type != "pdf":
    return sanic.response.text('File uploaded is not a pdf file', 400)
  
  with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
    temp_file.write(pdf_file.body)
    temp_pdf_path = temp_file.name

  try:
    text = read_pdf(temp_pdf_path)
    summary = summarize(text)

    with NamedTemporaryFile(delete=False, suffix=".pdf") as output_temp_file:
      output_pdf_path = output_temp_file.name

    write_pdf(output_pdf_path, "Summarized File", summary)

    return await FileResponse(output_pdf_path, headers={"Content-Disposition": "attachment"})

  except Exception as e:
    logger.error(f"Error durring processing: {e}")
    return sanic.response.text("An error occured durring processing", 500)

  finally:
    os.remove(temp_pdf_path)
    if 'output_pdf_path' in locals():
      os.remove(output_pdf_path)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)

