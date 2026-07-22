"""Input

583214

Output

8"""

n =int(input())
largest = n % 10
n = n // 10
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 10
print(largest)