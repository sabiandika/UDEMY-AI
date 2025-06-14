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