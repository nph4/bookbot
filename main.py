import stats
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = stats.read_book(book_path)
    words = stats.count_words(text)
    letters = stats.count_letters(text)
    report = stats.get_report(words, letters, book_path)
    
    print(report)


main()