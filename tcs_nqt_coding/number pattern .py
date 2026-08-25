def find_nth_term(n: int) -> int:
    if n % 2 != 0:
        # Odd position: corresponding natural number
        k = (n + 1) // 2
        return k
    else:
        # Even position: corresponding square number
        k = n // 2
        return k * k


def main():
    n = int(input().strip())
    print(find_nth_term(n))


if __name__ == "__main__":
    main()