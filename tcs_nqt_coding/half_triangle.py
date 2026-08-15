""" pattern printing """
def print_pattern(n):
    for i in range(1, n + 1):
        print(''.join(str(j) for j in range(1, i + 1)))
n = int(input())
print_pattern(n)