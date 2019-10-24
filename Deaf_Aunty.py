
def deaf_aunty():
    exit_loop = False
    my_name = input('What is your name? ')

    while not exit_loop:
        userInput = input("Speak Child... :")

        if userInput == "I love you aunty, I have to go now":
            print("ok. Goodbye. Don't come back...")
            print(f"{my_name}, are you there?")
            
            reply1 = input('Your reply: ')
            reply2 = input('Your reply: ')
            if reply1 == "" and reply2 == "":
                print('Dumb Bitch...')
                exit_loop=True
            else:
                print('You little shit!')

        elif userInput.isupper():
            print('YOU ARE VERY RUDE!')
        elif userInput.islower():
            print('WHAT? SPEAK UP!')
        elif not userInput.islower() and not userInput.isupper():
            print('SHOW SOME RESPECT!')



deaf_aunty()
