"""Second Largest Element

Input

6

5 8 2 10 3 9

Output

9"""

print("Second Largest Element\n")
n = int(input())
print("Input")
arr = list(map(int, input().split()))
if len(arr) != n:
    exit()
largest = float('-inf')
#this will store the largest element in the array
second_largest = float('-inf')
#this will store the second largest element in the array
for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest)