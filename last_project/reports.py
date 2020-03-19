#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os

def generate_report(filename, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)
    structure = [report_title]
    for line in paragraph:
        structure.append(empty_line)
        new_paragraph = Paragraph(line, styles["BodyText"])
        structure.append(new_paragraph)
    report.build(structure)