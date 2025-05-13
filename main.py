import sys

from stats import get_num_words, get_num_characters, get_sorted_nums


def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    text = get_book_text(file_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    num_characters = get_num_characters(text)
    sorted_characters = get_sorted_nums(num_characters)
    for entry in sorted_characters:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
