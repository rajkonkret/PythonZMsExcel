import pandas as pd

# wstawienie tabeli do arkusza

df = pd.DataFrame({
    "Imie": ['Jan', "Anna", 'Tomek'],
    "Wiek": [29, 24, 35],
    "Miasto": ["Warszawa", "Wrocław", "Legnica"]
})

# kontekst menadżer
with pd.ExcelWriter("Tabela.xlsx", engine="xlsxwriter") as writer:
# with pd.ExcelWriter("Tabela.xlsx") as writer:
    df.to_excel(writer, sheet_name="Osoby", startrow=1, header=False, index=False)

    workbook = writer.book
    worksheet = writer.sheets["Osoby"]

    header_format = workbook.add_format({
        'bold': True,
        "text_wrap": True,
        'valign': '#D7E4BC',
        'border': 1
    })
    # enumerate() - numeruje kolekcje
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    (max_row, max_col) = df.shape  # odczyt rozmiaru tabeli (Dataframa)
    # chr() - znak o kodzie ascii chr(65) to A
    cell_range = f"A1:{chr(65 + max_col - 1)}{max_row + 1}"

    worksheet.add_table(cell_range, {
        'name': "TabelaOsoby",
        "columns": [{"header": col} for col in df.columns]  # kolumny z dataframe
    })
