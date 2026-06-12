print("=====================================================")
print("              Wealth Gap Knowledge Quiz") 
print("Based on Pew Research Findings on Economic Inequality")
print("=====================================================\n")

def dsj_topic():
    score = 0
    print("Question 1\n")
    print("🤔   According to the report, what happened to the share of U.S. adults living in middle-income households between 1971 and 2019?\n")
    
    print("A. Increased from 51% to 61%")
    print("B. Remained about the same")
    print("C. Decreased from 61% to 51% ")
    print("D. Decreased from 71% to 41%")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "C":
        print("\n✅   Yes, Spot On! 😊\n")
        score += 1
    else: 
        while answer != "C":
            print("\n❌   Not quite.")
            answer = input(">>>    Try again A, B, C, or D: ").upper()
                            
        print("\n✅   Yes, Spot On! 😊")
        score += 1
        
    print("\n💡   The report notes that the share of American adults in middle-income households fell from 61% in 1971 to 51% in 2019, reflecting the shrinking of the middle class. Because of this, a larger share of America's overall income is going to upper-income households\n\n")

    input("Press Enter to continue to the next question\n\n")
    
    print("Question 2\n")
    print("🤔   What concept related to social mobility is discussed in the report's section on why inequality matters?\n")
    
    print("A. The Great Gatsby Curve")
    print("B. The Digital Divide")
    print("C. The Glass Ceiling Effect")
    print("D. The Trickle-Down Theory")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "A":
        print("\n✅   Yes, You Got It! 😊")
        score += 1
    else: 
        while answer != "A":
            print("\n❌   Not quite.")
            answer = input(">>>    Try again A, B, C, or D: ").upper()
                            
        print("\n✅   Yes, You Got It! 😊")
        score += 1
        
    print("\n💡   The report discusses The Great Gatsby Curve, which suggests that higher levels of inequality may be associated with reduced economic mobility and fewer opportunities to move up the economic ladder.\n")

    input("\nPress Enter to continue to the next question\n")
    
    print("Question 3\n")
    print("🤔   What did many Americans identify as a major contributor to economic inequality?\n")
    
    print("A. People spend too much money.")
    print("B. Some people start out with more opportunities than others.")
    print("C. Lack of entertainment options.")
    print("D. Too many college graduates.")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "B":
        print("\n✅   Yes, That's Right! 😊")
        score += 1
    else: 
        while answer != "B":
            print("\n❌   Not quite.")
            answer = input(">>>    Try again A, B, C, or D: ").upper()
                            
        print("\n✅   Yes, That's Right! 😊")
        score += 1
        
    print("\n💡   According to the report, About 40% of Americans said differences in starting opportunities contribute a great deal to economic inequality.\n")

    input("\nPress Enter to continue to the next question\n")
    
    print("Question 4\n")
    print("🤔   What percentage of Americans said there is too much economic inequality in the United States?\n")
    
    print("A. 78%")
    print("B. 51%")
    print("C. 42%")
    print("D. 61%")
    
    answer = ""
    
    while answer not in ["A", "B", "C", "D"]:
        answer = input("\nEnter A, B, C, or D: ").upper()
        
    if answer == "D":
        print("\n✅   Yes, Well Done! 😊")
        score += 1
    else: 
        while answer != "D":
            print("\n❌   Not quite.")
            answer = input(">>>    Try again A, B, C, or D: ").upper()
                            
        print("\n✅   Yes, Well Done! 😊")
        score += 1
        
    print("\n💡   The report found that 61% of Americans believe there is too much economic inequality in the country today.\n\n")

    
    if score == 4:
        print(f">>>  Final Tally: {score}/4  <<<")
        print("💯   Perfect Score!   💯")
    print("\n🏁   You have reached the end of quiz!")
    input("↳↳↳  Please press Enter to exit...")
    
        
dsj_topic()

