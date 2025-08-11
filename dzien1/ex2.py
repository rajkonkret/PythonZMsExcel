import openpyxl

# katalog w głownym, wychodzimy z dzien1 i wchodzimy do data
# .. - wyjdz wyzej
wb = openpyxl.load_workbook("../data/videogamesales.xlsx")

print(wb)