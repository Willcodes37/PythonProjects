from fpdf import FPDF

name = input("Name: ")
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=45)
pdf.cell(w=0, txt="CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=10, y=60, w=pdf.epw)
pdf.set_font('helvetica', size=25)
pdf.set_text_color(r=255, g=255, b=255)
pdf.text(x=60, y=130, txt=f'{name} took CS50')
pdf.output("shirtificate.pdf")
