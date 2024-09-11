from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")
# data = pa.read_csv("data.csv", sep=";")


for index, row in data.iterrows():
    pdf.add_page()

    # Set the Header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # add lines into page
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    # pdf.line(x1, y1, x2, y2)
    # pdf.line(10, 21, 200, 21)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # add lines into page
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # set footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("output.pdf")
