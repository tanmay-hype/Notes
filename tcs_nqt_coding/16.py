""" Armstrong """

def power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result
n = int(input())
original = n
count = 0
temp = n 
while temp > 0:
    count += 1
    temp //= 10
armstrong_sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    armstrong_sum += power(digit, count)
    temp //= 10
if armstrong_sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")