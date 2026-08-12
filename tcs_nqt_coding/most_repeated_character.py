"""Most Repeated Character

Input

programming

Output

g"""

s = input()
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_freq = 0
max_char = ''
for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]
        max_char = ch

print(max_char)