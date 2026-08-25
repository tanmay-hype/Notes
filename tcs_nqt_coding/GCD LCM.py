def gcd(a: int, b: int) -> int:
    while b:
        a,b = b, a % b
    return a 

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def main():
    a,b = map(int, input("Enter two numbers separated by space: ").split())

    print(f"GCD of {a} and {b} is: {gcd(a,b)}")
    print(f"LCM of {a} and {b} is: {lcm(a,b)}")

if __name__ == "__main__":
    main()