# Python 3

# Introduction to Insertion Sort

# Insertion Sort is not a fast sorting algorithms because it uses
# nested loops to sort.

# It is useful only for small dat sets.

# It runs in O(n^2).

# Here is my Code:


# Define a function:
def bubble_sort(arr):
    for i in range(0 , len(arr) - 1):
        for j in range(0, len(arr) -1 - i):
            if arr[j] > arr [j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr [j]
    return arr


# Lets consider a example
arr1 = [9, 4, 6, 2, 5, 1]
print('Output : ', bubble_sort(arr1))

