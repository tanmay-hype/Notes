""" reverse number """

rev = 0 
n = int(input())
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)
