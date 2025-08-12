import pandas as pd

# odczytanie konkretnego arkusza
df = pd.read_excel('excel_with_multiple_sheets.xlsx', sheet_name=2)  # indeks 2, arkusz numer 3
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    181
# 2  Darwin    170
# 3    Anna    167

df = pd.read_excel('excel_with_multiple_sheets.xlsx', sheet_name="marks")  # indeks 2, arkusz numer 3
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Marks
# 0  Aditya    179
# 1  Sammer    181
# 2  Darwin    170
# 3    Anna    167

# odcytanie nazw arkuszy, musimy użyc ExcelFile
dane = pd.ExcelFile("excel_with_multiple_sheets.xlsx")
print(dane.sheet_names)  # ['height', 'weight', 'marks']

df = pd.read_excel('excel_with_multiple_sheets.xlsx', sheet_name=dane.sheet_names[0])
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name  Height
# 0  Aditya     179
# 1  Sammer     181
# 2  Darwin     170
# 3    Anna     167

# wczytanie konkretnej kolumny
# usecols=['Name'] - kolumny, które chcemy odczytac
df = pd.read_excel('excel_with_multiple_sheets.xlsx', sheet_name="marks", usecols=['Name'])
print("The dataframe is:")
print(df)
# The dataframe is:
#      Name
# 0  Aditya
# 1  Sammer
# 2  Darwin
# 3    Anna