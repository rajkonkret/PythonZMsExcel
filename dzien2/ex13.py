import pandas as pd

# pip install xlsxwriter

data = [
    ["Adiya", 179],
    ["Samen", 181],
    ["Darek", 170],
    ["Jhon", 167],
]

column_names = ['Name', "Height"]
df = pd.DataFrame(data, columns=column_names)
writer = pd.ExcelWriter("excel_with_list.xlsx", engine='xlsxwriter')

# df.to_excel(writer)
# df.to_excel(writer, index=False) # bez indeksu
# df.to_excel(writer, sheet_name='first_sheet', index=False) # nadanie nazwy arkuszowi
# df.to_excel(writer, sheet_name='first_sheet', index=False, startrow=3) # start od wiersza 3
df.to_excel(writer, sheet_name='first_sheet', index=False, startrow=3, startcol=4)  # start od wiersza 3, kolumny 4
writer.close()
