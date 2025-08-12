import openpyxl

wb = openpyxl.load_workbook('video2.xlsx')

ws = wb['vgsales']

ws['P1'] = 'Average Sales'
# ws['P2'] = '= AVERAGE(K2:K16199)'
ws['P2'] = '= AVERAGE(L2:L16199)'  # =ŚREDNIA(L2:L16199)

wb.save('video2.xlsx')
wb.close()

ws['Q1'] = 'Number of populated cells'
ws['Q2'] = "=COUNTA(E2:E16220)"

wb.save('video2.xlsx')
wb.close()
