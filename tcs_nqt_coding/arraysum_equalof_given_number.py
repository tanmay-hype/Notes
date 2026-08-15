""" pairs in an array whose sum is equal to a given number """
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))      
    return pairs
arr = list(map(int, input().split()))
target_sum = int(input())
print(find_pairs(arr, target_sum))