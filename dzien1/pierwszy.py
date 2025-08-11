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

# type() - sprawdzenie typu danych
print(type(45))  # <class 'int'>, liczby całkowite
# zakres liczb całkowitych w pythonie
print(sys.int_info)

# ctrl / - komentarz
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)

# liczby zmiennoprzecinkowe
# float
print(4.56)  # 4.56
print(type(4.56))  # <class 'float'> liczby zmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024, max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021, min_10_exp=-307,
#                dig=15, mant_dig=53, epsilon=2.220446049250313e-16,
#                radix=2, rounds=1)

# bład zaokraglenia
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.9)  # 1.0

# zmienna - pudełko na dane

zmienna = 90
name = "Radek"
print(type(name))  # sprawdzenie typu zmiennej, <class 'str'>
# typowanie dynamiczne

name = 90  # int
print(name)  # 90
print(type(name))  # <class 'int'>

# hint - podpowiedzi (dla programisty)
name: str = "Radek"
name = 90
print(name)

# rzutowanie - zamiana na własciwy typ
a = "1"
b = 0
# print(a + b) # TypeError: can only concatenate str (not "int") to str
# int() - rzutowanie na int
# zamieniamy na liczby by wykonać matematyczne działanie
print(int(a) + int(b))  # 1

tekst = "Witaj Świecie"
print(tekst)

# teksty są niemutowalne
#  """ Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE, wypisało, nie zapamiętało zmian
nowy_tekst = tekst.upper()  # zapamiętanie zmiany w nowej zmiennej
print(nowy_tekst)  # wypisanie zmiany z tej zmiennej, WITAJ ŚWIECIE

zmienna1 = "GROSS"
zmienna2 = "groẞ"
