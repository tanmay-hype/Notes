def reverse_words(sentence):

    words = sentence.split()

    for word_index in range(len(words)):

        word = list(words[word_index])

        left = 0
        right = len(word) - 1

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        words[word_index] = "".join(word)
    return " ".join(words)
sentence = input("Enter a sentence: ")
print(reverse_words(sentence))
