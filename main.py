def main():
    book_path = "books/frankenstein.txt"
    book_string = read_full(book_path)
    num_words = wordcount(book_string)
    char_dict = letter_freq(book_string)
    char_sorted_list = convert_dict_to_sorted_list(char_dict)

    
    print(f"-------{book_path} Statistics-------")
    print(f"{num_words} words.")
    print()

    for c in char_sorted_list:
        if not c["char"].isalpha():
             continue
        print(f"The character {c["char"]} appears {c["num"]} times!")
    print("-----------------------------------------")
    print("Report Complete.")

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

def convert_dict_to_sorted_list(d):
    list_of_dicts = []
    for ch in d:
        list_of_dicts.append({"char":ch, "num":d[ch]})
        list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def sort_on(dict):
    return dict["num"]

main()
