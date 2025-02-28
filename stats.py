def get_book_num_words(text):
    words_in_book = text.split()
    num_words = len(words_in_book)
    return num_words

def num_letters(text):
    letter_count = {}
    letters = text.lower()
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def sorting_letter(letter_count):
    # Filter for alphabetic characters and convert to list of tuples
    alpha_count = [(letter, count) for letter, count in letter_count.items() if letter.isalpha()]
    # Sort by count (descending)
    alpha_count.sort(key=lambda x: x[1], reverse=True)
    return alpha_count