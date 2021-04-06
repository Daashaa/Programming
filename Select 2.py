def selection_sort(arr):        
    for i in range(0, len(arr) - 1):
        s = i
        alg_count[0] += 1
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[s]:
                s = j
                alg_count[1] += 1
        arr[i], arr[s] = arr[s], arr[i]
import timeit
a = timeit.default_timer()
import random
DIM = 20
arr = [random.randint(0, 100) for i in range(DIM)]
print(arr)
alg_count = [0, 0]
selection_sort(arr)  
print(arr)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
print(timeit.default_timer()-a)
