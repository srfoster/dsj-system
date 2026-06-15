def main():

    score = 0
    trust = 50

    print("Hello there! today we will be learning a bit about the book Pedagogy of the Opressed")
    print("This book was written by Paulo Freire and delves into the topics of Diversity and Social Justice")

    name = input("\nWhat is your name? ")

    print(f"\nWelcome, {name}!")
    print("You have just been elected as a community leader.")
    print("Your goal is to listen to residents, encourage")
    print("discussion, and help solve community problems.")

    input("\nPress Enter to begin.")

    scenarios = [

        {
            "title": "Day 1: Community Concerns",
            "description":
            "Residents say their neighborhood has fewer educational resources.",
            "options": [
                "1. Ignore the concern",
                "2. Meet with residents and learn more",
                "3. Assume the problem doesn't exist"
            ],
            "correct": "2",
            "success":
            "You listen to residents and learn more about the issue.",
            "failure":
            "Residents feel their concerns are not being heard."
        },

        {
            "title": "Day 2: Community Meeting",
            "description":
            "People disagree about how to improve local education.",
            "options": [
                "1. Allow respectful discussion",
                "2. Let only one person speak",
                "3. End the meeting"
            ],
            "correct": "1",
            "success":
            "People share ideas and learn from one another.",
            "failure":
            "The conversation shuts down before ideas can be explored."
        },

        {
            "title": "Day 3: Understanding Problems",
            "description":
            "A report shows some students struggle more than others.",
            "options": [
                "1. Investigate the causes",
                "2. Ignore the report",
                "3. Blame individuals only"
            ],
            "correct": "1",
            "success":
            "The community begins looking at the bigger picture.",
            "failure":
            "The root causes remain unexplored."
        },

        {
            "title": "Day 4: Youth Voices",
            "description":
            "Teenagers say their opinions are never included in decisions.",
            "options": [
                "1. Create opportunities for them to participate",
                "2. Ignore them",
                "3. Tell them adults know best"
            ],
            "correct": "1",
            "success":
            "More people become involved in the community.",
            "failure":
            "Young people feel excluded from decisions."
        },

        {
            "title": "Day 5: Solving a Problem",
            "description":
            "The community wants to improve educational access.",
            "options": [
                "1. Talk with community members",
                "2. Make decisions alone",
                "3. Assume everyone has the same experience"
            ],
            "correct": "1",
            "success":
            "Residents help create solutions together.",
            "failure":
            "Important perspectives are left out."
        }

    ]

    for scenario in scenarios:

        print("\n" + scenario["title"])
        print("\n" + scenario["description"])

        for option in scenario["options"]:
            print(option)

        choice = input("\nChoice: ")

        if choice == scenario["correct"]:
            print("\n" + scenario["success"])
            score += 1
            trust += 10
        else:
            print("\n" + scenario["failure"])
            trust -= 10

        print("Community Trust:", trust)

        input("\nPress Enter to continue.")

    print("\nFinal Quiz")

    quiz = [

        {
            "question":
            "True or False: Dialogue is important in Freire's ideas.",
            "answer": "true"
        },

        {
            "question":
            "True or False: People should think critically about social issues.",
            "answer": "true"
        },

        {
            "question":
            "True or False: Students should only memorize information.",
            "answer": "false"
        }

    ]

    for question in quiz:

        answer = input("\n" + question["question"] + " ")

        if answer.lower() == question["answer"]:
            score += 1

    print("\nFinal Results")

    print("\nScore:", score, "/ 8")
    print("Community Trust:", trust)

    if trust >= 80:
        print("\nExcellent Ending")
        print("Residents feel heard and actively participate.")
        print("The community works together to address problems.")

    elif trust >= 50:
        print("\nGood Ending")
        print("The community has made progress,")
        print("but there is still room for improvement.")

    else:
        print("\nNeeds Improvement")
        print("Many residents feel left out of decisions.")
        print("More dialogue and participation are needed.")

    print("\nKey Ideas from Pedagogy of the Oppressed:")
    print("- Dialogue is important to everyone in the community.")
    print("- People should ask questions about things they might not understand.")
    print("- Critical thinking helps communities grow.")
    print("- Learning helps improve every aspect of society.")

    print(f"\nThanks for playing, {name}!")

main()
