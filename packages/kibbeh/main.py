import openai
from pdfminer.high_level import extract_text
from fpdf import FPDF
from io import StringIO
import spacy

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

def main():
  text = read_pdf("test.pdf")
  summary = summarize(text)
  write_pdf("outputted.pdf", "Summarized File", summary)

main()
