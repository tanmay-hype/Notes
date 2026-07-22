"""
Input

998979999

Largest digit = 9

Frequency = 7

Output

7"""

num = int(input())
temp = num
largest = -1
while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp //= 10
count = 0
while num > 0:
    digit = num % 10
    if digit == largest:
        count += 1
    num //= 10
print(count)