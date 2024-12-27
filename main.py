def main():
    book_path = "books/frankenstein.txt"
    book_string = read_full(book_path)
    num_words = wordcount(book_string)
    print(f"{num_words} words.")

def read_full(text):
        with open(text) as f:
            return f.read()

def wordcount(string):
            return len(string.split())

main()