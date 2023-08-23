from collections import Counter


# Count words in the text
def count(text):
    return len(text.split())


# Count characters in the text
def char_counter(text):
    return Counter([c for c in text.lower() if c.isalpha()])


with open("books/frankenstein.txt") as f:
    text = f.read()
    counter = char_counter(text)

    for char, count in counter.most_common():
        print(f"The '{char}' character was found {count} times.")
