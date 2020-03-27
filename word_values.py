import string

alpha_list = list(string.ascii_lowercase)

number_goal = int(raw_input("What is your goal number to achieve: "))


def get_word_value(word):
    stripped_word = word.replace(" ", "")
    word_value = 0
    message = "Congratulations! You did it!"
    for letter in stripped_word.lower():
        letter_value = alpha_list.index(letter) + 1
        word_value = word_value + letter_value
    if word_value < number_goal:
        message = "That's too low :("
    elif word_value > number_goal:
        message = "Calm down! That's too high."
    print("%s\n%d" % (message, word_value))


keep_going = True
while(keep_going):
    input_word = raw_input("Give me somethin' to try > ")
    if input_word == "quit":
        keep_going = False
    else:
        get_word_value(input_word)
