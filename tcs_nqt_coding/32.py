"""
Move all zeros to the end (Chocolate Factory / Conveyor Belt problem)

Problem: Given an array, push all 0s to the end while maintaining the relative order of non-zero elements. Example: [4,5,0,1,9,0,5,0] → [4,5,1,9,5,0,0,0]
"""

def move_zeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

n = int(input())
arr = [int(input()) for _ in range(n)]
print(*move_zeros(arr))