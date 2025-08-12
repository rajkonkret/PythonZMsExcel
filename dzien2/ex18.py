import time
import numpy as np

lista = list(range(15_000_000))
lista_np = np.arange(15_000_000, dtype=np.int64)


# deklaracja funkcji
def sum_python():
    total = 0
    for i in lista:
        total += i
    print("Sum is:", total)


def sum_np():
    total = np.sum(lista_np)
    print("Sum is:", total)


# żeby funkcja zadziałała musi zostac wywołana
start_d = time.time()
# wywołanie funkcji
sum_python()
end_d = time.time()
print(end_d - start_d)

start_d = time.time()
# wywołanie funkcji
sum_np()
end_d = time.time()
print(end_d - start_d)
# Sum is: 112499992500000
# 0.49601316452026367
# Sum is: 112499992500000
# 0.010054349899291992