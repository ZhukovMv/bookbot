def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_number(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}

    for c in text:
        lower = c.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    
    return chars

def dict_to_array(dict):
    array = []

    for i in dict:
        if i.isalpha():
            el = {"char": i, "count": dict[i]}
            array.append(el)
    array.sort(reverse=True, key=sort_on)
    return array    

def sort_on(dict):
    return dict["count"]

def print_report(text, book_path):
    num_words = get_words_number(text)

    num_characters = get_chars_dict(text)
    chars_array = dict_to_array(num_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char in chars_array:
        print(f"The '{char['char']}' character was found {char['count']} times")

    print("--- End report ---")




main()