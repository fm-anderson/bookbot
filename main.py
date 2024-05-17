def book_to_array(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents.split()

def get_word_count(array):
    return len(array)

def get_letter_count(array):
    counter = {}
    for word in array:
        for char in list(word):
            if char.isalpha():
                lowercased = char.lower()
                if lowercased in counter:
                    counter[lowercased] += 1
                else:
                    counter[lowercased] = 1
                    
    letters_sorted = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    return letters_sorted

def print_report(word_count, letters_dict, book):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    for char in letters_dict:
        print(f"The {char} character was found {letters_dict[char]} times")
    print("--- End report ---")
        
def main():
    book_path = "./books/frankenstein.txt"
    book_array = book_to_array(book_path)
    words = get_word_count(book_array)  
    letters = get_letter_count(book_array) 

    print_report(words, letters, book_path)
    
main()

