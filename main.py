from stats import get_book_num_words, num_letters, sorting_letter
import sys

#Function to get the book path from *books/*.txt
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Function for error handling in Python in the event that argv does not have 2 arguments.      
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

# Try/Except block for main fucntion to run with proper formatting of the results.
# Exception block made to catch if the argv book path is invalid.
    path = sys.argv[1]
    try:
        text = get_book_text(path)
        num_words = get_book_num_words(text)
        letter_count = num_letters(text)
        sorted_count = sorting_letter(letter_count)

        # Start printing the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        # Loop through sorted counts and print only alphabetical characters
        for letter, count in sorted_count:
            print(f"{letter}: {count}")
                
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
main()