def main():
    n = int(input().strip())
    total_sales = 0.0

    for _ in range(n):
        parts = input().split()
        price = float(parts[1])
        quantity = float(parts[2])
        total_sales += price * quantity
    
    average_sales = total_sales / n if n  > 0 else 0.0
    print(f"Average Sales: {average_sales:.1f}")

if __name__ == "__main__":
 main()
