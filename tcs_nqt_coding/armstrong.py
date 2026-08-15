"""
Armstrong Number

Input

153 

1³ + 5³ + 3³
= 1 + 125 + 27
= 153

Output

Yes
"""
n = int(input())
power = len(str(n))
sum_of_digits = sum(int(digit) ** power for digit in str(n))
if sum_of_digits == n:
    print("Yes")
else:
    print("No")