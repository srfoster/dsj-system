q = [
        {"index": 0,
        "question": 0,
        "option": {
            "A": 1,
            "B": 2,
            "C": 3}
        },
        {"index": 1, "question": 1, "option": {"A": "", "B": "", "C": ""}},
        {"index": 2, "question": 2, "option": {"A": "", "B": "", "C": ""}}
]

def dsj_topic():
    main_menu()

def main_menu():
    menu_header("Trans Technologies", "by Oliver L. Haimson")
    options = {
        "1": "Questions and Answers",
        "Q": "Quit"
    }
    selection = True
    while selection == True:
        for key, value in options.items():
            print(f"[{key}] {value}")
        choice = input("Select an option: ").lower()
        if choice == "1":
            print("Questions and Answers selected.")
            questions()
        elif choice == "q":
            print("Exiting...")
            break

def menu_header(title, subtitle):
    if subtitle:
        if len(subtitle) > len(title):
            print("=" * len(subtitle))
            print(" " * int(((len(subtitle) - len(title))) / 2), title, sep = "")
            print(subtitle)
            print("=" * len(subtitle))
        else:
            print("=" * len(title))
            print(title)
            print(" " * int(((len(title) - len(subtitle))) / 2), subtitle, sep = "")
            print("=" * len(title))

def questions():
    for index in range(len(q)):
        current = (q[index]["question"])
        print(current)
        
#def answers(choice):

dsj_topic()