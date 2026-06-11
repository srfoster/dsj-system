def dsj_topic():
  print ("weapons of math destruction chapter 3")
  #isaac
  questions = ['How much of the ranking should be on student fulfillment vs student test scores, student to teacher ratios and acceptance rates?']

counter = 0
while counter<=len(questions)-1:
    print(questions[counter])
    input()
    counter += 1

  
  #ashlan
      amount = 2
    while amount >= 1:
        print("Passage: 'However, when you create a model from proxies, it is far simpler for people to game it. This is because proxies are easier to manipulate than the complicated reality they represent. Here’s an example … So the hiring manager settles on a proxy. She gives strong consideration to applicants with the most followers on Twitter.'")
        print(f"According to this passage, what is a proxy (be specific)? {amount}/2")
        possible_answers = input("a) Passage does not give enough information b) Twitter followers. c) the work value of someone d) an arbitrary value")
        if possible_answers == "d":
            print("Correct!")
            correct += 1
            break
        else:
            print("Incorrect.")
            break

    #question 3
    amount = 2
    while amount >= 1:
        print(f" Fill in the blank, 'The [blank], or course, are the vast majority of Americans, the poor and middle-class families who don’t have thousands of dollars to spend on courses and consultants.'")
        possible_answers = input("a) winners b) users c) victims d) aggressors")
        if possible_answers == "c":
            print("Correct!")
            correct += 1
            break
        else:
            print("Incorrect.")
            break
  
  #ian
  def ToF(question, answer):
    print(question)
    guess = input('True or False: ')
    
    if guess == answer:
        print('Correct\n')
        
    else:
        print("Incorrect\n")
  
  question = "Baylor University paid for admitted students to retake the SAT, hoping another try would boost their scores"
  answer = "true"
  ToF(question,answer)
  
  question = "Our society does not care for college education and does not value it."
  answer = "false"
  ToF(question,answer)
