def count_words(book_text: str) -> int:
    return len(book_text.split())


def count_characters(book_text: str) -> int:
    character_count = {}
    book_text = book_text.lower()
    for c in book_text:
        character_count[c] = character_count.get(c, 0) + 1
    return character_count


def main() -> None:
    with open('books/frankenstein.txt') as f:
        book_text = f.read()
        word_count = count_words(book_text)
        character_counts = count_characters(book_text)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for c in sorted(character_counts):
            print(f"The {repr(c)} character was found {character_counts[c]} times")


main()
