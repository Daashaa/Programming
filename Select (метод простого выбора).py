import timeit
a = timeit.default_timer()
import random
DIM = 20
arr = [random.randint(0, 100) for i in range(DIM)]
print("Исходный массив")
print(arr)
k = 0
alg_count = [0, 0]
for k in range(0, DIM - 1): 
    m = k  
    i = k + 1  
    for i in range(i, DIM):
        alg_count[0] += 1
        if arr[i] < arr[m]:
            m = i
    if k != m:
        t = arr[k]
        arr[k] = arr[m]
        arr[m] = t
        alg_count[1] += 1
print("\nУпорядоченный массив: метод простого выбора")
print(arr)
print("\nЭлементов в массиве: ", DIM)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
print(timeit.default_timer()-a)
