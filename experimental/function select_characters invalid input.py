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
                             +" Type 'c' for a consonant or 'v' for a vowel: "))
        if response == 'c':
            if consonant_count == 8:
                print("Automatically selected a vowel to match criteria")
                letters_string += choice(vowels, p=vowel_weight)
                vowel_count += 1
            else:
                letters_string += choice(consonants, p=consonant_weight)
                consonant_count += 1
        elif response == 'v':
            if vowel_count == 8:
                print("Automatically selected a consonant to match criteria")
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
>>>
__        __   _                            _____     
\ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/ 
                                                  
  ____                  _      _                     _ 
 / ___|___  _   _ _ __ | |_ __| | _____      ___ __ | |
| |   / _ \| | | | '_ \| __/ _` |/ _ \ \ /\ / / '_ \| |
| |__| (_) | |_| | | | | || (_| | (_) \ V  V /| | | |_|
 \____\___/ \__,_|_| |_|\__\__,_|\___/ \_/\_/ |_| |_(_)
                                                       
Please select 9 letters
Please include a minimum of one vowel and one consonant

Select letter 1 - Type 'c' for a consonant or 'v' for a vowel: hello world
Please answer with only 'c' or 'v'
Select letter 1 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 2 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 3 - Type 'c' for a consonant or 'v' for a vowel: _
Please answer with only 'c' or 'v'
Select letter 3 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 4 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 5 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 6 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 7 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 8 - Type 'c' for a consonant or 'v' for a vowel: c
Select letter 9 - Type 'c' for a consonant or 'v' for a vowel: c
Automatically selected a vowel to match criteria
Press enter to view the letters generated 

Here are the letters to use "lkskdnrji"