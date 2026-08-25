def count_characters(text: str):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    space_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
        elif char == " ":
            space_count += 1

    return vowel_count, consonant_count, space_count

def main():
    text = input("Enter a string: ")
    vowels, consonants, spaces = count_characters(text)
    print(f"Vowels: {vowels}, Consonants: {consonants}, Spaces: {spaces}")  

if __name__ == "__main__":
    main()