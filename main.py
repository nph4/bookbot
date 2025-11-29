from stats import get_book_text 
from stats import get_word_count


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book)
    print(f"Found {num_words} total words")


main()


