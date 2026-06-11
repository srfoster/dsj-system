def dsj_topic():
    space = '-----'
    old_guess = 0
    word = ''

    while True:
        print(
        "You'll be trying to guess some numbers of certain thing\n"
        "Guess it right and you'll move on\n"
        "All of these will use whole numbers\n"
        )
        start = input("If you are ready, click enter\n"
        'If you want to go back, type "Back"\n')

        if start.lower() == 'back':
            break

        else:
            while True:
                true_num = 75

                new_guess = float(input(
                'What number did I choose?(just the number)\n'))



                #sees if you increase or decrease by small amounts (for fun)
                if abs(new_guess - old_guess) <= 5:
                    if new_guess >= 60 and new_guess <= 80:
                        None
                    else:
                        print("If you're just gonna increase or decrease by small amounts, you're boring\nanyways")

                #checks if new guess is different from old (higher or lower)
                if (old_guess<75 and new_guess>75) or (old_guess>75 and new_guess<75):
                    word = ''

                #checks guess
                if new_guess > 75:
                    if new_guess > 90:
                        print(f"You're {word}too high.\n")
                    elif new_guess > 80:
                        print(f"You're {word}so close, but still too high.\n")
                    else:
                        print(f"Come on! You're {word}THIS close, but still too high\n")
                elif new_guess < 75:
                    if new_guess < 60:
                        print(f"You're {word}too low.\n")
                    elif new_guess < 70:
                        print(f"You're {word}so close, but still too low.\n")
                    else:
                        print(f"You're {word}THIS close, but still too low\n")
                else:
                    if old_guess == 0:
                        print('\nGuessed it on the first go. Nice :D')
                    print("Yup it's 75%. Information will be added later (Hopefully soon)")
                    break

                word = 'still '
                old_guess = new_guess

            start = input('keep going or go back')

            if start.lower() == ('back') or ('exit'):
                break
            else:
                print("I'm still working on more")
                break

    print('\nHope to see you again\n')
