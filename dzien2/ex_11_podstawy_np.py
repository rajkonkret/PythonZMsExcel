import math

import numpy as np

# numpy zostało zainstalowane przez pandas
# pip install numpy

# ndarray - tablice, macierze
array = np.array([10, 100, 1000.])
print(array)  # [  10.  100. 1000.] kropka oznacza float

array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(array2)
# [[1 2 3]
#  [4 5 6]]
print(array2.dtype)  # int64 typ danych
print(array.dtype)  # float64

# rzutowanie na float pythonowy
print(float(array[0]))  # 10.0
print(type(float(array[0])))  # <class 'float'>

# json - dane typu klucz-wartosc, słownik
import json

# do obliczen potrzebowalismy tablice numpy
x = np.int64(42)
print(type(x))  # <class 'numpy.int64'>

# serializacja - zamiana danych na json
# json.dumps("value": x) # TypeError: dumps() takes 1 positional argument but 2 were given
# serializacja nie przyjmuje typów z numpy
# musimy zamienic na typ pythonowy
python_int = int(x)  # całkowite
print(type(python_int))  # <class 'int'> pythonowy int
json_str = json.dumps({"value": python_int})
print(json_str)  # {"value": 42} z typów pythonowych da sie zrobić jsona

# broadcasting
# rozgłaszanie i wektoryzacja obliczen
# [[1 2 3]
#  [4 5 6]]
print(array2 + 1)
# [[2 3 4]
#  [5 6 7]]

print(array2 * array2)
# [[ 1  4  9]
#  [16 25 36]]

# pierwiastek
# print(math.sqrt(array2)) # TypeError: only length-1 arrays can be converted to Python scalars

# numpy posiada swoje metody do tego działajaće z danymi typu numpy
print(np.sqrt(array2))
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]

# sumowanie wszystkich eleemntów macierzy
print(array2.sum())  # 21
