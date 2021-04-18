"""This module is designed to run the countdown word game"""
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
    # the list of numbers corresponds to the likelihood of selecting each vowel
    vowel_weight = [0.223, 0.313, 0.194, 0.194, 0.076]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j',
                  'k', 'l', 'm', 'n', 'p', 'q', 'r',
                  's', 't', 'v', 'w', 'x', 'y', 'z']
    # this list is the likelihood of selecting each consonant
    consonant_weight = [0.0270, 0.0405, 0.0811, 0.0270, 0.0405, 0.0270, 0.0135,
                        0.0135, 0.0676, 0.0542, 0.1081, 0.0542, 0.0135, 0.1216,
                        0.1216, 0.1216, 0.0135, 0.0135, 0.0135, 0.0135, 0.0135]
    # counters for the number of vowels and consonants in the current string
    vowel_count = 0
    consonant_count = 0
    print("Please select 9 letters")
    print("Please include a minimum of one vowel and one consonant\n")
    # while loop exits when nine characters have been selected and of these a
    # minimum of one vowel and one consonant have been selected for the string
    while len(letters_string) < 9:
        response = str(input("Select letter " + str(len(letters_string)+1) + " -"
                             + " Type 'c' for a consonant or 'v' for a vowel: "))
        if response == 'c':
            # if the user inputs c and less than 8 consonants have already been
            # added to the string then a consonant is generated and added to the
            # string according to the probabilities in the weighting list above
            if consonant_count == 8:
                print("Automatically selected a vowel to meet criteria")
                letters_string += choice(vowels, p=vowel_weight)
                vowel_count += 1
            # if the user inputs c and 8 consonants have been selected already then
            # the remaining letter in the string is required to be a vowel so that
            # the minimum criteria for the number of vowels and consonants is met,
            # therefore the program ignores the user request for another consonant
            # and instead will generate and add a vowel to the string of letters
            else:
                letters_string += choice(consonants, p=consonant_weight)
                consonant_count += 1
        elif response == 'v':
            # if the user inputs v and less than 8 vowels have already been
            # added to the string then a consonant is generated and added to the
            # string according to the probabilities in the weighting list above
            if vowel_count == 8:
                print("Automatically selected a consonant to meet criteria")
                letters_string += choice(consonants, p=consonant_weight)
                consonant_count += 1
            # if the user inputs v and 8 vowels have been selected already then
            # the last letter in the string is required to be a consonant so that
            # the minimum criteria for the number of vowels and consonants is met,
            # therefore the program ignores the user request for another vowel and
            # instead will generate and add a consonant to the string of letters
            else:
                letters_string += choice(vowels, p=vowel_weight)
                vowel_count += 1
        else:
            print("Please answer with only 'c' or 'v'")
    input("Press enter to view the letters generated ")
    print("\nHere are the letters to use \"" + letters_string + "\"\n")
    return letters_string


def word_combinations(letters_string: str) -> str:
    """Finds every combination of available characters independent
       of length and add these substrings to a list"""
    # sorted_string contains same letters as before but arranged alphabetically
    sorted_string = "".join(sorted(letters_string))
    comb_list = []
    from itertools import combinations
    # generate combination of substrings starting with the full letters_string
    for i in range(len(sorted_string), 0, -1):
        # for each length of substrings generate all possible combinations
        for substring_letters_list in combinations(sorted_string, i):
            # for each combination of letters convert list to string
            substring_letters = "".join(substring_letters_list)
            comb_list.append(substring_letters)
    # later list of combinations is compared with sorted_dictionary
    return comb_list


def dictionary_reader() -> Tuple[str, str]:
    """Opens the text file containing the dictionary and
       iterates through each line adding the words to a list"""
    sorted_dictionary = []
    # converts each line in the text file into a list
    with open("../Dictionary Words.txt", "r") as words:
        # remove all newline characters and add the word to dictionary list
        dictionary = words.read().splitlines()
    words.close()
    # adds all words less than 9 characters in length to normal_dictionary list
    normal_dictionary = [line for line in dictionary if len(line) < 10]
    # removes any capitalisation within word inside the normal_dictionary
    normal_dictionary = [x.lower() for x in normal_dictionary]
    for element in normal_dictionary:
        # makes a new list, sorted_dictionary, where the characters
        # making up each word are arranged alphabetically
        alphabetical = "".join(sorted(element))
        sorted_dictionary.append(alphabetical.lower())
    # by removing any word greater than length 9 in the previous step we ensure
    # that the index of sorted_dictionary can be used to find the proper
    # english word in the normal_dictionary which has not been modified
    return normal_dictionary, sorted_dictionary


def word_lookup(comb_list: List[str], sorted_dictionary: List[str],
                normal_dictionary: List[str]) -> List[str]:
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
        # here we are comparing the each line in the sorted_dictionary to
        # each arrangement of letters in the comb_list to find perfect matches
        if line in comb_list:
            # if a match is found we then get the index of the line from
            # the sorted_dictionary and store this value in word_index
            index = sorted_dictionary.index(line)
            word_index.append(index)
            # so that words made from identical letters are not missed from
            # the word_index we set a value of None for any lines that have
            # already been evaluated ensuring that we do not evaluate the
            # same line multiple times and are able to move on to the next
            # instance of the identical combination of letters
            sorted_dictionary[index] = None
    for element in word_index:
        # here we are using out list of indexes for matching words to find the
        # original form of the english word to add to out matching word_list
        word_list.append(normal_dictionary[element])
    return word_list


def lengthy_words(word_list: List[str]) -> List[str]:
    """This function iterates through every item in the word_list and will
       overwrite the list longest_list with the current element if its length
       exceeds that of any element the loop has previously checked, if two or
       more words are the longest and of equal lengths then all are appended"""
    longwords_string = ""
    longest_length = 0
    for element in word_list:
        # if the current word being evaluated is longer than any previous word
        # the entire list is overwritten with the new longest word
        if len(element) > longest_length:
            # the longest_length variable is updated with the number
            # of letters in the longest word
            longest_length = len(element)
            # here we are finding the positional index of the longest word
            index = word_list.index(element)
            # the index is used to overwrite longwords_string with longest_word
            longwords_string = word_list[index]
        elif len(element) == longest_length:
            # the current word being evaluated is equal in length to all the
            # words currently in longwords_string so we need to append it
            index = word_list.index(element)
            # this code adds the current word to the continuous string
            # longwords_string and separates is from other items by a comma
            longwords_string += (", " + word_list[index])
    # longwords_string is a continuous string with items separated by a ', '
    # this code look for each comma and splits the string into separate
    # elements based on separation by the comma and adds them to longest_list
    longest_list = longwords_string.split(", ")
    return longest_list


def user_guess(word_list: List[str], longest_list: List[str], test=False):
    """This function allows for comparison of the users guess with the
       matching list of words and scores the user according to the length
       of the word chosen, at the end of the game the user is shown all
       correct answers as well as the best possible words to score highest"""

    # consider that when evaluating the users guess there are only four
    # possible scenarios when comparing their input to the correct answers
    # First: the user guesses one of the best possible words with the
    # longest length and submits their answer within the allowed time limit
    # Second: the user guesses a correct word which is not one of the best
    # words and submits their answer within the allowed time limit
    # Third: the user guesses a correct word but exceeds the time limit
    # Fourth: the user guesses an incorrect word

    # boolean logic for checking if the users guess is one of the best words
    best_word = False
    # time limit for the user to submit their answer
    max_time = 30
    score = 0
    print("The timer has begun\n")
    print("Please use the singular form of the english word")
    # timer begins as soon as the letters_string becomes visible to the user
    start = time.time()
    if test:
        response = "test"
    else:
        response = str(input("Enter your guess for the longest possible word: "))
    # the timer stops once the user has made their guess
    end = time.time()
    # from the start and finish times the time taken is calculated
    timer = (end - start)
    # rounding the time in seconds to an appropriate degree of accuracy
    seconds = (round(timer, 2))
    # informs the user of how long they took to submit their answer
    print("\nTime taken: " + str(seconds) + " seconds\n")

    # users guess has any capitalisation removed
    guess = response.lower()
    # from above we consider the first scenario referred to in line 202
    if guess in longest_list and timer <= max_time:
        # the score is updated with the number of characters the longest words
        score = str(len(longest_list[0]))
        # feedback is given to the user stating that they found the longest
        # word from the letters_string and score points equal to the length
        # of the the longest_word i.e. the length of the users guess
        print("Your answer '" + guess + "' is one of the longest words that "
              "can be made with\nthese letters, you scored " + score + " points")

    # evaluates time taken, provided users guess is a correct answer
    elif guess in word_list:
        # from above we consider the second scenario referred to in line 204
        if timer <= max_time:
            # score is changed to the number of characters in the users guess
            score = str(len(guess))
            # feedback is given to the user stating that they scored points
            # equal to the length of their answer
            print("The word \'" + guess + "\'" + " scores "
                  + score + " points")
        # from above we consider the third scenario referred to in line 206
        elif timer > max_time:
            # feedback is given to the user stating that whilst their answer
            # was correct, they exceeded the time limit so scored 0
            print("Your answer '" + guess + "' was correct but"
                  "\nyou took too long so scored zero points")
    # from above we consider the fourth scenario referred to in line 207
    elif guess not in word_list:
        # feedback is given to the user stating their guess was incorrect
        # so regardless of how quickly they answered they still scored 0
        print("Your answer '" + guess + "' was incorrect so you scored 0 points")

    # check previous boolean identity to determine whether users guess is one
    # of the longest_words, prints a different messages dependent on this logic
    if guess in longest_list:
        best_word = True
        # if user did not get longest_words then the below message is displayed
    if not best_word:
        print("\nThe longest words you could have made with these"
              " letters are: ")
        # shows all solutions with the greater number of letters
        print(*longest_list, sep="\n")
        print("\nThese would each be worth " +
              str(len(longest_list[0])) + " points")
        # if user did get longest_words then a different message is displayed
    elif best_word:
        print("\nCongratulations on finding one of the longest words")
        print("\nHere are all the longest words you could "
              "have made with these letters: ")
        # shows all alternative solutions with the greater number of letters
        print(*longest_list, sep="\n")
    # request user input before displaying all correct words of any length
    input("\nPress enter to view a list of all the possible answers: ")
    # shows all combinations of letters that make a word irrespective of length
    print(*word_list, sep="\n")

    # requests user input to determine whether to call run_game and play again
    response = str(input("\nWould you like to play again? "))
    # evaluates response and if one of the below, run the game from start
    if response in ['y', 'yes', 'okay', 'sure', 'yes please']:
        run_game()
    # awaits any other responses not listed and will request input to exit game
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
    # the module start by testing each of the different functions
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
    # countdown is started by calling the function run_game
    run_game()


if __name__ == '__main__':
    main()
