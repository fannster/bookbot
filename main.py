


import sys
sys.path.append("../bookbot")
from stats import get_num_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts =count_characters(text)
    sorted_chars = sort_characters(char_counts)




    print("============BOOKBOT============")
    print(f"Analyzing book found at {book_path}...")
    print("-----------Word Count-----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")

    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    
    print("============= END =============")
    



    
if __name__ == "__main__":
    main()




