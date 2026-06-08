def dsj_topic():
	answers_to_question_1 = ["A. The sophists are right, and you concur.", "B. Justice is what is fair and good to everyone", "C. You say nothing"]
	answers_to_question_2 = ["A. Only strong, because it is better to be feared than to know", "B. Only wise, because it is better to know than it is to be ignorant", "C. Both wise and strong, a philosopher-king should have ample experience in both life and academics."]
	answers_to_question_3 = []
	answers_to_question_4 = []
	flag_1 = True
	flag_2 = False
	flag_3 = False
	flag_4 = False
	print("-----Welcome to Plato's Cave-----")
	print()
	print("This is a text-based adventure where you must answer 4 questions correctly in sequence, otherwise you will not escape!")
	print("There are two people, sophists, on each side of you that will prevent you from leaving, so answer wisely. ")
	
	while flag_1:
		print("First question - **Your chains are broken magically and the others take note.**")
		print("---------------")
		print("Plato asks, 'what is justice?'")
		print("The sophists respond that justice is what benefits the strongest. Plato then turns to you and you say: ")
		
		for answer in answers_to_question_1:
			print(answer)
		response = input("")
		if response.strip().lower() == 'a':
			print("Plato smiles, then says you are wrong, because he knows the truth.")
			print("**Your chains are now on you and you remain in ignorance.**")
			flag_1 = False
		elif response.strip().lower() == 'b':
			print("Plato looks to you and says, 'you are showing potential for wisdom', you are correct, and you see a bright light.")
			flag_2 = True
			flag_1 = False
			
		elif response.strip().lower() == 'c':
			print("Plato is upset by your lack of realizing of possibility, you remain in ignorance.")
			flag_1 = False
		else:
			print("Please choose an option")
	
	while flag_2:
		print("The bright light is coming from the fire that not even the sophists can see. You are blinded, but eventually you get used to the fire.")
		print("The sophists see that you are seeing differently, but don't know how, Plato is still here, and he has another question (as always).")
		print("---------------")
		print("Should a philosopher-ruler be strong or wise?")
		for answer in answers_to_question_2:
			print(answer)
		response = input("")
		if response.strip().lower() == 'a':
			print("Plato smiles, then says you are wrong, because he knows the truth.")
			print("**Your chains are now on you and you remain in ignorance.**")
			flag_2 = False
		elif response.strip().lower() == 'b':
			print("Plato laughs, then says, 'it is good to be wise but it is best to be both', you remain in ignorance and your chains bind you like the others. ")
			flag_2 = False
			
		elif response.strip().lower() == 'c':
			print("Plato looks to you and says, 'you are growing in wisdom', you are correct, and you see the source of an even brighter light, the sun.")
			flag_2 = False
			flag_3 = True
			
		else:
			print("Please choose an option")
		
			
		
		
	
	
	
	
	
	
	
dsj_topic()
