import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

files = glob.glob("textfiles/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for file in files:
    pdf.add_page()

    filename = Path(file).stem
    name = filename.title()

    with open(file, 'r') as book:
        content = book.read()

    # Set the Header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=12, txt=name, align="L", ln=1)

    # Set the Body
    pdf.set_font(family="Times", style="I", size=10)
    pdf.multi_cell(w=0, h=10, txt=content)

pdf.output("PDF/final_output.pdf")
