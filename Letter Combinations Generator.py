"""
This snippet of code will generate all combinations of letters in a string for
different lengths. Starting with the longest string, for which there is only
one combination additional characters will be removed until only one letter is
sampled at a time.
"""
from itertools import combinations


test_letters = "abcdefghi"
# sort the letters
sorted_word = "".join(sorted(test_letters))
# starting with the longest letter string count down to zero
for i in range(len(sorted_word), 0, -1):
    # for each length of letter strings generate all possible combinations
    for substring_letters_list in combinations(sorted_word, i):
        # for each combination of letters convert list to string
        substring_letters = "".join(substring_letters_list)
        # substring_letters should then be compared with a sorted_word_list
        print(substring_letters) # printing is only here for test purposes
