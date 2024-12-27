def main():
    def read_full():
        with open("books/frankenstein.txt") as f:
            print(f.read())

    def wordcount():
        with open("books/frankenstein.txt") as f:
            words = f.read().split()
            print(len(words))

    wordcount()
main()