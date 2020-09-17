from random import sample, randint
from random import shuffle


def generate_word():
    vowels = 'eeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaiiiiiiiiiiiiiooooooooooooouuuuu'
    consonants = 'bbcccddddddffggghhjklllllmmmmnnnnnnnnppppqrrrrrrrrrssssssssstttttttttvwxyz'
    n_vowels = randint(3, 5)
    vowels = sample(vowels, n_vowels)
    consonants = sample(consonants, 9 - n_vowels)
    letters = vowels + consonants
    print(letters)
    shuffle(letters)
    word = ''.join(letters)
    print(word)


def main():
    generate_word()


if __name__ == '__main__':
    main()
