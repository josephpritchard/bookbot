import sys
from stats import get_word_num, get_char_stats, sort_key, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(report_dict):
    for d in report_dict:
        if d["char"].isalpha(): 
            character = d["char"]
            count = d["num"] 
            print(f"{character}: {count}")

def startup():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
 

def main():
    startup() 
    text = get_book_text(sys.argv[1])
    num_words = get_word_num(text) 
    char_dict = get_char_stats(text)
    sorted_dict = sort_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}") 
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    print_report(sorted_dict)
    print("============= END ===============")

main()
