"""Generates a string of characters based on frequency analysis of the dictionary"""


def select_characters():
    """Defines the function used to select the letters used in the game"""
    letters = ""
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowelweight = [0.223, 0.313, 0.194, 0.194, 0.076]
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                 'k', 'l', 'm', 'n', 'p', 'q', 'r',
                 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonantweight = [0.0270, 0.0405, 0.0811, 0.0270, 0.0405, 0.0270, 0.0135,
                       0.0135, 0.0676, 0.0542, 0.1081, 0.0542, 0.0135, 0.1216,
                       0.1216, 0.1216, 0.0135, 0.0135, 0.0135, 0.0135, 0.0135]
    num = 0
    vowelcount = 0
    consonantcount = 0
    print("Please select a minimum of one vowel and one consonant\n")
    while num < 9:
        from numpy.random import choice
        ans = str(input("Select letter " + str(num+1) +
                        " - Type a 'c' for a consonant or a 'v' for a vowel: "))
        if ans == "c":
            letters += choice(consonant, p=consonantweight)
            print("\nLetter " + str(num+1) + " is '" + letters[num] + "'")
            print("The current string is \"" + letters + "\"\n")
            num += 1
            vowelcount += 1
        elif ans == "v":
            letters += choice(vowel, p=vowelweight)
            print("\nLetter " + str(num+1) + " is '" + letters[num] + "'")
            print("The current string is \"" + letters + "\"\n")
            num += 1
            consonantcount += 1
        else:
            print("\nPlease enter only 'c' or 'v'\n")
    if vowelcount < 1 or consonantcount < 1:
        print("\"" + letters + "\"" +
              " does not contain a minimum of one vowel and one consonant\n")
        select_characters()
    else:
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
    """Runs the program"""
    word_combinations(select_characters())


if __name__ == '__main__':
    main()
