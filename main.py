import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(f"This book contains {word_count(file_contents)} words!")
    print(char_count(file_contents))   

def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)
    
def char_count(file_contents):
    allowed_characters = string.ascii_letters
    char_counts = {}
    for letter in file_contents.lower():
        if letter in allowed_characters:
            if letter not in char_counts:
                char_counts[letter] = 1
            else:
                char_counts[letter] += 1
    return char_counts

def sort_on(char_counts):
    return char_counts["num"]

char_counts.sort(reverse=True, key=sort_on)
main()

