import string
# Grabbing frankenstein book text
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    # Printing a small portion of the book for readability
    preview_length = min(len(file_contents), 200)  # Print first 200 characters or less if file is shorter
    print(file_contents[:preview_length] + '...')  # Print first 200 chars with ellipsis if longer
    
    print(f"This book contains {word_count(file_contents)} words!")
    
    char_list = char_count(file_contents)  # Get the character list
    char_list.sort(reverse=True, key=sort_on)  # Sort the list
    # Printing report for character count
    print("--- Begin report of books/frankenstein.txt ---")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
# Splitting file contents text into word list
def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)
# creating dictionary with char -> count key value pair     
def char_count(file_contents):
    allowed_characters = string.ascii_letters
    char_counts = {}
    for letter in file_contents.lower():
        if letter in allowed_characters:
            if letter not in char_counts:
                char_counts[letter] = 1
            else:
                char_counts[letter] += 1
    # Splitting char_count dictionary into list of key value pairs for sorting
    char_list = [{"char": k, "num": v} for k, v in char_counts.items()]
    return char_list
# Sorting char_list
def sort_on(item):
    return item["num"]

main()

