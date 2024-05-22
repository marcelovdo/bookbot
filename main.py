def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    num_words = get_num_words(contents)
    letter_count = get_letter_count(contents)
    ordered_list = get_ordered_list(letter_count)
    show_ordered_list(ordered_list, book_path, num_words)

def get_book_contents(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(contents):
    return len(contents.split())

def get_letter_count(contents):
    count = {}
    for character in contents.lower():
        if character in count:
            count[character] += 1
        else:
            count[character] = 1
    return count

def get_ordered_list(letter_count):
    result = []
    for letter in letter_count:
        if letter.isalpha():
            result.append({ "char": letter, "count": letter_count[letter]})
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(dict):
    return dict["count"]

def show_ordered_list(ordered_list, book_path, num_words):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter in ordered_list:
        print(f"The '{letter["char"]}' character was found {letter["count"]} times")
    print("--- End report ---")
    

main()