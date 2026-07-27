""" largest sum contiguous subarray (Kadane's Algorithm) """
def max_subarray_sum(arr):
    curr = best = arr[0]
    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        best = max(best, curr)
    return best 
arr=list(map(int,input().split()))
print(max_subarray_sum(arr))
