def decimal_to_binary(n: int) ->str:
    if n==0:
        return "0"

    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(digits))

def main():
    n = int(input().strip())
    print(decimal_to_binary(n))

if __name__ == "__main__":
    main()
    