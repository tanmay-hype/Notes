def digital_root(n: int) -> int:
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def digital_root_iterative(n: int)-> int:
    while n >= 10:
        n =  sum(int(digit)for digit in str(n))
    return n 

def main():
    n = int(input().strip())
    print(digital_root(n))
    print(digital_root_iterative(n))

if __name__ == "__main__":
    main()