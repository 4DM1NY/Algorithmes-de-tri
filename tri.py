import time
import random
import matplotlib.pyplot as plt

def tribulle(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def triselection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def triinsertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def trirapide(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return trirapide(left) + middle + trirapide(right)

def trifusion(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = trifusion(left_half)
    right_half = trifusion(right_half)
    return fusion(left_half, right_half)

def fusion(left, right):
    result = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def calcul_execution_time(algo_func, arr_size):
    arr = [random.randint(0, 1000) for _ in range(arr_size)]
    start_time = time.time()
    algo_func(arr)
    end_time = time.time()
    return end_time - start_time

# Listes de tailles différentes pour les tests
sizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000]

# Mesure du temps d'exécution pour chaque algorithme de tri et taille de liste
algos = {
    "Tri à bulle": tribulle,
    "Tri par sélection": triselection,
    "Tri par insertion": triinsertion,
    "Tri rapide": trirapide,
    "Tri fusion": trifusion
}

# Tracé des résultats dans une figure pour chaque algorithme de tri
for algo_name, algo_func in algos.items():
    execution_times = []
    for size in sizes:
        execution_time = calcul_execution_time(algo_func, size)
        execution_times.append(execution_time)

    plt.plot(sizes, execution_times, marker='o', label=algo_name)

plt.title('Temps d\'exécution des algorithmes de tri en fonction de la taille de la liste')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.grid(True)
plt.show()
