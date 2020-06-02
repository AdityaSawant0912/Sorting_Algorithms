# Python 3

# Introduction to Merge Sort

# Merge Sort is recursive (method that calls itself)

# Divide-and-conquer algorithm.

# Very efficient for large data sets.

# Merge Sort does log n merge steps because each merge step
# doubles the arrst size.

# It does n work for each merge step because it must look at
# every item.

# It runs in O(n*logn).

# Here is my code:


# Define a Recursive function:
def merge(left, right):
    sorted_otp = [] 
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_otp.append(left[i])
            i += 1
        else:
            sorted_otp.append(right[j])
            j += 1

    sorted_otp += left[i:]
    sorted_otp += right[j:]
    return sorted_otp


# Define Main Function:
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])
    return merge(left_arr, right_arr)


# Lets consider a example
arr1 = [9, 4, 6, 2, 5, 1, 3, 7]
print('Output : ', merge_sort(arr1))
