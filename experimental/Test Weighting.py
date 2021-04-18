"""Imports the python function for random number generator"""
import random
import numpy


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
    num = 0
    while num < 4:
        from numpy.random import choice
        ans = str(input("Select letter " + str(num+1) +
                        " - Type a 'c' for a consonant or a 'v' for a vowel: "))
        if ans == "c":
            letters += choice(consonant, p=consonantweight)
            print("\nLetter " + str(num+1) + " is '" + letters[num] + "'")
            print("The current string is \"" + letters + "\"\n")
            num += 1
        elif ans == "v":
            letters += choice(vowel, p=vowelweight)
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


def dictionary_reader(substringletters):
    """Opens words file and iterates through each line adding the words to a list"""
    match = ""
    with open("../cntdwn/3 Letter Words.txt", "r") as words:
        dictionary = words.read().splitlines()
    for line in dictionary:
        if len(line) < 9 and line in substringletters:
            match += line
            print(len(line))
            print(line)
            words.close()
    print(match)
    input("Press enter to exit program")


def solver(substringletters):
    letters = sorted(letters) ##sorting alphabets
    for i in reversed(range(MIN_RANGE,MAX_RANGE)): #reverse means we are starting from high to low value. Decending order.
        result = set() #set to hold the result (countdown letters)
        for permutations in combinations(letters,i): #itertools.combinations()
            #we are looping through the list returned by the combinations function from itertools. 
            #"Return r length subsequences of elements from the input iterable."
            sortedWord = ''.join(permutations)
            if(sortedWord in dictionary):
                for word in dictionary[sortedWord]:
                    result.add(word)
        if(result):
            return result #we fond the longest
        #if you want to get all the words from length max (9) to min(4) than
        #comment if(result) then you can see all the words in decending order.
    return result


def word_lookup():
    """Imports a dictionary of all english words"""
    words = open("../cntdwn/Dictionary Words.txt")
    print(words.read())


def main():
    """Starts the function word_lookup"""
    dictionary_reader(word_combinations(select_characters()))


if __name__ == '__main__':
    main()
