def dictionary_reader() -> Tuple[str, str]:
    """Opens the text file containg the dictionary and
       iterates through each line adding the words to a list"""
    sorted_dictionary = []
    with open("2letterwords.txt", "r") as words:
        dictionary = words.read().splitlines()
    words.close()
    normal_dictionary = [line for line in dictionary if len(line) < 10]
    normal_dictionary = [x.lower() for x in normal_dictionary]
    for element in normal_dictionary:
        alphabetical = "".join(sorted(element))
        sorted_dictionary.append(alphabetical.lower())
    print("Here is the normal dictionary\n" + str(normal_dictionary))
    print("\nHere is the sorted_dictionary dictionary\n" + str(sorted_dictionary))
    return normal_dictionary, sorted_dictionary
>>>

Here is the normal dictionary
['am', 'an', 'as', 'at', 'go', 'if', 'in', 'is', 'it', 'ma', 'me', 'my', 'no', 'of', 'oh', 'on', 'or', 'ox', 'pa', 'so', 'to', 'up', 'we']

Here is the sorted_dictionary dictionary
['am', 'an', 'as', 'at', 'go', 'fi', 'in', 'is', 'it', 'am', 'em', 'my', 'no', 'fo', 'ho', 'no', 'or', 'ox', 'ap', 'os', 'ot', 'pu', 'ew']