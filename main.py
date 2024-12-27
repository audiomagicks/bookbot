def main():
    book_path = "books/frankenstein.txt"
    book_string = read_full(book_path)
    num_words = wordcount(book_string)
    char_dict = letter_freq(book_string)
    print(f"{num_words} words.")
    print(f"Character count: {char_dict}")

def read_full(text):
    with open(text) as f:
        return f.read()

def wordcount(string):
    return len(string.split())

def letter_freq(text):
    text = text.lower()
    chars = {}

    for char in text:
        if char in chars:
                chars[char] += 1
        else:
                chars[char] = 1
    return chars

main()