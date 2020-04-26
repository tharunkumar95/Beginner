def vowels_and_consonants(my_str, vowels):

    vowel_list = [vowel for vowel in my_str if vowel in vowels]
    for vw in vowel_list:
        print(vw)

    consonant_list = [cons for cons in my_str if cons not in vowels]
    for con in consonant_list:
        print(con)

def main():
    # javascriptloops
    my_str = str(input())
    vowels = 'aAeEiIoOuU'
    vowels_and_consonants(my_str, vowels)


if __name__ == '__main__':
    main()