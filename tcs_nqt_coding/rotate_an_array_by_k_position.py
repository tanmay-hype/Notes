""" rotate an array left by k postion """
def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k is larger than the array size
    return arr[k:] + arr[:k]

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_left(arr, k))  # Output: [3, 4, 5, 1, 2]