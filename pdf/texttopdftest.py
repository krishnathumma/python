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
    # Set the Header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=12, txt=name, align="L", ln=1)

pdf.output("PDF/final_output.pdf")
