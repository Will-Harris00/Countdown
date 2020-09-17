"""Imports the python function for random number generator"""
import random


def select_characters():
    """Defines the function used to select the letters used in the game"""
    letters = ""
    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    num = 0
    while num < 9:
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
    input(" Press enter to exit program")


def main():
    """Runs the program"""
    select_characters()


if __name__ == '__main__':
    main()
