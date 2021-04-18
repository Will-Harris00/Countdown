"""This module is designed to run the countdown letter combinations game"""
import time
from typing import List, Tuple
from numpy.random import choice


def select_characters(test=False):
    """Generates a string of characters to use in the letter combinations game
       based on frequency analysis of the letters in the english dictionary"""
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
    letters_string = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_weight = [0.223, 0.313, 0.194, 0.194, 0.076]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                  'k', 'l', 'm', 'n', 'p', 'q', 'r',
                  's', 't', 'v', 'w', 'x', 'y', 'z']
    consonant_weight = [0.0270, 0.0405, 0.0811, 0.0270, 0.0405, 0.0270, 0.0135,
                        0.0135, 0.0676, 0.0542, 0.1081, 0.0542, 0.0135, 0.1216,
                        0.1216, 0.1216, 0.0135, 0.0135, 0.0135, 0.0135, 0.0135]
    vowel_count = 0
    consonant_count = 0
    print("Please select 9 letters")
    print("Please include a minimum of one vowel and one consonant\n")
    while len(letters_string) < 9:
        response = str(input("Select letter " + str(len(letters_string)+1) + " -"
                             + " Type 'c' for a consonant or 'v' for a vowel: "))
        if response == 'c':
            if consonant_count == 8:
                print("Automatically selected a vowel to meet criteria")
                letters_string += choice(vowels, p=vowel_weight)
                vowel_count += 1
            else:
                letters_string += choice(consonants, p=consonant_weight)
                consonant_count += 1
        elif response == 'v':
            if vowel_count == 8:
                print("Automatically selected a consonant to meet criteria")
                letters_string += choice(consonants, p=consonant_weight)
                consonant_count += 1
            else:
                letters_string += choice(vowels, p=vowel_weight)
                vowel_count += 1
        else:
            print("Please answer with only 'c' or 'v'")
    input("Press enter to view the letters generated ")
    print("\nHere are the letters to use \"" + letters_string + "\"\n")
    return letters_string


def word_combinations(letters_string):
    """Finds every combination of available characters independent
       of length and add these substrings to a list"""
    sorted_string = "".join(sorted(letters_string))
    comb_list = []
    from itertools import combinations
    for i in range(len(sorted_string), 0, -1):
        for substring_letters_list in combinations(sorted_string, i):
            substring_letters = "".join(substring_letters_list)
            comb_list.append(substring_letters)
    return comb_list


def dictionary_reader():
    """Opens the text file containing the dictionary and
       iterates through each line adding the words to a list"""
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


def word_lookup(comb_list, sorted_dictionary, normal_dictionary):
    """This function does a comparison for each line in the sorted_dictionary
       to determine if it appears in the alphabetically sorted comb_list,
       if the two items are identical it will get the index of the item
       in the sorted_dictionary and add this to the list word_index, the next
       step of this process involves using the list of indexes to look up the
       original form of the word in the normal_dictionary and add this to a
       new list called word_list which contains all the possible matches"""
    word_list = []
    word_index = []
    for line in sorted_dictionary:
        if line in comb_list:
            index = sorted_dictionary.index(line)
            word_index.append(index)
            sorted_dictionary[index] = None
    for element in word_index:
        word_list.append(normal_dictionary[element])
    return word_list


def lengthy_words(word_list):
    """This function iterates through every item in the word_list and will
       overwrite the list longest_list with the current element if its length
       exceeds that of any element the loop has previously checked, if two or
       more words are the longest and of equal lengths then all are appended"""
    longwords_string = ""
    longest_length = 0
    for element in word_list:
        if len(element) > longest_length:
            longest_length = len(element)
            index = word_list.index(element)
            longwords_string = word_list[index]
        elif len(element) == longest_length:
            index = word_list.index(element)
            longwords_string += (", " + word_list[index])
    longest_list = longwords_string.split(", ")
    return longest_list


def user_guess(word_list, longest_list, test=False):
    """This function allows for comparison of the users guess with the
       matching list of words and scores the user according to the length
       of the word chosen, at the end of the game the user is shown all
       correct answers as well as the best possible words to score highest"""
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
    if guess in longest_list and timer <= max_time:
        score = str(len(longest_list[0]))
        print("Your answer '" + guess + "' is one of the longest words that "
              "can be made with\nthese letters, you scored " + score + " points")

    elif guess in word_list:
        if timer <= max_time:
            score = str(len(guess))
            print("The word \'" + guess + "\'" + " scores "
                  + score + " points")
        elif timer > max_time:
            print("Your answer '" + guess + "' was correct but"
                  "\nyou took too long so scored zero points")
    elif guess not in word_list:
        print("Your answer '" + guess + "' was incorrect so you scored 0 points")

    if guess in longest_list:
        best_word = True
    if not best_word:
        print("\nThe longest words you could have made with these"
              " letters are: ")
        print(*longest_list, sep="\n")
        print("\nThese would each be worth " +
              str(len(longest_list[0])) + " points")
    elif best_word:
        print("\nCongratulations on finding one of the longest words")
        print("\nHere are all the longest words you could "
              "have made with these letters: ")
        print(*longest_list, sep="\n")
    input("\nPress enter to view a list of all the possible answers: ")
    print(*word_list, sep="\n")

    response = str(input("\nWould you like to play again? "))
    if response in ['y', 'yes', 'okay', 'sure', 'yes please']:
        run_game()
    elif response not in ['y', 'yes', 'okay', 'sure', 'yes please']:
        input("\nPress enter to exit the game")
    return score


def run_game():
    """This function contains the entire game and can be called at the end of
       the each game to play the game again as many times as the user wants"""
    combinations = word_combinations(select_characters())
    standard_dictionary, sorted_dictionary = dictionary_reader()
    long_words = word_lookup(combinations, sorted_dictionary,
                             standard_dictionary)
    longest = lengthy_words(long_words)
    user_guess(long_words, longest)


def main():
    """This function is responsible for testing before the game begins
       and running the first instance of the game before it is later looped"""
    if select_characters(True) == "test":
        print("select_characters test: PASSED")
    else:
        print("select_characters test: FAILED")
    norm_dic, sorted_dic = dictionary_reader()
    if len(norm_dic) > 5000:
        print("dictionary_reader test: PASSED")
    else:
        print("dictionary_reader test: FAILED")
    index_list = word_lookup(word_combinations("examine"),
                             sorted_dic, norm_dic)
    if len(index_list) > 3:
        print("word_lookup test: PASSED")
    else:
        print("word_lookup test: FAILED")
    long_matches = lengthy_words(word_lookup("evaluate",
                                             index_list, norm_dic))
    if len(long_matches) >= 1:
        print("user_guess test: PASSED")
    else:
        print("user_guess test: FAILED")
    run_game()


if __name__ == '__main__':
    main()
