# Function to get the number of words in the books
def get_book_num_words(text):
    words_in_book = text.split()
    num_words = len(words_in_book)
    return num_words

# Function to get the number of letters in the books.
# Only displays alpha characters.
def num_letters(text):
    letter_count = {}
    letters = text.lower()
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Function to sort the letters into dictionaires dpending on frequency in the book.
def sorting_letter(letter_count):
    # Filter for alphabetic characters and convert to list of tuples
    alpha_count = [(letter, count) for letter, count in letter_count.items() if letter.isalpha()]
    # Sort by count (descending)
    alpha_count.sort(key=lambda x: x[1], reverse=True)
    return alpha_count