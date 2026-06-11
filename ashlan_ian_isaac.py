def dsj_topic():
  #isaac
 questions = ['“Clifford learned that he had bombed on a teacher evaluation, a so-called value-added model, similar to the one that led to Sarah Wysocki’s firing.”\nWhere have you seen so called ‘value-added’ models in your life?', 
'Clifford states: “I didn’t see how it was possible that could have worked so hard and gotten such poor results”\nHave you been disappointed by the results of a model despite your hard work? Where?',
'Clifford states: “You’d think I’d have been elated, but I wasn’t, I knew that my low score was bogus, so I could hardly rejoice at getting a high score using the same flawed formula.”\nWould you be able to forgive the model if you first got a poor score?',
]

counter = 0
while counter<=len(questions)-1:
    print(questions[counter])
    input()
    counter += 1
#ashlan
    amount = 2
    correct = 0
    possible_answers = ""
    print("dummy intro")
    #question 1
    while amount >= 1:
        print("Passage: 'The Obama Administration realized early on that school districts punished under the 2001 No Child Left Behind reforms, which mandated high-stakes standardized testing, tended to be poor and disadvantaged. So it offered waivers to districts that could demonstrate the effectiveness of their teachers, ensuring that these schools would not be punished even if their students were lagging.'")
        print(f"According to this passage, what did the Obama Administration do in response to the No Child Left Behind Act? {amount}/2")
        possible_answers = input("a) offered waivers b) ignored the schools c) punished them more d) awarded them")
        if possible_answers == "a":
            print("Correct!")
            correct += 1
            break
        else:
            print("Incorrect.")
            break
    #question 2
    amount = 2
    while amount >= 1:
        print(f"Fill in the blank: 'But in late 2015… Congress and the White House agreed to [blank] No Child Left Behind Act' {amount}/2")
        possible_answers = input("a) enforce b) revoke (correct) c) ignore d) vote on the")
        if possible_answers == "b":
            print("Correct!")
            correct += 1
            break
        else:
            print("Incorrect.")
            break

    #question 3
    amount = 2
    while amount >= 1:
        print(f"True or false, the No Child Left Behind Act had the opposite effect of its enactment. {amount}/2")
        possible_answers = input("true or false")
        if possible_answers == "true":
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
          
  question = "The value-added model had given him a failing grade but no advice on how to improve it"
  answer = "false"
  ToF(question,answer)
  
  question = "Tim Clifford made changes to his teaching in order to change his score"
  answer = "true"
  ToF(question,answer)
  
  question = "The No Child Left Behind Act had the opposite effect of its enactment"
  answer = "false"
  ToF(question,answer)
