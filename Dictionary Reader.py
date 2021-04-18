"""Opens words file and iterates through each line adding the words to a list"""


def dictionary_reader():
    words = open("Dictionary Words.txt", "r")
    dictionary = words.readlines()
    words.close()
    print(dictionary)
    print(len(dictionary))
    for line in dictionary:
        print(line)


def main():
    """Starts the function word_lookup"""
    dictionary_reader()


if __name__ == '__main__':
    main()
