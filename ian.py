def dsj_topic():
    #Number guessing question
    def GuessGame(correct_num, question):
        old_guess = 0
        word = ''
        num_guesses = 0

        while True:
            num_guesses = num_guesses + 1 #tracks how many guesses

            print(question)
            new_guess = float(input("Guess a number: "))

            #checks if new guess is different from old (higher or lower)
            if (old_guess<correct_num and new_guess>correct_num) or (old_guess>correct_num and new_guess<correct_num):
                word = ''

            #checks guess
            if new_guess > correct_num:     #too high
                if new_guess > correct_num + 15:
                    print(f"You're {word}too high.\n")
                elif new_guess > correct_num + 5:
                    print(f"You're so close, but still too high.\n")
                else:
                    print(f"Come on! You're THIS close, but still too high\n")

            elif new_guess < correct_num:   #too low
                if new_guess < correct_num - 15:
                    print(f"You're {word}too low.\n")
                elif new_guess < correct_num - 5:
                    print(f"You're so close, but still too low.\n")
                else:
                    print(f"You're THIS close, but still too low\n")

            else:                           #correct
                if num_guesses == 1:
                    print('\nGot it on the first go. Nice :D')
                break

            word = 'still '
            old_guess = new_guess
        print(f"Correct, the answer is {correct_num}")

    #True or False questions
    def ToF(answer, question):
        print(question)
        guess = input('True or False: ')

        if guess == answer:
            print('Correct\n')
        else:
            print("Incorrect\n")

    while True:
        print(
        "Welcome to my section on the Gender Work Gap\n"
        "While part of it is the gender pay gap\n"
        "I'll mainly be going other parts that people don't really notice\n"
        "Information based on the book: Invisible Women by Caroline Criado Cerez\n")

        start = input("If you are ready to begin, enter anything\n"
        "To go back to main page, enter Exit\n")
        if start.lower() == 'exit':
            break

        print("-----\nI'll be asking some questions and you will be tring to quess the right answer\n"
        "Some questions you will have to guess multipule times till you get the right number\n"
        "While some are just True or False\n-----\n")

        #question 1
        print("First Question")
        num = 75
        quetion = "What percent of unpaid work (work and home related) do you think is done by women?"
        GuessGame(num, quetion)
        print("Women spend three and six hours per day on unpaid work\ncompared to men’s average of thirty minutes to two hours\n")

        #question 2
        print("-----\nSecond Question\n"
        "Continuing of the previous question")
        num = 61
        question = "What percent of just household work on average do you think is done by women?"
        GuessGame(num, quetion)
        print("Women spend on average 6 hours on household work compared to men who spend on average 30 minutes\n"
        "I understand not all men are like this but this is what the book says\n"
        "-----\n")

        start = input("To continue, enter anything\nTo go back to main page, enter Exit: ")
        if start.lower() == "exit":
            break

        #question 3
        print("\n-----\nThird Question")
        num = "true"
        question = "Women have higher rates of work-related stress, anxiety, and depression than men."
        ToF(num, question)
        print("Women are overall 53% more stressed than men\n"
        "The HSE concluded that this is because stress is more prevalent in public service industries, such as education, health and social care\n"
        "as well as curltural differences between men and women\n-----")

        #question 4
        print("Forth Question\n"
        "A 2016 paper on the impact of long work hours over a thirty-two-year period found that")
        num = "false"
        question = "working moderately long hours was ‘associated with less risk of contracting heart disease, chronic lung disease, or depression’ in men and women"
        ToF(num, question)
        print("The paper said that it would actually increase the risk of life-threatening diseases despite stating the work hours between men and women are the same\n"
        "This isn't because women are weaker, just that there are other work women do that goes unnoticed\n\n-----")
        
        print("You made it through my little quiz :D")
        again = input("If you would like to exit to the main page, enter anything\nIf you would to go again, enter Again: ")
        if again.lower() == "again":
            print("-----\n")
        else:
            break
        
    print('\nHope to see you again\n\n-----')
