""" anagram """

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
str1 = input()
str2 = input()
if is_anagram(str1, str2):
    print("Anagram")
else:
    print("Not Anagram")