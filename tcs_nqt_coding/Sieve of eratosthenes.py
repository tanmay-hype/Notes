def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return[]

    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p*p, n+1, p):
                is_prime[multiple] = False
        p += 1

    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes

def main():
    n = int(input().strip())
    primes = sieve_of_eratosthenes(n)
    print(*(primes))

if __name__ == "__main__" :
    main()

