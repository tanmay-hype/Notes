""" binary search """

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return -1
print("Enter the elements of the array in sorted order:")
arr = list(map(int, input().split()))
print ("Enter the target element to search:")
target = int(input())
print("Index of target element:", binary_search(arr, target))