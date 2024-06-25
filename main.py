def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(f"This book contains {word_count()} words!")   

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count
main()

