import pandas as pd

# Ścieżki do plików
pliki = ['plik1.xlsx', 'plik2.xlsx', 'plik3.xlsx']

# Nazwa arkusza i kolumny, którą chcesz wczytać
arkusz = 'Arkusz1'
kolumna = 'nazwa_kolumny'

# Lista do przechowywania danych
dane = []

# Wczytaj dane z każdego pliku
for plik in pliki:
    df = pd.read_excel(plik, sheet_name=arkusz, usecols=[kolumna])
    dane.append(df)

# Połącz dane w jeden DataFrame
polaczone = pd.concat(dane, ignore_index=True)

# Zapisz do nowego pliku Excel
polaczone.to_excel('wynik.xlsx', index=False)
