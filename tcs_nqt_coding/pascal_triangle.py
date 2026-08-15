""" print pascals triangle """
def print_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [0]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)))

n = int(input())
print_pascals_triangle(n)