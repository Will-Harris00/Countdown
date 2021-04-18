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
    print("Here is the list of the long words:\n"+str(longest_list))
    return longest_list
>>>

Here are the letters to use "ologohuta"

Here is the list of the long words:
['galoot', 'galuth', 'goolah']