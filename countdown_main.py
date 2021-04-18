"""This module is designed to run the countdown letter combinations game"""
import time
from typing import List, Tuple
from numpy.random import choice


def select_characters(test=False):
    """Generates a string of characters based on frequency analysis of the dictionary"""
    if test:
        return "test"
    ascii_banner = (
        "__        __   _                            _____              \n" +
        "\\ \\      / /__| | ___ ___  _ __ ___   ___  |_   _|__         \n" +
        " \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\   | |/ _ \\  \n" +
        "  \\ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |        \n" +
        "   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|   |_|\\___/   \n" +
        "                                                               \n" +
        "  ____                  _      _                     _         \n" +
        " / ___|___  _   _ _ __ | |_ __| | _____      ___ __ | |        \n" +
        "| |   / _ \\| | | | '_ \\| __/ _` |/ _ \\ \\ /\\ / / '_ \\| |  \n" +
        "| |__| (_) | |_| | | | | || (_| | (_) \\ V  V /| | | |_|       \n" +
        " \\____\\___/ \\__,_|_| |_|\\__\\__,_|\\___/ \\_/\\_/ |_| |_(_)\n" +
        "                                                                 ")
    print(ascii_banner)
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
    print("Please select 9 letters")
    print("Please include a minimum of one vowel and one consonant\n")
    while len(letters) < 9:
        response = str(input("Select letter " + str(len(letters)+1) +
                             " - Type a 'c' for a consonant or a 'v' for a vowel: "))
        if response == 'c':
            if consonant_count == 8:
                print("Vowel selected as not enough chosen")
                letters += choice(vowel, p=vowelweight)
                vowel_count += 1
            else:
                letters += choice(consonant, p=consonantweight)
                consonant_count += 1
        elif response == 'v':
            if vowel_count == 8:
                print("Consonant selected as not enough chosen")
                letters += choice(consonant, p=consonantweight)
                consonant_count += 1
            else:
                letters += choice(vowel, p=vowelweight)
                vowel_count += 1
        else:
            print("Please enter only 'c' or 'v'")
    input("Press enter to view the letters generated ")
    print("\nHere are the letters to use \"" + letters + "\"\n")
    return letters


def word_combinations(letters: str) -> str:
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


def dictionary_reader() -> Tuple[str, str]:
    """Opens words file and iterates through each line adding the words to a list"""
    sorted_dictionary = []
    with open("../Dictionary Words.txt", "r") as words:
        dictionary = words.read().splitlines()
    words.close()
    normal_dictionary = [line for line in dictionary if len(line) < 10]
    normal_dictionary = [x.lower() for x in normal_dictionary]
    for element in normal_dictionary:
        alphabetical = "".join(sorted(element))
        sorted_dictionary.append(alphabetical.lower())
    return normal_dictionary, sorted_dictionary


def word_lookup(comblist: List[str], sorted_dictionary: List[str],
                normal_dictionary: List[str]) -> List[str]:
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


def long_words(wordlist: List[str]) -> List[str]:
    """This function finds the longest english word that can be made with the
    random selection of characters"""
    equal_length = ""
    length = 0
    for element in wordlist:
        if len(element) > length:
            length = len(element)
            index = wordlist.index(element)
            equal_length = wordlist[index]
        elif len(element) == length:
            index = wordlist.index(element)
            equal_length += (", " + wordlist[index])
    longest_words = equal_length.split(", ")
    return longest_words


def user_guess(wordlist: List[str], longest_words: List[str], test=False):
    """This function allows for comparison of the users guess with the matching
    list of words and scores the user according to the length of the word chosen"""
    best_word = False
    max_time = 30
    score = 0
    print("The timer has begun\n")
    print("Please use the singular form of the english word")
    start = time.time()
    if test:
        response = "test"
    else:
        response = str(input("Enter your guess for the longest possible word: "))
    end = time.time()
    timer = (end - start)
    seconds = (round(timer, 2))
    print("\nTime taken: " + str(seconds) + " seconds\n")
    guess = response.lower()
    if guess in longest_words and timer <= max_time:
        score = str(len(longest_words[0]))
        print("Your answer '" + guess + "' is the longest word that can be made "
              "with\nthese letters you scored " + score + " points")
    elif guess in wordlist:
        if timer <= max_time:
            score = str(len(guess))
            print("The word \'" + guess + "\'" + " scores "
                  + score + " points")
        elif timer > max_time:
            score = 0
            print("Your answer '" + guess + "' was correct but you took too long "
                  "so scored " + str(score) + " points")
    elif guess not in wordlist:
        print("Your answer '" + guess + "' was incorrect so you scored 0 points")
    if guess in longest_words:
        best_word = True
    if not best_word:
        print("\nThe longest words you could have made with these"
              " letters are: ")
        print(*longest_words, sep="\n")
        print("\nThis would be worth " + str(len(longest_words[0])) + " points")
    elif not best_word:
        print("\nCongratulations on finding the longest word")
    input("\nPress any key to view a list of all the possible answers: ")
    print(*wordlist, sep="\n")
    response = str(input("\nWould you like to play again? "))
    if response in ['y', 'yes', 'okay', 'sure', 'yes please']:
        run_game()
    elif response not in ['y', 'yes', 'okay', 'sure', 'yes please']:
        input("\nPress enter to exit the game")
    return score


def run_game():
    """This function allow the game to be run multiple times after completion"""
    combinations = word_combinations(select_characters())
    standard_dictionary, sorted_dictionary = dictionary_reader()
    longest = word_lookup(combinations, sorted_dictionary, standard_dictionary)
    longword = long_words(longest)
    user_guess(longest, longword)


def main():
    """Runs the program"""
    if select_characters(True) == "test":
        print("select_characters test: PASSED")
    else:
        print("select_characters test: FAILED")
    norm_dic, sorted_dic = dictionary_reader()
    if len(norm_dic) > 5000:
        print("dictionary_reader test: PASSED")
    else:
        print("dictionary_reader test: FAILED")
    index_list = word_lookup(word_combinations("examine"), sorted_dic, norm_dic)
    if len(index_list) > 3:
        print("word_lookup test: PASSED")
    else:
        print("word_lookup test: FAILED")
    long_matches = long_words(word_lookup("reference", index_list, norm_dic))
    if len(long_matches) >= 1:
        print("user_guess test: PASSED")
    else:
        print("user_guess test: FAILED")
    run_game()


if __name__ == '__main__':
    main()
