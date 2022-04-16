# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:36:36 2022

@author: maiaw
"""

from fpdf import FPDF
import analyzer 


def report_pdf():
    
    analyzer.extract_temperature()
    analyzer.extract_current()
    analyzer.extract_rssi()
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    # Logo
    pdf.set_xy(30, 10)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(0, 0, " ", 0, 2, 'C')
    pdf.image('python-logo.png', x = 85, y = None, w = 40, h = 35, type = '', link = '')
    
    # Title
    pdf.set_xy(20, 40)
    pdf.set_fill_color(88, 133, 175)
    pdf.cell(170, 10, "Monitoring Report Using Python", 1, 2, 'C', fill=True)

    # Manager
    pdf.set_xy(20, 60)
    pdf.set_font('arial', 'B', 10)
    pdf.cell(65, 10, 'Company: Xablau SA', 1, 0, 'C')
    pdf.cell(65, 10, 'Technical Manager: Wesley', 1, 0, 'C')
    pdf.cell(40, 10, 'Date: 16/04/2022', 1, 2, 'C')

    # Temperature - title
    pdf.set_xy(55, 80)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(100, 10, "Temperature", 0, 2, 'C')

    # Temperature - data
    pdf.set_xy(20, 100)
    pdf.set_font('arial', 'B', 10)
    pdf.cell(50, 10, 'Number of samples:', 1, 0, 'L')
    pdf.set_xy(20, 110)
    pdf.cell(50, 10, 'Temp Max:', 1, 0, 'L')
    pdf.set_xy(20, 120)
    pdf.cell(50, 10, 'Temp Min:', 1, 0, 'L')
    
    # Temperature - figure
    pdf.set_xy(100, 90)
    pdf.image('fig-temperature.png', x = None, y = None, w = 100, h = 75, type = '', link = '')
   
    # Current - title
    pdf.set_xy(55, 170)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(100, 10, "Current", 0, 2, 'C')
    
    # Current- data
    pdf.set_xy(20, 190)
    pdf.set_font('arial', 'B', 10)
    pdf.cell(50, 10, 'Number of samples:', 1, 0, 'L')
    pdf.set_xy(20, 200)
    pdf.cell(50, 10, 'Temp Max:', 1, 0, 'L')
    pdf.set_xy(20, 210)
    pdf.cell(50, 10, 'Temp Min:', 1, 0, 'L')
    
    # Current - figure
    pdf.set_xy(100, 180)
    pdf.image('fig-current.png', x = None, y = None, w = 100, h = 75, type = '', link = '')

    # Footer
    pdf.set_xy(55, 260)
    pdf.set_font('arial', 'B', 10)
    pdf.cell(100, 8, "https://www.iot-report-python.com", 0, 2, 'C')

    pdf.output('report_monitoring.pdf', 'F')
    
    print("Report finished")
    
    
report_pdf()
