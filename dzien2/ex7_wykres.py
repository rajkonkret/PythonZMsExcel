from multiprocessing.managers import BarrierProxy

import openpyxl
from openpyxl.chart import Reference, BarChart

wb = openpyxl.load_workbook('video2.xlsx')
ws = wb['Total Sales by Genre']

# wycinamy dane z excela potrzebne do wykresu
values = Reference(ws,
                   min_col=2,
                   max_col=2,
                   min_row=1,
                   max_row=13)

cats = Reference(ws,
                 min_col=1,
                 max_col=1,
                 min_row=2,
                 max_row=13)

# tworzenie wykresu, słupkowy
chart = BarChart()
chart.add_data(values, titles_from_data=True)
chart.set_categories(cats)
chart.title = "Total Sales"
chart.x_axis.title = "Genre"
chart.y_axis.title = "Total Sales by Genre"
ws.add_chart(chart, "D2")  # umiesczenie wykresu w komórce D2

wb.save('video2.xlsx')
wb.close()
