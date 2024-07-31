def main():
    path = "./books/"
    file = "frankenstein.txt"
    words = get_text(path + file)
    word_count = count_words(words)
    char_count = count_characters(words.lower())
    print_report(path + file, word_count, char_count)


def get_text(file):
    with open(file) as contents:
        return contents.read()


def count_words(contents):
    count = len(contents.split())
    return count


def count_characters(text):
    chars = {}
    for char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
        if char in text:
            chars[char] = text.count(char)
        else:
            chars[char] = 0
    return chars


def print_report(file_name, word_count, char_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"Total words found: {word_count}")
    print("\n")
    char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    for char in char_count:
        print(f"Character '{char}' was found {char_count[char]} times in the file.")



if __name__ == "__main__":
    main()
