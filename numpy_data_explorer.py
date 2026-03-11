# NumPy Data Explorer
import numpy as np
import time
print("----- NumPy Data Explorer -----")

# 1. Array Creation
print("\n1. ARRAY CREATION")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.arange(1, 10)
arr3 = np.random.randint(1, 100, (3,3))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Random 3x3 Array:\n", arr3)

# 2. Indexing and Slicing
print("\n2. INDEXING AND SLICING")
print("First element:", arr1[0])
print("Last element:", arr1[-1])
print("Slice (1:4):", arr1[1:4])

# 3. Mathematical Operations
print("\n3. MATHEMATICAL OPERATIONS")
print("Addition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square Root:", np.sqrt(arr1))

# 4. Statistical Operations
print("\n4. STATISTICAL OPERATIONS")
print("Mean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))
print("Sum:", np.sum(arr1))

# Axis wise operation
print("Column Sum:\n", np.sum(arr3, axis=0))
print("Row Sum:\n", np.sum(arr3, axis=1))

# 5. Reshaping
print("\n5. RESHAPING")
arr4 = np.arange(1,13)
reshaped = arr4.reshape(3,4)
print("Original:", arr4)
print("Reshaped (3x4):\n", reshaped)

# 6. Broadcasting
print("\n6. BROADCASTING")
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([10,20,30])
result = matrix + vector
print("Matrix:\n", matrix)
print("Vector:", vector)
print("Broadcasted Result:\n", result)

# 7. Save and Load Arrays
print("\n7. SAVE AND LOAD NUMPY ARRAY")
np.save("saved_array.npy", arr3)
loaded_array = np.load("saved_array.npy")
print("Loaded Array:\n", loaded_array)

# 8. Performance Comparison (NumPy vs Python List)
print("\n8. PERFORMANCE COMPARISON")
size = 1000000

# Python list
list1 = list(range(size))
start = time.time()
list_result = [x + 5 for x in list1]
end = time.time()
print("Python List Time:", end - start)

# NumPy array
np_array = np.arange(size)
start = time.time()
np_result = np_array + 5
end = time.time()
print("NumPy Array Time:", end - start)
print("\nNumPy is faster for large computations!")