#information given is based on this paper. https://pmc.ncbi.nlm.nih.gov/articles/PMC5453398/

error = 1
def play_intro(): #plays explanatory intro
    print("The experience of economic inequality in everyday life. Learn about how our perception of others effects our day to day understanding of economic inquality.")
    print("In this program, you have the option to practice and learn the information in three different ways, as well as quiz yourself.")

def dsj_topic(): #the introduction. If the user enters nonsense at least five times it'll exit the program and return to main
    global error
    play_intro()
    pick = input("To begin, chose to either practice (recommended for new users) or play the quiz. Enter 'practice' for practice, 'quiz' for quiz, or 'exit' to exit.")
    if pick == "quiz":
        quiz()
    elif pick == "practice":
        pick_two = int(input("You have chosen practice. Pick one of the options to practice. True or false or fill in the blank. (enter 1 or 2)"))
        if pick_two == 1:
            practice_true_false()
        elif pick_two == 2:
            practice_fill_blank()
        elif pick_two != 1 and pick_two != 2:
            error += 1
            print(f"{pick_two} is not valid input. Read the instructions carefully.")
            dsj_topic()
    elif error == 5:
        print("It's clear you don't want to learn. Goodbye.")
        return
    elif pick == "exit":
        print("Exiting program")
        return
    elif pick != "quiz" and pick != "practice":
        error += 1
        print(f"{pick} is not valid input. Read the instructions carefully.")
        dsj_topic()

def quiz():
    amount = 2
    correct = 0
    possible_answers = ""
    print("You have reached the quiz. There are 10 questions, being a mix of true or false and fill in the blank. To answer true or false questions, enter 'true' or 'false', to answer fill in the blank questions, enter the letter 'a', 'b'.... Any nonsense input will be marked as incorrect. You have two attempts to answer each question. Good luck!")
    #question 1
    while amount >= 1:
        print(f"People of higher social class standing view lower social class others as outgroup members who are less human, less warm, and less competent than their same class counterparts and each of these perceptions is likely to create a compassion barrier. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "true":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break
    #question 2
    amount = 2
    while amount >= 1:
        print(f"Schools and neighborhoods are often segregated in terms of [blank], with many explicit home lending policies favoring neighborhood separation based on [blank]. {amount}/2")
        possible_answers = input("a) social class b) politics c) family size d) home size")
        if possible_answers == "a":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "a":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 3
    amount = 2
    while amount >= 1:
        print(f"Lower class individuals tend to trust the political system more, and participate in general elections more than upper class individuals. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "false":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "false":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 4
    amount = 2
    while amount >= 1:
        print(f"In roughly 70% of studies examining the health impacts of economic inequality, data indicates that societal health [blank] as economic inequality intensifies. {amount}/2")
        possible_answers = input("a) stays the same b) improves c) worsens d) cat")
        if possible_answers == "c":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "c":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 5
    amount = 2
    while amount >= 1:
        print(f"One of the most pervasive domains of person perception is the voice, and much research supports the utility of aspects of speech—including word choice and linguistic and paralinguistic vocal patterns—in signaling various forms of social status. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "true":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 6
    amount = 2
    while amount >= 1:
        print(f"Though [blank] style varies by region and cultural background, it is also determined by social class: For instance, studies find that students from lower social class backgrounds are more likely to [blank] using nonstandard dialects than relatively upper class individuals. {amount}/2")
        possible_answers = input("a) speech, speak b) hearing, hear c) hair, style d) clothing, dress")
        if possible_answers == "a":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "a":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 7
    amount = 2
    while amount >= 1:
        print(f"When economic inequality grows, ideas that society is fair widen. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "false":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "false":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 8
    amount = 2
    while amount >= 1:
        print(f"[blank] determines the foods people eat, the music and art they enjoy, the leisure activities people engage in, the linguistic patterns they employ, and the clothing they wear. {amount}/2")
        possible_answers = input("a) region b) nationality c) language d) class")
        if possible_answers == "d":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "d":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 9
    amount = 2
    while amount >= 1:
        print(f"According to a study done, when resources are visible, participants shared their resources with other resource-rich individuals, thereby perpetuating economic inequality. In contrast, when resources were invisible, participants shared regardless of the resources of their partners, thereby reducing economic inequality. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "true":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break

    #question 10
    amount = 2
    while amount >= 1:
        print(f"Research on social comparison indicates that people compare themselves to others frequently on [blank] dimensions. {amount}/2")
        possible_answers = input("a) clothing choice b) economic c) appearance d) cat")
        if possible_answers == "b":
            print("Correct!")
            correct += 1
            break
        elif possible_answers != "a":
            amount = amount - 1
            if amount >= 1:
                again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
                if (again == "try again"):
                    continue
                else:
                    break
            elif amount == 0:
                break
    final = input(f"You have reached the end of the quiz. Your total score: {correct}/10. Enter 'try again' to return to the opening module, or any input to exit this dsj module.")
    if final == "try again":
        dsj_topic()
    else:
        return
#def practice_multi_choice():
#    print("You have reached the practice, multiple choice.")
#There was originally going to be a third section, and 15 total questions
#but I was running out of ways to rewrite and word questions without repeating information
#Now that it's all done and the longest program I've ever written for a class assignment I think it's fine

def practice_true_false():
    possible_answers = ""
    print("You have reached the practice, true or false. There are five questions, and each question as the option of either true, or false. Enter true or false to answer. Nonsense responses will be counted as incorrect.")
    #question 1
    while possible_answers == "":
        print("People of higher social class standing view lower social class others as outgroup members who are less human, less warm, and less competent than their same class counterparts and each of these perceptions is likely to create a compassion barrier.")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 2
    while possible_answers == "":
        print("Lower class individuals tend to trust the political system more, and participate in general elections more than upper class individuals.")
        possible_answers = input("true or false")
        if possible_answers == "false":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 3
    while possible_answers == "":
        print("One of the most pervasive domains of person perception is the voice, and much research supports the utility of aspects of speech—including word choice and linguistic and paralinguistic vocal patterns—in signaling various forms of social status.")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 4
    while possible_answers == "":
        print("When economic inequality grows, ideas that society is fair widen.")
        possible_answers = input("true or false")
        if possible_answers == "false":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 5
    while possible_answers == "":
        print("According to a study done, when resources are visible, participants shared their resources with other resource-rich individuals, thereby perpetuating economic inequality. In contrast, when resources were invisible, participants shared regardless of the resources of their partners, thereby reducing economic inequality.")
        possible_answers = input("true or false")
        if possible_answers == "true":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    final = input("You have reached the end of the true or false practice questions. Enter 'try again' to restart the practice, or any input to return to the opening module.")
    if final == "try again":
        practice_true_false()
    else:
        dsj_topic()

def practice_fill_blank():
    possible_answers = ""
    print("You have reached the practice, fill in the blank. There are five questions, and each question has a group of possible answers. Type the letter of the answer you think the most correct. Nonsense responses will be counted as incorrect.")
    #question 1
    while possible_answers == "":
        print("Schools and neighborhoods are often segregated in terms of [blank], with many explicit home lending policies favoring neighborhood separation based on [blank].")
        possible_answers = input("a) social class b) politics c) family size d) home size")
        if possible_answers == "a":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 2
    while possible_answers == "":
        print("In roughly 70% of studies examining the health impacts of economic inequality, data indicates that societal health [blank] as economic inequality intensifies.")
        possible_answers = input("a) stays the same b) improves c) worsens d) cat")
        if possible_answers == "c":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 3
    while possible_answers == "":
        print("Though [blank] style varies by region and cultural background, it is also determined by social class: For instance, studies find that students from lower social class backgrounds are more likely to [blank] using nonstandard dialects than relatively upper class individuals.")
        possible_answers = input("a) speech, speak b) hearing, hear c) hair, style d) clothing, dress")
        if possible_answers == "a":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 4
    while possible_answers == "":
        print("[blank] determines the foods people eat, the music and art they enjoy, the leisure activities people engage in, the linguistic patterns they employ, and the clothing they wear.")
        possible_answers = input("a) region b) nationality c) language d) class")
        if possible_answers == "d":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    #question 5
    while possible_answers == "":
        print("Research on social comparison indicates that people compare themselves to others frequently on [blank] dimensions.")
        possible_answers = input("a) clothing choice b) economic c) appearance d) cat")
        if possible_answers == "b":
            print("Correct!")
        else:
            again = input("Incorrect. Either try again, or move onto the next question. Enter 'try again' to try again, or any input to move on.")
            if (again == "try again"):
                possible_answers = ""
    final = input("You have reached the end of the fill in the blank practice questions. Enter 'try again' to restart the practice, or any input to return to the opening module.")
    if final == "try again":
        practice_fill_blank()
    else:
        dsj_topic()
