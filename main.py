from stats import get_word_num, get_char_stats, sort_key, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_word_num(text) 
    char_dict = get_char_stats(text)
    print(f"Found {num_words} total words")
    print(char_dict)    
    sort_dict(char_dict)
    print(sorted_d)

main()
