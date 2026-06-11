def dsj_topic():
  print ("weapons of math destruction chapter 3")
  
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
