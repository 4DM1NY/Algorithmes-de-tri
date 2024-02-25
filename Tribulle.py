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

def calcul_execution_time(arr_size):
    arr = [random.randint(0, 1000) for _ in range(arr_size)]
    start_time = time.time()
    tribulle(arr)
    end_time = time.time()
    return end_time - start_time

# Listes de tailles différentes pour les tests
sizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Mesure du temps d'exécution pour chaque taille de liste
execution_times = []
for size in sizes:
    execution_time = calcul_execution_time(size)
    execution_times.append(execution_time)
 #   print(f"Temps d'exécution pour une liste de taille {size}: {execution_time} secondes")

# Tracé des résultats dans une figure
plt.plot(sizes, execution_times, marker='o', color="green", label='Tri à bulle')
plt.title('Temps d\'exécution du tri à bulle en fonction de la taille de la liste')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.grid(True)
plt.show()
