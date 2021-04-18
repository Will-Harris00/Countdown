"""Opens words file and iterates through each line adding the words to a list"""


def dictionary_reader():
    with open("3 Letter Words.txt", "r") as words:
        dictionary = words.read().splitlines()
    words.close()
    print(dictionary)
    print(len(dictionary))
    for line in dictionary:
        print(line)
        print(len(line))


def main():
    """Starts the function dictionary_reader"""
    dictionary_reader()


if __name__ == '__main__':
    main()
