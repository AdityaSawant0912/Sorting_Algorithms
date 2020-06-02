# Python 3

# Introduction to Insertion Sort

# Insertion Sort is not a fast sorting algorithms because it uses
# nested loops to sort.

# It is useful only for small dat sets.

# It runs in O(n^2).

# Here is my Code:


# Define a function:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while arr[j] > arr[j+1] and j >= 0:
            arr[j], arr[j + 1] = arr[j+1], arr[j]
            j -= 1

    return arr


# Lets consider a example
arr1 = [9, 4, 6, 2, 5, 1]
print('Output : ', insertion_sort(arr1))

