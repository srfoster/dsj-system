def dsj_topic():
    play_intro()
    quiz_isaac()
    quiz_ashlan()
    quiz_ian()

def play_intro(): #plays explanatory intro
    print("This module is based on the book Weapons of Math Destruction by Cath O'Neil, focusing specifically on Chapter 7. This module is a quiz that includes open ended questions, multiple choice questions, and true/false questions.")
    print("Created by Ashlan Koose, Ian-Robert Palmer, and Isaac Holloway.")
    print()

def quiz_isaac():
    #isaac's questions and code
    questions = ['“Clifford learned that he had bombed on a teacher evaluation, a so-called value-added model, similar to the one that led to Sarah Wysocki’s firing.”\nWhere have you seen so called ‘value-added’ models in your life?', 
    'Clifford states: “I didn’t see how it was possible that could have worked so hard and gotten such poor results”\nHave you been disappointed by the results of a model despite your hard work? Where?',
    'Clifford states: “You’d think I’d have been elated, but I wasn’t, I knew that my low score was bogus, so I could hardly rejoice at getting a high score using the same flawed formula.”\nWould you be able to forgive the model if you first got a poor score?',
    ]

    counter = 0
    while counter<=len(questions)-1:
        print(questions[counter])
        input()
        counter += 1

def quiz_ashlan():
    #ashlan's questions and code
    possible_answers = ""
    #question 1
    print("Passage: 'The Obama Administration realized early on that school districts punished under the 2001 No Child Left Behind reforms, which mandated high-stakes standardized testing, tended to be poor and disadvantaged. So it offered waivers to districts that could demonstrate the effectiveness of their teachers, ensuring that these schools would not be punished even if their students were lagging.'")
    print("According to this passage, what did the Obama Administration do in response to the No Child Left Behind Act?")
    possible_answers = input("a) offered waivers b) ignored the schools c) punished them more d) awarded them")
    if possible_answers == "a":
        print("Correct!")
    else:
        print("Incorrect.")

    #question 2
    print("Fill in the blank: 'But in late 2015… Congress and the White House agreed to [blank] No Child Left Behind Act'")
    possible_answers = input("a) enforce b) revoke c) ignore d) vote on the")
    if possible_answers == "b":
        print("Correct!")
    else:
        print("Incorrect.")

def quiz_ian():  
    #ian's questions and code
    question = "The value-added model had given him a failing grade but no advice on how to improve it"
    answer = "false"
    ToF(question,answer)
    
    question = "Tim Clifford made changes to his teaching in order to change his score"
    answer = "true"
    ToF(question,answer)
    
    question = "The No Child Left Behind Act had the opposite effect of its enactment"
    answer = "false"
    ToF(question,answer)

#this is also part of Ian's code
def ToF(question, answer):
    print(question)
    guess = input('True or False: ')
    if guess == answer:
        print('Correct\n')      
    else:
        print("Incorrect\n")

'''
ending notes:
When our group met up on Thursday, June 11, in the afternoon, Isaac was not able to edit the shared github repository, so what we had him do was copy/paste his code
onto the shared Google Doc, and I added his code for the co-authored file for him, so we wouldn't have to wait.
We decided to write some questions individually and write code for each of the questions and add them to the file. I volunteered to
fix any bugs and errors up later, and added a quick intro. -Ashlan Koose
'''
