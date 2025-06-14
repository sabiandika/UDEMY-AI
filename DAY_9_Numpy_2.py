import numpy as np

# Define the function to calculate the sum of squares of differences between two arrays
arr = np.array([1, 2, 3])
print(arr + 10)

matrix = np.array([1, 2, 3]), ([4, 5, 6])
vector = np.array([1, 0, 1]) 
print(matrix + vector) #cara hitungnya 1+1, 2+0, 3+1 yang samping juga 4+1, 5+0, 6+1
# Output: [[2, 1, 4], [5, 5, 7]]

arr = np.array([1, 2, 3, 4, 5, 6,])

evens = arr[arr % 2 == 0]
print(evens) # Output: [2, 4, 6]

arr[arr > 3] = 0
print ("udah diganti: ", arr) #anga yang lebih dari 3 akan beruabah jadi 0

#np random

random_array = np.random.rand(3, 4)  # Membuat array 2D acak dengan 3 baris dan 4 kolom
print("Array acak:\n", random_array)

random_integers = np.random.randint(0, 10, size=(2,3))  # Membuat array 2D acak dengan bilangan bulat antara 0 dan 10 
print("Array bilangan bulat:\n", random_integers)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, -1])

result = matrix + vector 
print("hasil penjumlahan:\n", result)  # Penjumlahan matriks dengan vektor
# Output: [[2, 2, 2], [5, 5, 5], [8, 8, 8]] 

result_kali = matrix * 2
print("hasil perkalian:\n", result_kali)  # Perkalian matriks dengan skalar
# Output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]