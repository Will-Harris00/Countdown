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
    print("Here is the list of matching words:\n" + str(word_list))
    return word_list
>>>
Here are the letters to use "ologohuta"

Here is the list of matching words:
['a', 'ago', 'agoho', 'ah', 'ah', 'aho', 'aht', 'ahu', 'al', 'al', 'alo',
 'alt', 'altho', 'alto', 'ao', 'aoul', 'at', 'augh', 'aught', 'auh', 'auto',
 'ga', 'ga', 'gal', 'galoot', 'galt', 'galuth', 'gaol', 'gat', 'gau', 'gaul',
 'gault', 'gault', 'gaut', 'ghat', 'ghoul', 'gloat', 'glout', 'glut', 'go',
 'goa', 'goal', 'goat', 'gol', 'gola', 'golo', 'goo', 'gool', 'goolah', 'got',
 'goth', 'gotha', 'gout', 'guao', 'guato', 'guha', 'gul', 'gula', 'gulo',
 'gut', 'ha', 'hag', 'hal', 'halo', 'halt', 'hao', 'hat', 'hau', 'haul', 'ho',
 'ho', 'hog', 'hoga', 'holt', 'hoot', 'hot', 'hu', 'hug', 'hugo', 'hula',
 'hut', 'la', 'lag', 'lao', 'lat', 'lath', 'laugh', 'lhota', 'lo', 'lo', 'loa',
 'loa', 'loath', 'log', 'loo', 'loot', 'lot', 'lot', 'lota', 'lota', 'lou',
 'lough', 'lout', 'lu', 'lug', 'lug', 'luo', 'lut', 'lutao', 'oat', 'oath',
 'og', 'oh', 'oho', 'olga', 'oto', 'ough', 'ought', 'out', 'outgo', 'ta',
 'tag', 'tal', 'tal', 'tao', 'tao', 'tau', 'th', 'tha', 'tho', 'tho', 'thoo',
 'thou', 'thug', 'to', 'toa', 'toag', 'tog', 'toga', 'toho', 'tol', 'tolu',
 'too', 'tool', 'tou', 'toug', 'tough', 'tu', 'tua', 'tug', 'tula', 'ug',
 'ugh', 'ula', 'ut', 'uta', 'uta', 'utah']