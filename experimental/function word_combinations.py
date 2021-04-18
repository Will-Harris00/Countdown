def word_combinations(letters_string: str) -> str:
    """Finds every combination of available characters independent
       of length and add these substrings to a list"""
    sorted_string = "".join(sorted(letters_string))
    comb_list = []
    from itertools import combinations
    # starting with the longest letter string count down to zero
    for i in range(len(sorted_string), 0, -1):
        # for each length of letter strings generate all possible combinations
        for substring_letters_list in combinations(sorted_string, i):
            # for each combination of letters convert list to string
            substring_letters = "".join(substring_letters_list)
            comb_list.append(substring_letters)
    # substring_letters should then be compared with a sorted_word_list
    print("List of combinations of letters in string:\n" + str(comb_list))
    return comb_list
>>>

Here are the letters to use "hoa"

List of combinations of letters in string:
['aho', 'ah', 'ao', 'ho', 'a', 'h', 'o']