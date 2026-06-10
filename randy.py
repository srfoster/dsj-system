print("=====================================================")
print("              Wealth Gap Knowledge Quiz") 
print("Based on Pew Research Findings on Economic Inequality")
print("=====================================================\n")

def wealth_gap_questions():
    print("Question 1\n")
    print("According to the report, what happened to the share of U.S. adults living in middle-income households between 1971 and 2019?\n")
    
    print("A. Increased from 51% to 61%")
    print("B. Remained about the same")
    print("C. Decreased from 61% to 51% ")
    print("D. Decreased from 71% to 41%")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "C":
        print("\nYes, Spot On!")
    else: 
        while answer != "C":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nYes, Spot On!")
        
    print("\nThe report notes that the share of American adults in middle-income households fell from 61% in 1971 to 51% in 2019, reflecting the shrinking of the middle class. Because of this, a larger share of America's overall income is going to upper-income households\n")

    input("\nPress Enter to continue to the next question\n\n")
    
    print("Question 2\n")
    print("What concept related to social mobility is discussed in the report's section on why inequality matters?\n")
    
    print("A. The Great Gatsby Curve")
    print("B. The Digital Divide")
    print("C. The Glass Ceiling Effect")
    print("D. The Trickle-Down Theory")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "A":
        print("\nYes, You Got It!")
    else: 
        while answer != "A":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nYes, You Got It!")
        
    print("\nThe report discusses The Great Gatsby Curve, which suggests that higher levels of inequality may be associated with reduced economic mobility and fewer opportunities to move up the economic ladder.\n")

    input("\nPress Enter to continue to the next question\n")
    
    print("Question 3\n")
    print("What did many Americans identify as a major contributor to economic inequality?\n")
    
    print("A. People spend too much money.")
    print("B. Some people start out with more opportunities than others.")
    print("C. Lack of entertainment options.")
    print("D. Too many college graduates.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "B":
        print("\nYes, That's Right!")
    else: 
        while answer != "B":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nYes, That's Right!")
        
    print("\nAccording to the report, About 40% of Americans said differences in starting opportunities contribute a great deal to economic inequality.\n")

    input("\nPress Enter to continue to the next question\n")
    
    print("Question 4\n")
    print("What percentage of Americans said there is too much economic inequality in the United States?\n")
    
    print("A. 78%")
    print("B. 51%")
    print("C. 42%")
    print("D. 61%")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "D":
        print("\nYes, Well Done!")
    else: 
        while answer != "D":
            print("\nNot quite.")
            answer = input("Try again A, B, C, or D: ").upper()
                            
        print("\nYes, Well Done!")
        
    print("\nThe report found that 61% of Americans believe there is too much economic inequality in the country today.\n")

    print("\nYou have reached the end of quiz!")
    input("Please press Enter to exit...")
        
wealth_gap_questions()


