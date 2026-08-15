"""
Input

4582

Output

19 (digit sum)
"""

num = int(input())
digit_sum = 0
count = 0
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
    count += 1
print(digit_sum)
print(digit_sum // count)