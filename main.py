def main():
    book_path = "books/frankenstein.txt"
    book_string = read_full(book_path)
    num_words = wordcount(book_string)
    char_dict = letter_freq(book_string)
    char_list = convert_dict(char_dict)
    #char_list.sort(reverse=True, key=sort_on)
    print(f"=-=-=-=-{book_path} Statistics-=-=-=-=")
    print(f"{num_words} words.")
    for c in char_list:
        for key, value in c.items():
             print(f"The character {key} appears {value} times!")

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
def convert_dict(dict):
    list_of_dicts = []
    for key, value in dict.items():
        list_of_dicts.append({key: value})
    return list_of_dicts

def sort_on(dict):
    return dict["value"]

main()