"""Reverse Words

Input

TCS is Awesome

Output

Awesome is TCS"""

s = input()
i = len(s) - 1
while i >= 0:
    while i >= 0 and s[i] == ' ':
        i -= 1
    if i < 0:
        break
    end = i
    while i >= 0 and s[i] != ' ':
        i -= 1
    start = i + 1
    for j in range(start, end + 1):
        print(s[j], end='')
    print(' ', end='')
print()