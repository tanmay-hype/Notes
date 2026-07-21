"""Input
12345678
Output
8642"""

num = int(input())
reverse_even = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        reverse_even = reverse_even * 10 + digit
    num //= 10
print(reverse_even)