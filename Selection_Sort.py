# Python 3

# Introduction to Selection Sort

# Selection Sort is not a fast sorting algorithms because it uses
# nested loops to sort.

# It is useful only for small dat sets.

# It runs in O(n^2).

# Here is my Code:


# Define a function:
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Lets consider a example
arr1 = [9, 4, 6, 2, 5, 1]
print('Output : ', selection_sort(arr1))
