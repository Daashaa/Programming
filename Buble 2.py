def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            alg_count [0] += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                alg_count[1] += 1
import timeit
a = timeit.default_timer()
import random
DIM = 20
arr = [random.randint(0, 100) for i in range(DIM)]
print(arr)
alg_count = [0, 0]
bubble_sort(arr)
print(arr)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
print(timeit.default_timer()-a)
