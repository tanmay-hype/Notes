n = int(input())
arr = list(map(int, input().split()))

answer = 0

for num in arr:
    answer = answer ^ num

print(answer)