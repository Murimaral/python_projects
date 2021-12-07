#!/usr/bin/env python3

fruits = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("./report.pdf")
### created the pdf object

from reportlab.platypus import Paragraph, Spacer, Table, Image
### Flowables of the document >> PArts to be joined at the endmaking the entire pdf doc

from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
### this module describes the styles

### START
### Paragraph
report_title = Paragraph("A Complete Inventory of Fruit", styles["h1"])

### Table >> list of lists
table_contents = []
for fruit, quant in fruits.items():
  table_contents.append([fruit, quant])

### Styles
from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_contents, style=table_style, hAlign="LEFT")

### Graphics
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=6, height=6) # criar o objeto PIE
report_pie.data = [] 
report_pie.labels = []
for fruit in sorted(fruits):  # atribuir dados e rotulos no objeto PIE
  report_pie.data.append(fruits[fruit])
  report_pie.labels.append(fruit)

report_chart = Drawing() # instanciaçao do chart (pode ter varios objetos de gráfico)
report_chart.add(report_pie) # adicionar o objeto pie
### SEE FINAL PDF
report.build([report_title, report_table, report_chart])
