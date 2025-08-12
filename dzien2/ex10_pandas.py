# pandas - biblioteka do przetwarzania i wizualizacji danych
import pandas as pd  # pd to alias

#  pip install pandas

# tworzymy tabelki (w pamięci)
writer = pd.ExcelWriter('empty_file.xlsx')
empty_dataframe = pd.DataFrame()  # tablice/macierze w pandasie(pythonie)

# zapisujemy do pliku excel
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()  # jak uzywamy excelwriter musi byc close()
