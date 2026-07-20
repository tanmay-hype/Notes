"""Count Frequency of Elements

Input

7
1 2 2 3 4 4 4

Output

1 ->1
2 ->2
3 ->1
4 ->3"""

print("Count Frequency of Elements\n")
n = int(input())
print("Input")
arr = list(map(int, input().split()))
if len(arr) != n:
    print("Error: The number of elements does not match the specified count.")
    exit()
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
    
    """this will count the frequency of each element
    in the array and store it in a dictionary called
    freq. The keys of the dictionary will be the 
    unique elements from the array, and the 
    values will be their corresponding frequencies."""

for key in sorted(freq.keys()):
    print(f"{key} -> {freq[key]}")