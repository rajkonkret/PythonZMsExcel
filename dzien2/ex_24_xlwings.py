# xlwings - praca z plikami excel, wymaga excela w systemie !!!
import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.randn(100, 5),
                  columns=[f"Próba {i}" for i in range(1, 6)])

print(df)
print(df.head())  # pięć pierwszych
print(df.tail())  # pięć ostatnich
#      Próba 1   Próba 2   Próba 3   Próba 4   Próba 5
# 95 -1.363015  0.771833 -0.857463 -1.074409 -0.457788
# 96  0.921857  0.774228 -0.267045  0.112779 -1.205598
# 97 -0.545419 -0.633828  0.509880 -1.665996  0.392408
# 98  1.534107  1.362831 -1.229998 -1.859633  0.305683
# 99 -1.693275  1.419422  0.679595  0.822421  0.251229

# xw.view(df)  # wyswietlenie arkusza w excelu

book = xw.Book(visible=True)
print(book.name)
print(book.sheets)  # Sheets([<Sheet [Zeszyt2]Arkusz1>])

sheet1 = book.sheets[0]  # pierwszy arkusz z excela
print(sheet1.range('A1'))  # <Range [Zeszyt2]Arkusz1!$A$1>

sheet1.range('A1').value = [[1, 2],
                            [3, 4]]

sheet1.range('A4').value = "Witaj"

print(sheet1['A1'].value)  # 1.0

print(sheet1['A1:B2'].value)
# [[1.0, 2.0], [3.0, 4.0]]
