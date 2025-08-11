# PEP8
# import bilioteki - dołaczenie do naszego pliku
import sys

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu

print("Radek")
print('Radek')

# ctrl / - szybki komentarz
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\PythonZMsExcel\dzien1\pierwszy.py", line 7
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 7)
# Radek
# Radek

# wypisanie typu danych
print(type("Radek"))  # <class 'str'>, dane typu tekstowego
print("34" + "90")  # 3490, złączenie tekstów, konkatenacja

print(34 + 19)  # 53
print(type(45))  # <class 'int'>, liczby całkowite
# zakres liczb całkowitych w pythonie
print(sys.int_info)

# ctrl / - komentarz
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
