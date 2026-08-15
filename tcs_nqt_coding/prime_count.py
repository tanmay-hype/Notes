"""Prime Count

Input

20

Output

8

Primes

2
3
5
7
11
13
17
19"""

def prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


n = int(input())
primes = []

for i in range(2, n + 1):
    if prime(i):
        primes.append(i)

print(f"Number of primes: {len(primes)}")
print("Primes")

for i in primes:
    print(i)