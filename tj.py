def dsj_topic():
    main_menu()

def main_menu():
    title_subtitle("Trans Technologies", "by Oliver L. Haimson")
    options = {
        "1": "Ask Yourself",
        "2": "Review Your Answers",
        "3": "View Total Number of Attempts",
        "4": "Clear Total Number of Attempts",
        "Q": "Quit"
    }
    selection = True
    while selection == True:
        print("Main Menu:\n")
        for key, value in options.items():
            print(f"    [{key}] {value}")
        user_choice = input("\nSelect an option: ").lower()
        if user_choice == "1":
            for _ in range(len(q)):
                questions()
            main_menu()
        elif user_choice == "2":
            review_answers()
            main_menu()
        elif user_choice == "3":
            review_attempts()
            main_menu()
        elif user_choice == "4":
            total_attempts.clear()
            title_subtitle("Total attempts have been reset", "Returning to main menu...")
            main_menu()
        elif user_choice == "q":
            print("\nExiting...\n")
            break
        else:
            error_message(user_choice)

def title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")
    
def title_subtitle(title, subtitle):
    if len(subtitle) > len(title):
        delta = int((len(subtitle) - len(title)) / 2)
        print("=" * len(subtitle))
        print(" " * delta, title, sep = "")
        print(subtitle)
        print("=" * len(subtitle) + "\n")
    else:
        delta = int((len(title) - len(subtitle)) / 2)
        print("=" * len(title))
        print(title)
        print(" " * delta, subtitle, sep = "")
        print("=" * len(title) + "\n")

def error_message(user_input):
    print(f"\n{user_input} is not a valid selection.\n")

q = [
        {
        "question": "Do you like it?",
        "option": {
            "A": "Yes",
            "B": "No",
            "C": "Maybe"}
        },
        {
        "question": 1,
        "option": {
            "A": "4",
            "B": "5",
            "C": "6"}
        },
        {
        "question": 2,
        "option": {
            "A": "7",
            "B": "8",
            "C": "9"}
        }
    ]
a = [
        {
        "answer": "",
        "answer_key": {
            "A": "Good",
            "B": "Good",
            "C": "Bad"}
        },
        {
        "answer_key": {
            "A": "Good",
            "B": "Good",
            "C": "Bad"}
        },
        {
        "answer": "",
        "answer_key": {
            "A": "Good",
            "B": "Good",
            "C": "Bad"}
        }
    ]
total_attempts = []

def questions():
    title("Ask Yourself")
    index = 0
    attempts = 0
    for item in q:
        valid_selection = False
        while not valid_selection:
            print(f"Question #{index + 1}:")
            if attempts > 0:
                print("Total attempts:", attempts)
            print(f"\n{item['question']}")
            for key, value in item["option"].items():
                print(f"    [{key}] {value}")
            user_choice = input("Select an answer: ")
            if user_choice in ["a", "A", "b", "B", "c", "C"]:
                valid_selection = True
                total_attempts.append(attempts)
                attempts = 0
                #print(total_attempts)
                a[index]["answer"] = user_choice
                print(a)
            else:
                error_message(user_choice)
            attempts += 1
        attempts = 0
        index += 1
     
def review_answers():
    print("\nAnswers I guess\n")
    title("Guided Review")
def review_attempts():
    print("\nAttempts I guess\n")
    title("Total Number of Attempts Per Question")

dsj_topic()