import random

def display_menu():
    print('''
        1. Type 1 if you choose to play with cities
        2. Type 2 if you choose to play wiyh countries
        3. Type 0 to exit
    ''')
    choice = ""
    while choice == "" :
        choice = input("Choose one of the options listed above:")
        if choice not in ["1", "2", "0"]:
            choice = ""
            print("Invalid input.")
    return choice

def choose_word(word_list):
    # random.shuffle(word_list)
    # return word_list[0]
    result = random.choice(word_list)
    return result
    # index = random.randint(0, len(word_list)-1)
    # return word_list[index]


def mask_word(word, letter_mask="_ "):
    result = ""
    for letter in word:
        result = result + letter_mask
    return result

def play(word, lives):
    word = word.lower()
    masked_word = mask_word(word)
    print(masked_word)\

    word_as_list = list(word)
    masked_word_as_list = list(masked_word)

    while masked_word != word and lives > 0:
        user_input = input("Type your guess:").lower()

        #!!!!!!!verify if input is letter => ord() chr() ASCII code

        # for index, word_letter in enumerate(word_as_list):
        #     if word_letter == letter:
        #         masked_word_as_list[index*2] = letter
        if user_input == word:
            print("You won!")
            break
        if user_input not in word_as_list:
            lives = lives -1
        else:
            for i in range(len(word_as_list)):
                if word_as_list[i] == user_input:
                    masked_word_as_list[i*2] = user_input
                    masked_word_as_list[i*2+1] = ""
        masked_word = "".join(masked_word_as_list)
        print(masked_word)
    print

cities = ["Oslo", "Viena"]

my_word = choose_word(cities)

play(my_word, 1)

# cities = ["Oslo", "Viena"]


# 0. Definire meniu joc
# 1. Alegerea cuvantului de ghicit
# 2. Trebuie sa maschez cuvantul


# 3. Joaca
#     a) trebuie sa verific daca mai am vieti
#     b) trebuie sa verific daca ce s-a introdus e litera
#     c) afisare mesaje succes sau fi
#     d) afisare optiune play again

# play('Codecool', 6)
