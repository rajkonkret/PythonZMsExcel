import pandas as pd

data = pd.read_excel("course_participants.xlsx")
print(data)
#    numer   imię  wiek    kraj  ocena kontynent
# 0   1001   Mark    55  Włochy    4.5    Europa
# 1   1000   John    33     USA    6.7   Ameryka
# 2   1002    Tim    41     USA    3.9   Ameryka
# 3   1003  Jenny    12  Niemcy    9.0    Europa

data.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   numer      4 non-null      int64
#  1   imię       4 non-null      object
#  2   wiek       4 non-null      int64
#  3   kraj       4 non-null      object
#  4   ocena      4 non-null      float64
#  5   kontynent  4 non-null      object
# dtypes: float64(1), int64(2), object(3)
# memory usage: 324.0+ bytes

data = [["Mark", 55, "Włochy", 4.5, "Europa"],
        ["John", 33, "USA", 6.7, "Ameryka"],
        ["Tim", 41, "USA", 3.9, "Ameryka"],
        ["Jenny", 12, "Niemcy", 0.0, "Europa"],
        ]

df = pd.DataFrame(data=data,
                  columns=["imie", "wiek", "kraj", "ocena", "kontynent"],
                  index=[1001, 1000, 1002, 1003])

print(df)
#        imie  wiek    kraj  ocena kontynent
# 1001   Mark    55  Włochy    4.5    Europa
# 100    John    33     USA    6.7   Ameryka
# 1002    Tim    41     USA    3.9   Ameryka
# 1003  Jenny    12  Niemcy    0.0    Europa

print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# Index: 4 entries, 1001 to 1003
# Data columns (total 5 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   imie       4 non-null      object
#  1   wiek       4 non-null      int64
#  2   kraj       4 non-null      object
#  3   ocena      4 non-null      float64
#  4   kontynent  4 non-null      object
# dtypes: float64(1), int64(1), object(3)
# memory usage: 192.0+ bytes

# wypisanie co jest indexem w arkuszu
print(df.index)  # Index([1001, 100, 1002, 1003], dtype='int64')
# nadanie nazwy dla indexu
df.index.name = "numer"
print(df)

# reset dla indexu
df.reset_index()
print(df)
# 1003   Jenny    12  Niemcy    0.0    Europa
#         imie  wiek    kraj  ocena kontynent
# numer
# 1001    Mark    55  Włochy    4.5    Europa
# 1000    John    33     USA    6.7   Ameryka
# 1002     Tim    41     USA    3.9   Ameryka
# 1003   Jenny    12  Niemcy    0.0    Europa

df.reset_index().set_index("imie")
df.reindex([999, 1000, 1001, 1004])
df.sort_index() # sortowanie indeksu
print(df)

# sortowanie danych
print(df.sort_values(["kontynent", "wiek"]))
# numer
# 1000    John    33     USA    6.7   Ameryka
# 1002     Tim    41     USA    3.9   Ameryka
# 1003   Jenny    12  Niemcy    0.0    Europa
# 1001    Mark    55  Włochy    4.5    Europa