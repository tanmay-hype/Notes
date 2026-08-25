def find_smallest(arr: list[int]) -> int:
    if not arr:
        return 0

    min_val =arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(find_smallest(arr))

if __name__ == "__main__":
    main()