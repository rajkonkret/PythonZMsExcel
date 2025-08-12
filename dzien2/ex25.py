import pandas as pd

df = pd.DataFrame({
    "Imie": ["Ania", "Tomek", "Jan", "Anna", "Jan"],
    "Miasto": ["Kraków", "Warszawa", "Gdańsk", "Kraków", "Gdańsk"],
    "Wynik": [88, 95, 70, 91, 60]
})

df_sorted = df.sort_values(by="Imie")
print(df_sorted)

# malejąco
df_sorted_desc = df.sort_values(by="Imie", ascending=False)
print(df_sorted_desc)

df_sorted_multi = df.sort_values(by=["Miasto", 'Wynik'], ascending=[True, False])
print(df_sorted_multi)

df_grouped_mean = df.groupby("Imie", as_index=False)["Wynik"].mean()
print(df_grouped_mean)

df_grouped_sum = df.groupby("Imie", as_index=False)["Wynik"].sum()
print(df_grouped_sum)

df_grouped_count = df.groupby("Imie").size().reset_index(name="Ilość wpisów")
print(df_grouped_count)

with pd.ExcelWriter('raport.xlsx', engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Oryginalne", index=False)
    df_sorted.to_excel(writer, sheet_name="posortowane", index=False)
    df_grouped_mean.to_excel(writer, sheet_name="Średnia", index=False)