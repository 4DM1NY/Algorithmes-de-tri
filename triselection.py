import time
import random
import matplotlib.pyplot as plt

def triselection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def calcul_execution_time(arr_size):
    arr = [random.randint(0, 1000) for _ in range(arr_size)]
    start_time = time.time()
    triselection(arr)
    end_time = time.time()
    return end_time - start_time

# Listes de tailles différentes pour les tests
sizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Mesure du temps d'exécution pour chaque taille de liste
execution_times = []
for size in sizes:
    execution_time = calcul_execution_time(size)
    execution_times.append(execution_time)
   # print(f"Temps d'exécution pour une liste de taille {size}: {execution_time} secondes")

# Tracé des résultats dans une figure
plt.plot(sizes, execution_times, marker='o', color="red", label='Tri par selection')
plt.title('Temps d\'exécution du tri par sélection en fonction de la taille de la liste')
plt.xlabel('Taille de la liste')
plt.ylabel('Temps d\'exécution (s)')
plt.legend()
plt.grid(True)
plt.show()
