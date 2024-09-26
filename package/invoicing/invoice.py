import glob
import os

import pandas as pd
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, product_id, product_name,amount_purchased,
             price_per_unit, total_price):
    """

    """
    files = glob.glob(f"{invoices_path}/*.xlsx")

    for file in files:
        data = pd.read_excel(file, sheet_name="Sheet 1")

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.add_page()

        filename = Path(file).stem
        invoice_nr = filename.split("-")[0]
        date = filename.split("-")[1]

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Invoice nr - {invoice_nr}", ln=1)

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

        data = pd.read_excel(file, sheet_name="Sheet 1")

        # Add Table Header
        columns_data = list(data.columns)
        # no_of_hear = len(columns_data)

        columns_data = [item.replace("_", " ").title() for item in columns_data]
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=columns_data[0], border=1)
        pdf.cell(w=70, h=8, txt=columns_data[1], border=1)
        pdf.cell(w=30, h=8, txt=columns_data[2], border=1)
        pdf.cell(w=30, h=8, txt=columns_data[3], border=1)
        pdf.cell(w=30, h=8, txt=columns_data[4], border=1, ln=1)
        for index, row in data.iterrows():
            pdf.set_font(family="Times", style="I", size=12)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)

        total_sum = data["total_price"].sum()
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

        # Add Total Price
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=30, h=8, txt=f"Total Price is {total_sum}", ln=1)

        # Add Company Logo
        pdf.set_font(family="Times", style="B", size=10)
        pdf.cell(w=30, h=8, txt=f"Python")
        # pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")
