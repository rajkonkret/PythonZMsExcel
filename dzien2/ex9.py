import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule

wb = openpyxl.load_workbook('video2.xlsx')
ws = wb.active

ws = wb['Video Games Sales Data']
