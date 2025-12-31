import sys
from stats import get_book_text, count_chars, chars_dict_to_sorted_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    for arg in sys.argv[1:]:
        book_path = arg
        book_contents = get_book_text(book_path)
        num_words = len(book_contents.split())

        char_counts = count_chars(book_contents)

        char_counts_sorted = chars_dict_to_sorted_list(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for c in char_counts_sorted:
            if not c["name"].isalpha():
                continue
            print(f"{c['name']}: {c['num']}")

        print("============= END ===============")


if __name__ == "__main__":
    main()
