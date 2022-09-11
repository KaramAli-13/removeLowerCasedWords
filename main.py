# Q1 - Case Sensitive
def main():
    sentence = " ".join(case_checker(word_splitter(input("Please enter a sentence: "))))
    return sentence


def word_splitter(word):
    return case_checker(word.split())


def case_checker(split_words):
    words_with_capitals = []
    for word in split_words:
        if word[0].isupper():
            words_with_capitals.append(word)
    return words_with_capitals


main()
