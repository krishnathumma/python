from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

data = pd.read_csv("topics.csv")
# data = pa.read_csv("data.csv", sep=";")


for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # pdf.line(x1, y1, x2, y2)
    pdf.line(10, 21, 200, 21)

    pdf.output("output.pdf")
