def get_book_text(filepath):
    try:
        with open(filepath) as f:
            book_contents = f.read()
        return book_contents
    except FileNotFoundError:
        print("Please check the path.")

def get_word_count(book):
    wordlist = book.split()
    return len(wordlist)

def get_character_count(book):
    char_list = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "0",
        "1", "2", "3", "4", "5", "6", "7", "8", "9", ","
    ]