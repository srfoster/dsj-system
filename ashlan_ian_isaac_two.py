def dsj_topic():
    play_intro()
    quiz_isaac()
    quiz_ashlan()
    quiz_ian()

def play_intro(): #plays explanatory intro
    print("This module is based on the book Weapons of Math Destruction by Cath O'Neil, focusing specifically on Chapter 3. This module is a quiz that includes open ended questions, multiple choice questions, and true/false questions.")
    print("Created by Ashlan Koose, Ian-Robert Palmer, and Isaac Holloway.")
    print()

def quiz_isaac():
    #isaac's questions and code
    questions = ['How much of the ranking should be on student fulfillment vs student test scores, student to teacher ratios and acceptance rates?']

    counter = 0
    while counter<=len(questions)-1:
        print(questions[counter])
        input()
        counter += 1

def quiz_ashlan():
    #ashlan's questions and code
    #question 1
    possible_answers = ""
    print("Passage: 'However, when you create a model from proxies, it is far simpler for people to game it. This is because proxies are easier to manipulate than the complicated reality they represent. Here’s an example … So the hiring manager settles on a proxy. She gives strong consideration to applicants with the most followers on Twitter.'")
    print("According to this passage, what is a proxy (be specific)?")
    possible_answers = input("a) Passage does not give enough information b) Twitter followers. c) the work value of someone d) an arbitrary value")
    if possible_answers == "d":
        print("Correct!")
    else:
        print("Incorrect.")

    #question 2
    print("Fill in the blank, 'The [blank], or course, are the vast majority of Americans, the poor and middle-class families who don’t have thousands of dollars to spend on courses and consultants.'")
    possible_answers = input("a) winners b) users c) victims d) aggressors")
    if possible_answers == "c":
        print("Correct!")
    else:
        print("Incorrect.")

def quiz_ian():  
    #ian's questions and code
    question = "Baylor University paid for admitted students to retake the SAT, hoping another try would boost their scores"
    answer = "true"
    ToF(question,answer)
    question = "Our society does not care for college education and does not value it."
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
