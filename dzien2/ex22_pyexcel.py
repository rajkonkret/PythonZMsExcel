import pyexcel

# pip install pyexcel pyexcel-xlsx

data = [
    ["Imię", "Wiek"],
    ["Tomek", 38],
    ["Kasia", 28],
]

sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')

# wczytanie arkusza
sheet = pyexcel.get_sheet(file_name="wyniki.xlsx")
print(sheet)
# pyexcel sheet:
# +-------+------+
# | Imię  | Wiek |
# +-------+------+
# | Tomek | 38   |
# +-------+------+
# | Kasia | 28   |
# +-------+------+
