def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break 
    return arr

def main():
    n =  int(input().strip())
    arr = list(map(int, input().split()))
    sorted_arr = bubble_sort(arr)
    print(*(sorted_arr))

if __name__ == "__main__" :
    main()