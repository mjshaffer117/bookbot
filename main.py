def main():
    path = "./github.com/mjshaffer117/bookbot/books/"
    file = "frankenstein.txt"

    words = get_text(path + file)
    print(count_words(words))


def get_text(file):
    with open(file) as contents:
        return contents.read()


def count_words(contents):
    count = len(contents.split())
    return count



if __name__ == "__main__":
    main()
