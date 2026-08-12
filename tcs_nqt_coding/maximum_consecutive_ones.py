"""Maximum Consecutive Ones

Input

1 1 0 1 1 1 0 1

Output

3"""

arr = list(map(int, input().split()))

if len(arr) == 0:
    print(0)
else:
    current = arr[0]
    count = 1
    max_count = 1

    for i in range(1, len(arr)):
        if arr[i] == current:
            count += 1
        else:
            current = arr[i]
            count = 1

        if count > max_count:
            max_count = count

    print(max_count)