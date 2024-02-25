import time
import random
import matplotlib.pyplot as plt

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

def calcul_execution_time(arr_size):
    arr = [random.randint(0, 1000) for _ in range(arr_size)]
    start_time = time.time()
    sorted_arr = trifusion(arr)
    end_time = time.time()
    return end_time - start_time

# Listes de tailles différentes pour les tests
sizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Mesure du temps d'exécution pour chaque taille de liste
execution_times = []
for size in sizes:
    execution_time = calcul_execution_time(size)
    execution_times.append(execution_time)
    print(f"Temps d'exécution pour une liste de taille {size}: {execution_time} secondes")

# Tracé des résultats dans une figure
plt.plot(sizes, execution_times, marker='o', color='yellow', label='Tri fusion')
plt.title('Temps d\'exécution du tri fusion en fonction de la taille de la liste')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (secondes)')
plt.legend()
plt.grid(True)
plt.show()
