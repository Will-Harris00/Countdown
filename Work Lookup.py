"""Imports the python function for random number generator"""
import random


def word_search():
    """Test to determine how python reads the txt file by default"""
    words = open("Dictionary Words.txt")
    print(words.read())


def word_lookup(substringletters):
    """Converts each line in the txt file into an element in the list"""
    correctwords = ""
    with open("Dictionary Words.txt") as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            if substringletters == line:
                correctwords += line
                print(correctwords)


def select_characters():
    """Defines the function used to select the letters used in the game"""
    letters = ""
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    num = 0
    while num < 3:
        ans = str(input("Select letter " + str(num+1) +
                        " - Type a 'c' for a consonant or a 'v' for a vowel: "))
        if ans == "c":
            letters += consonant[random.randint(0, 20)]
            print("\nLetter " + str(num+1) + " is '" + letters[num] + "'")
            print("The current string is \"" + letters + "\"\n")
            num += 1
        elif ans == "v":
            letters += vowel[random.randint(0, 4)]
            print("\nLetter " + str(num+1) + " is '" + letters[num] + "'")
            print("The current string is \"" + letters + "\"\n")
            num += 1
        else:
            print("\nPlease enter only 'c' or 'v'\n")
    print("Here are the letters to use \"" + letters + "\"\n")
    return letters


def word_combinations(letters):
    """Finds every combination of every length of the available characters"""
    sorted_word = "".join(sorted(letters))
    from itertools import permutations
    # starting with the longest letter string count down to zero
    for i in range(len(sorted_word), 0, -1):
        # for each length of letter strings generate all possible combinations
        for substringletterslist in permutations(sorted_word, i):
            # for each combination of letters convert list to string
            substringletters = "".join(substringletterslist)
            # substring_letters should then be compared with a sorted_word_list
            print(substringletters)  # printing is only here for test purposes
    return substringletters


def main():
    """Starts the function word_lookup"""
    word_lookup(word_combinations(select_characters()))


if __name__ == '__main__':
    main()
