from stats import get_num_words
from stats import get_character_count
from stats import get_sorted_list

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>:")
    sys.exit(1)  
else:
    book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_dict = get_character_count(text)
    sorted_list = get_sorted_list(char_dict)
    print_report(book_path, word_count, sorted_list)

def print_report(book_path, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()