def read_book(book_path):
    # Open and read the contents of the specified book file
    try:
        with open(book_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print("Please check the path.")

def count_words(text):
    # Split the text into words and count the number of words
    words = text.split()
    return len(words)

def count_letters(text):
    # Count the frequency of each letter in the text
    non_duplicate_letters = text.lower()
    letters_dict = {}
    for letter in non_duplicate_letters:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def get_report(words, letters, book_path):
    # Generate a report including word count and letter frequency
    chars_data = ""
    sorted_list = []

    # Sort the list of letter frequencies in descending order
    for letter in letters:
        if not letter.isalpha():
            continue
        sorted_list.append(letters[letter])
    sorted_list.sort(reverse=True)

    # Generate the character frequency data for the report
    for char_count in sorted_list:
        for key, value in letters.items():
            if value == char_count:
                char = key
                char_data = f"{char}: {char_count}\n"
                chars_data += char_data

    # Construct and return the final report
    return f"============ BOOKBOT ============\n \
Analyzing book found at {book_path}...\n \
----------- Word Count ----------\n \
Found {words} total words\n \
--------- Character Count -------\n\
{chars_data}"