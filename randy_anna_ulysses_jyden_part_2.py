# Chapter 10 - Questions & Code

def ulysses():
	answer_list_chap_10_question_1 = ["A. Microsoft", "B. Facebook", "C. Twitter (now X)", "D. Youtube"]
	answer_list_chap_10_question_2 = ["A. Mitt Romney", "B. Bill Clinton", "C. Hillary Clinton", "D. Barack Obama"]

	print("What company targeted users on their platform to increase voting patterns?")
	for answer in answer_list_chap_10_question_1:
		print(answer)
	while True:
		answer = input("Enter A, B, C, or D: ").strip().lower()
		if answer == 'a':
			print("Incorrect")
			break
		elif answer == 'b':
			print("Correct!")
			break
		elif answer == 'c':
			print("Incorrect")
		elif answer == 'd':
			print("Incorrect")
		else:
			print("Please type in a letter from the list")
	print("-------------------")
	print("What presidential candidate hired analysts to increase their odds of winning?")
	for answer in answer_list_chap_10_question_2:
		print(answer)
	while True:
		answer = input("Enter A, B, C, or D: ").strip().lower()
		if answer == 'a':
			print("Incorrect")
			break
		elif answer == 'b':
			print("Incorrect")
			break
		elif answer == 'c':
			print("Incorrect")
		elif answer == 'd':
			print("Correct!")
			break
		else:
			print("Please type in a letter from the list")
	print("-------------------")
			
def randy_question_three():
    print("Why is it difficult to hold campaigns accountable for misleading targeted political advertisements?")
    
    print("A. All targeted ads are reviewed by independent fact-checkers.")
    print("B. Targeted ads are often visible only to the selected audience receiving them.")
    print("C. Television stations approve every political advertisement before it airs.")
    print("D. Voters are required to report misleading ads to the government.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("Enter A, B, C, or D: ").upper()
        
    if answer == "B":
        print("Correct!")
    else: 
        while answer != "B":
            print("Not quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("Correct!")
        
    print("According to O'Neill, targeted ads are shown only to certain groups, misleading or contradictory messages may go unnoticed by the general public, journalists, and opposing campaigns.")
    
def randy_question_four():
    print("What makes targeted political advertising different from traditional television political advertising?")
    
    print("A. Targeted political ads use personal data to reach specific groups of voters with customized messages.")
    print("B. Targeted political ads are subject to stricter transparency requirements than television ads.")
    print("C. Television ads cannot influence voter behavior.")
    print("D. Targeted political ads are required to be shown equally to all registered voters.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("Enter A, B, C, or D: ").upper()
        
    if answer == "A":
        print("Correct!")
    else: 
        while answer != "A":
            print("Not quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("Correct!")
        
    print("According to O'Neil, unlike television ads that are broadcast to a broad audience, targeted political ads use data about voters' interests, demographics, and online behavior to deliver tailored messages designed to influence specific groups.")

def randy():
	randy_question_three()
	print("-------------------")
	randy_question_four()
	print("-------------------")

def jyden():
	print("What is O'Neil main concern about the Facebook news feed algorithms?")
	print("A. Shows too many advervisements")
	print("B.can shape political behvaior by controlling what the users see")
	print("C. Slows down trhe internet speed")
	print("D. Gets rid of political content entirely")

	answer=(input("Enter A, B, C, or D: ")).strip().lower()

	if answer=="b":
		print("Correct!")
		
	else:
		print("Incorrrect!. The answer is 'B'")

	print("-------------------")	

	print("What is the broader warning in Chapter 10?")
	print("A. Tech companies are going to create Skynet")
	print("B. Political campaigns are going to rethink using big data")
	print("C. Algorithms can quietly influence demacracy without public accountability")
	print("D. Furries are the real threat to demacracy")

	answer=(input("Enter A, B, C, or D: ")).strip().lower()

	if answer== "c":
		print("Correct!")
	else:
		print("Incorrect!. The answer is 'C'")
	
	print("-------------------")


def anna():
	print(" Because the content Facebook shows to each user is filtered and individualized, which of the following could cause political influence on a user because of the platform's filter?")
	print('''A. Only showing pessimistic status updates from the user's friends.
B. Not showing posts from any friends who hold different political beliefs than the user.
C. Mainly featuring posts from the user's politically involved friends.
D. Prioritizing posts from the user's friends about celebrating accomplishments or milestones.''')
	user_answer = (input("Enter A, B, C, or D: ")).strip().lower()

	if user_answer == "b":
		print("Correct!")
	else:
		print("Incorrect. The correct answer was B")

	print("-------------------")

	print("Which of the following is NOT a way politicians can deliver micro-targeted advertising?")
	print('''A. Facebook banners 
B. Direct mail
C. Campaign speeches
D. Emails''')	
	user_answer = (input("Enter A, B, C, or D: ")).strip().lower()

	if user_answer == "c":
		print("Correct!")
	else:
		print("Incorrect. The correct answer was C")

	print("-------------------")



group = [ulysses, randy, jyden, anna]   

def main():
    for student in group:
        student()
    print("You have now reached the end of the Chapter 10 questions.")
    print("Activity Complete")
