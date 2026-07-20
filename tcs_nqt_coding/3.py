"""Move all Zeroes to End

Input

1 0 4 0 6 8 0

Output

1 4 6 8 0 0 0"""

print("Move all Zeroes to End\n")
arr=list(map(int,input().split()))
j=0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[i],arr[j]=arr[j],arr[i]
        #this will swap the current element with the element at index j
        j+=1
print(*arr)