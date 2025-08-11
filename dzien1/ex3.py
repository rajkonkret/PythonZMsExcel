import openpyxl

wb = openpyxl.load_workbook('video2.xlsx')
ws = wb.active

# wybranie konkretnego arkusza
ws = wb['vgsales']

row_position = 2
col_position = 7

total_sales = ((ws.cell(row=row_position, column=col_position).value)
               + (ws.cell(row=row_position, column=col_position + 1).value)
               + (ws.cell(row=row_position, column=col_position + 2).value)
               + (ws.cell(row=row_position, column=col_position + 3).value)
               )


