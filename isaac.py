def dsj_topic():
    play_intro()
    openended_questions()
    multiple_choice1()


def play_intro():
    print ("Welcome to questions about the 'Communist Manifesto' by Karl Marx.")

def openended_questions ():
    question_bank= ['One communist was asked: "What are such principles (of communism)? Answer: For example, every individual strives to be happy. The happiness of the individual is inseparable from the happiness of all, etc."\n     What do you think are principals of communism?\n',
 'The Communist Manifesto was written by Marx in 1947, Do you see much of the communist ideals in society (media, politicians, policy) today?\n',
    "What is a benefit or consequence of adopting these ideals historically (today to the past)?\n",
    "Who benefits the most?\n",
    "Give an estimation of what portion of the population is benefiting and what portion of the population is negatively affected?\n",
    '''A quote from the Communist Manifesto: "Modern bourgeois society, with its relations of production,
of exchange and of property, a society that has conjured up such gigantic means of production and of
exchange, is like the sorcerer who is no longer able to control the powers of the nether world whom
he has called up by his spells…. In these crises, a great part not only of the existing products, but
also of the previously created productive forces, are periodically destroyed. (pg 17)"

    Marx believed that all societies come to a boiling point in which the ‘owners’ can no longer control
    the ‘workers’ and so an uprising would be upon us. Do you see evidence of an uprising? What is the
    evidence?\n''', '"The proletariat goes through various stages of development. With its birth begins its struggle with the bourgeoisie. At first the contest is carried on by individual labourers, then by the workpeople of a factory, then by the operative of one trade, in one locality, against the individual bourgeois who directly exploits them. They direct their attacks not against the bourgeois conditions of production, but against the instruments of production themselves; they destroy imported wares that compete with their labour, they smash to pieces machinery, they set factories ablaze, they seek to restore by force the vanished status of the workman of the Middle Ages."\n     Is their anger targeted correctly?\n'
    ]
    count = 0
    #loops through list question_bank
    while count <= len(question_bank) - 1:
        #prints question number
        print(f"{count + 1}.")
        #asks the question with a user opportunity to input answer
        input(question_bank[count])
        count += 1
def multiple_choice1 ():
    question = '5.\nA quote from the Communist Manifesto: "At this stage, the labourers still form an incoherent mass scattered over the whole country, and broken up by their mutual competition. If anywhere they unite to form more compact bodies, this is not yet the consequence of their own active union, but of the union of the bourgeoisie, which class, in order to attain its own political ends, is compelled to set the whole proletariat in motion, and is moreover yet, for a time, able to do so. At this stage, therefore, the proletarians do not fight their enemies, but the enemies of their enemies, the remnants of absolute monarchy, the landowners, the non-industrial bourgeois, the petty bourgeois. Thus, the whole historical movement is concentrated in the hands of the bourgeoisie; every victory so obtained is a victory for the bourgeoisie." \nWhy does Marx say proletarians are fighting enemies of their enemies? How does this help the bourgeoisie?'

    #define answer choices
    choices = ["A) It doesn’t help the bourgeoisie", "B) The proletarians are helping solidify the power dynamics of capitalism", "C) Union reps are empowered", "D) Bourgeoisie are making money in the stock market"]

    #define the correct answer
    correct_answer = "B"

    #display question
    print(question)

    #display each choice
    for choice in choices:
        print(choice)

    #user input
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    #check correctness
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The correct answer was:", correct_answer)
    print("Game Over")
