def main():
        book_text = get_book_text('books/frankenstein.txt')
        count = count_words(book_text)
        # print(count)
        character_counts = count_characters(book_text)
        # print(character_counts)
        print_report(character_counts, count)

def get_book_text(path):
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_counts = {}
    for char in text:
        if(char.isalpha()):
            c = char.lower()
            if c not in character_counts:
                character_counts[c] = 0
            character_counts[c] += 1
    return character_counts

def print_report(character_counts, word_count):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{word_count} words found in the document")
    for char in character_counts:
        print(f"The {char} character was found {character_counts[char]} times")

# This line tells Python to run main() only if this file is run directly
if __name__ == "__main__":
    main()