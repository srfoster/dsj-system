# "Educational Experience" based on the book Evicted by Matthew Desmond.

def dsj_topic():

    print("Based on the book, Evicted: Poverty and Profit in the American City\n")

    # Introduction
    print("--- Welcome! ---")
    print("Evicted follows families struggling to afford housing.")
    print("The book explores how poverty and eviction affect people's lives.\n")
    print("''it is hard to argue that housing is not a fundamental human need. Decent, affordable housing should be a")
    print("basic right for everybody in this country. The reason is simple: without stable shelter, everything else falls apart.''")
    print("― Matthew Desmond, Evicted.\n")

    answer = input("What is eviction?\nA. Leaving school\nB. Losing your home\nC. Buying food\n\nAnswer: ")

    if answer.upper() == "B":
        print("Correct!\n")
    else:
        print("The correct answer is B.\n")

    answer = input("How can eviction affect children?\nA. More stress\nB. Better sleep\nC. More money\n\nAnswer: ")

    if answer.upper() == "A":
        print("Correct!\n")
    else:
        print("The correct answer is A. More stress.")

    choice = input(
    "\nYou only have enough money for one:\n"
    "A. Rent\n"
    "B. Groceries\n"
    "C. Gas\n"
    "D. Medicine\n"
    "\nWhich would you choose?: "
    )

    print("\n-- Families facing poverty often have to make difficult choices like these. --\n")
    
    answer = input("Which is a federal policy initiative widely used to attempt and reduce poverty among low-income working families in the U.S.?\nA. Implementing a universal flat tax rate on all household income\nB. Expanding the Earned Income Tax Credit (EITC) and Child Tax Credit (CTC)\nC. Eliminating state-level minimum wage requirements\nD. Shifting all community aid responsibility exclusively to private charities \n\nAnswer: ")

    if answer.upper() == "B":
        print("Correct!\n")
    else:
        print("The correct answer is B. Expanding the Earned Income Tax Credit (EITC) and Child Tax Credit (CTC).\n")

    choice = input("Let's reflect, why do you believe housing is important?: ")

    print("\nYour answer:")
    print(choice)

    print("\nThanks for learning about Evicted! ;D")

#dsj_topic() # Remember to comment out the function call!
