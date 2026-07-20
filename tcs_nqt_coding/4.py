"""Find Missing Number

Input

5

1 2 4 5

Output

3"""

print("Find Missing Number\n")
n = int(input())
print("Input")
arr = list(map(int, input().split()))
if len(arr) != n-1:
    print("Invalid input")
    exit()
s = sum(arr)
total = n*(n+1)//2
print(total - s)