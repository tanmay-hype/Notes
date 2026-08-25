def length_of_longest_substring(s: str) -> int:
    char_map = {}  # stores the last seen index of each character
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If character was seen inside the current window, slide left boundary
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1

        # Update last seen index of character
        char_map[char] = right

        # Update max length found so far
        max_len = max(max_len, right - left + 1)

    return max_len


def main():
    s = input().strip()
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()