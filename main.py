import sys
from stats import get_num_words, character_count, sort_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = get_num_words(text)
    ch_count = character_count(text)
    clean_list = sort_count(ch_count)
    print_report(book_path, word_count, clean_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, word_count, clean_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in clean_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
main()