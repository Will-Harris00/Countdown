"""This module is designed to run the countdown word game"""
import time
from numpy.random import choice


def select_characters():
    """Generates a string of characters based on frequency analysis of the dictionary"""
    letters = ""
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowelweight = [0.223, 0.313, 0.194, 0.194, 0.076]
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                 'k', 'l', 'm', 'n', 'p', 'q', 'r',
                 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonantweight = [0.0270, 0.0405, 0.0811, 0.0270, 0.0405, 0.0270, 0.0135,
                       0.0135, 0.0676, 0.0542, 0.1081, 0.0542, 0.0135, 0.1216,
                       0.1216, 0.1216, 0.0135, 0.0135, 0.0135, 0.0135, 0.0135]
    vowel_count = 0
    consonant_count = 0
    print("Please select a minimum of one vowel and one consonant\n")
    while len(letters) < 9:
        ans = str(input("Select letter " + str((len(letters)+1)) +
                        " - Type a 'c' for a consonant or a 'v' for a vowel: "))
        if ans == "c":
            letters += choice(consonant, p=consonantweight)
            print("\nLetter " + str(len(letters)+1) + " is '"
                  + letters[vowel_count+consonant_count] + "'")
            print("The current string is \"" + letters + "\"\n")
            vowel_count += 1
        elif ans == "v":
            letters += choice(vowel, p=vowelweight)
            print("\nLetter " + str(len(letters)+1) + " is '"
                  + letters[vowel_count+consonant_count] + "'")
            print("The current string is \"" + letters + "\"\n")
            consonant_count += 1
        else:
            print("\nPlease enter only 'c' or 'v'\n")
    if vowel_count < 1 or consonant_count < 1:
        print("\"" + letters + "\"" +
              " does not contain a minimum of one vowel and one consonant\n")
        select_characters()
    else:
        print("Here are the letters to use \"" + letters + "\"\n")
    return letters


def word_combinations(letters):
    """Finds every combination of every length of the available characters"""
    sorted_word = "".join(sorted(letters))
    comblist = []
    from itertools import combinations
    # starting with the longest letter string count down to zero
    for i in range(len(sorted_word), 0, -1):
        # for each length of letter strings generate all possible combinations
        for substringletterslist in combinations(sorted_word, i):
            # for each combination of letters convert list to string
            substringletters = "".join(substringletterslist)
            comblist.append(substringletters)
    # substring_letters should then be compared with a sorted_word_list
    return comblist


def dictionary_reader():
    """Opens words file and iterates through each line adding the words to a list"""
    sorted_dictionary = []
    with open("Dictionary Words.txt", "r") as words:
        dictionary = words.read().splitlines()
    words.close()
    normal_dictionary = [line for line in dictionary if len(line) < 10]
    normal_dictionary = [x.lower() for x in normal_dictionary]
    for element in normal_dictionary:
        alphabetical = "".join(sorted(element))
        sorted_dictionary.append(alphabetical.lower())
    return normal_dictionary, sorted_dictionary


def word_lookup(comblist, sorted_dictionary, normal_dictionary):
    """"This function compares the various combinations of the string letters
        with the sorted dictionary and adding matching words to a new list"""
    wordlist = []
    wordindex = []
    for line in sorted_dictionary:
        if line in comblist:
            index = sorted_dictionary.index(line)
            wordindex.append(index)
            sorted_dictionary[index] = None
    for element in wordindex:
        wordlist.append(normal_dictionary[element])
    return wordlist


def long_words(wordlist):
    """This function finds the longest english word that can be made with the
    random selection of characters"""
    longest_word = []
    length = 0
    for element in wordlist:
        if len(element) > length:
            length = len(element)
            index = wordlist.index(element)
            longest_word = (wordlist[index])
    return longest_word


def user_guess(wordlist, longest_word):
    print("The timer has begun\n")
    start = time.time()
    response = str(input("Enter your guess for the longest possible word: "))
    end = time.time()
    timer = (end - start)
    print(timer)
    guess = response.lower()
    if guess in wordlist:
        print(guess + " scores " + str(len(guess)) + " points")


def main():
    """Runs the program"""
    combinations = word_combinations(select_characters())
    standard_dictionary, sorted_dictionary = dictionary_reader()
    longest = word_lookup(combinations, sorted_dictionary, standard_dictionary)
    longword = long_words(longest)
    user_guess(longest, longword)


if __name__ == '__main__':
    main()


# user start timer in one function as soon as the characters are available
# and stop timer as soon as the user submits their answer for the longest word

# user a test string for the combination of letters function

# add ascii art to the program

# use typehinting to define variable and the type of data that they contain

# add doc string to each line of the function to make the program easier to understand

# user validation for if not 'c' or 'v' where wrong input is given

# allow the user to guess the longest possible word and compare this with any
# matches between the two lists

# use boolean true and false statement for the testing framework

# get length of longest word and length of max possible word to compare user score
# to highest possible score

# use the assert function to check for possible combinations
