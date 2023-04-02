from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import  BytesIO
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.pagesizes import letter
from .models import *
from reportlab.lib.utils import ImageReader
import urllib
import os
from django.conf import settings



class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFillColor(colors.black)
        if page_count > 1:
            if self._pageNumber != 1: self.line(30, 716, 582, 716) 
            if self._pageNumber != page_count: self.line(30, 81.5, 582, 81.5)
        self.setFont("Helvetica", 10)
        self.drawCentredString(300, 15*mm,
            "Hotel Management System")
        self.drawRightString(580, 15*mm,
            "Page %d of %d" % (self._pageNumber, page_count))
        

class BillPdfGenerator:
    def __init__(self, bill_data, data, table_header, col_width, response) -> None:
        self.bill_data = bill_data
        self.table_data = data
        self.table_header = table_header
        self.col_width = col_width
        self.response = response

    def onFirstPage(self, canvas, document):
        pdf = canvas
    
        # print(logo)
        pdf.drawString(45, 580,
            f"Bill No          :-  {str(self.bill_data['bill_no'])}")
        pdf.drawString(45, 560,
            f"Date & Time :-  {str(self.bill_data['date_time'])}")
        logo = ImageReader('https://res.cloudinary.com/drfdjango/image/upload/v1680432951/hotel_management/media/profile_photos/image_context_unnkdw.jpg')
        pdf.drawImage(logo, 215, 670, width=200, height=100)
        pdf.setLineWidth(2)
        pdf.line(40, 650, 580, 650)
        pdf.setLineWidth(1)
        pdf.line(40, 645, 580, 645)
        pdf.setFont("Helvetica", 18)
        
       
        

    def main(self):

        buffer = BytesIO()

        menu_pdf = SimpleDocTemplate(buffer, pagesize=letter)
       
        
        t = Table([self.table_header] + self.table_data, colWidths=self.col_width)
        ts = TableStyle([
                        ("GRID", (0,0), (-1,-1), 2, colors.black),
                        ('BACKGROUND',(0,0),(0,0),colors.limegreen),
                        ('BACKGROUND',(1,0),(len(self.table_header),0),colors.limegreen),
                        ('BOX',(0,0),(-1,-1),2,colors.black)
                        ]
                        )
        t.setStyle(ts)
       
        elements = []
        elements.append(Spacer(7 * cm, 7 * cm))
        elements.append(t)
       
        menu_pdf.build(elements, onFirstPage=self.onFirstPage, canvasmaker=NumberedCanvas)
        self.response.write(buffer.getvalue())
        buffer.close()

        return self.response