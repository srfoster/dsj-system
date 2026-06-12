def dsj_topic():
    menu_header("Opaque Hiring")
    wmd()
    

def personality_test():
    menu_header("Personality Test")
    traits = {
        # Looked up traits interviewers look for.https://status.net/articles/professional-characteristics-for-the-workplace-essential-traits-for-success/
        "Integrity": 0,
        "Commitment": 0,
        "Communication": 0,
        "Reliability": 0,
        "Teamwork": 0,
        "Problem Solving": 0,
        "Time Management": 0,
        "Adaptability": 0,
        "Emotional Intelligence": 0
    }
    # Looked up interview questions. https://www.bing.com/search?q=Interview%20questions%20for%20job%20interview%20that%20grade%20the%20following%20traits%3A%20Integrity%2C%20Commitment%2C%20Communication%2C%20Reliability%2C%20Teamwork%2C%20Problem Solving%2C%20Time%20Management%2C%20Adaptability%2C%20and%20Emotional%20Intelligence.%20Multiple%20choice&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=interview%20questions%20for%20job%20interview%20that%20grade%20the%20following%20traits%3A%20integrity%2C%20commitment%2C%20communication%2C%20reliability%2C%20teamwork%2C%20Problem Solving%2C%20time%20management%2C%20adaptability%2C%20and%20emotional%20intelligence.%20multiple%20choice&sc=7-223&sk=&cvid=1EF9F21A57EA42AA85AECAF4BF07992C
    questions = [
        {
            "user answer": None,
            "question": "You discover a colleague has made a mistake that could cost the company money. They ask you not to tell anyone. What do you do?",
            "options": {
                "A": "Keep it quiet to protect your colleague.",
                "B": "Report it immediately without speaking to them.",
                "C": "Discuss it with them first, then work together to inform the right person.",
                "D": "Ignore it and hope it doesn’t cause problems."
            },
            "values": {
                "A": {"Integrity": -2, "Communication": -1, "Teamwork": 1},
                "B": {"Integrity": 2, "Teamwork": -2, "Emotional Intelligence": -1},
                "C": {"Integrity": 2, "Communication": 2, "Teamwork": 2, "Emotional Intelligence": 1},
                "D": {"Integrity": -2, "Reliability": -2, "Problem Solving": -1}
            }
        },
        {
            "user answer": None,
            "question": "A project deadline is unexpectedly moved up by a week. How do you respond?",
            "options": {
                "A": "Complain about the change but still try to finish.",
                "B": "Adjust your schedule and put in extra effort to meet the new deadline.",
                "C": "Ask for the deadline to be moved back.",
                "D": "Do what you can but accept it might be late."
            },
            "values": {
                "A": {"Commitment": 1, "Adaptability": -1, "Emotional Intelligence": -1},
                "B": {"Commitment": 2, "Adaptability": 2, "Reliability": 2},
                "C": {"Commitment": -1, "Communication": 1, "Adaptability": -1},
                "D": {"Commitment": -1, "Reliability": -2, "Integrity": -1}
            }
        },
        {
            "user answer": None,
            "question": "Your manager gives you unclear instructions. What’s your next step?",
            "options": {
                "A": "Guess what they meant and proceed.",
                "B": "Ask clarifying questions to ensure you understand.",
                "C": "Wait until they notice and clarify themselves.",
                "D": "Ask a coworker to interpret for you."
            },
            "values": {
                "A": {"Communication": -2, "Problem Solving": -1, "Reliability": -1},
                "B": {"Communication": 2, "Problem Solving": 2, "Time Management": 1},
                "C": {"Communication": -2, "Reliability": -2, "Time Management": -2},
                "D": {"Communication": -1, "Teamwork": 1}
            }
        },
        {
            "user answer": None,
            "question": "A teammate is relying on you to deliver part of a project. You realize you might be late. What do you do?",
            "options": {
                "A": "Say nothing and hope you can catch up.",
                "B": "Let them know immediately and offer solutions.",
                "C": "Wait until the deadline to explain.",
                "D": "Ask someone else to cover for you without telling them why."
            },
            "values": {
                "A": {"Reliability": -2, "Integrity": -2, "Communication": -2},
                "B": {"Reliability": 2, "Communication": 2, "Integrity": 2, "Problem Solving": 1},
                "C": {"Reliability": -2, "Communication": -1, "Emotional Intelligence": -2},
                "D": {"Reliability": -1, "Teamwork": -2, "Integrity": -1}
            }
        },
        {
            "user answer": None,
            "question": "During a group project, one member is not contributing equally. How do you handle it?",
            "options": {
                "A": "Take over their tasks without saying anything.",
                "B": "Speak to them privately to understand and offer help.",
                "C": "Complain to the manager right away.",
                "D": "Ignore it and focus on your own work."
            },
            "values": {
                "A": {"Teamwork": -1, "Communication": -2, "Commitment": 1},
                "B": {"Teamwork": 2, "Emotional Intelligence": 2, "Communication": 2},
                "C": {"Teamwork": -2, "Emotional Intelligence": -1, "Integrity": 1},
                "D": {"Teamwork": -2, "Commitment": -1, "Reliability": 1}
            }
        },
        {
            "user answer": None,
            "question": "A client rejects your proposed solution. What’s your approach?",
            "options": {
                "A": "Defend your idea strongly.",
                "B": "Ask for feedback, then brainstorm alternatives.",
                "C": "Drop the project entirely.",
                "D": "Wait for them to change their mind."
            },
            "values": {
                "A": {"Problem Solving": 0, "Adaptability": -2, "Emotional Intelligence": -1},
                "B": {"Problem Solving": 2, "Adaptability": 2, "Communication": 2},
                "C": {"Problem Solving": -2, "Commitment": -2, "Adaptability": -2},
                "D": {"Problem Solving": -2, "Adaptability": -2, "Time Management": -2}
            }
        },
        {
            "user answer": None,
            "question": "You have multiple urgent tasks due today. What’s your first step?",
            "options": {
                "A": "Start with the easiest task.",
                "B": "Prioritize tasks based on importance and deadlines.",
                "C": "Work on all tasks at once.",
                "D": "Ask for deadline extensions on all tasks."
            },
            "values": {
                "A": {"Time Management": 1, "Problem Solving": 0},
                "B": {"Time Management": 2, "Problem Solving": 2, "Reliability": 1},
                "C": {"Time Management": -2, "Adaptability": -1, "Problem Solving": -1},
                "D": {"Time Management": -1, "Reliability": -2, "Commitment": -1}
            }
        },
        {
            "user answer": None,
            "question": "Your company suddenly changes its main software tool. How do you react?",
            "options": {
                "A": "Resist the change and keep using the old tool.",
                "B": "Learn the new tool quickly and help others adjust.",
                "C": "Wait until you’re forced to switch.",
                "D": "Complain about the change to coworkers."
            },
            "values": {
                "A": {"Adaptability": -2, "Problem Solving": -1, "Commitment": -1},
                "B": {"Adaptability": 2, "Teamwork": 2, "Commitment": 2},
                "C": {"Adaptability": -1, "Reliability": -1},
                "D": {"Adaptability": -2, "Emotional Intelligence": -2, "Teamwork": -1}
            }
        },
        {
            "user answer": None,
            "question": "A coworker is visibly upset during a meeting. What do you do?",
            "options": {
                "A": "Ignore it to avoid awkwardness.",
                "B": "Check in with them privately afterward.",
                "C": "Ask them in front of everyone what’s wrong.",
                "D": "Tell them to focus on work."
            },
            "values": {
                "A": {"Emotional Intelligence": -1, "Teamwork": -1},
                "B": {"Emotional Intelligence": 2, "Teamwork": 2, "Communication": 1},
                "C": {"Emotional Intelligence": -2, "Communication": -1},
                "D": {"Emotional Intelligence": -2, "Teamwork": -2, "Communication": -1}
            }
        }
    ]
    count = 0
    for question in questions:
        while True:
            print(f"Question #{count + 1}:")
            print(f"\n{question['question']}")  #changed "" into '' to avoid python bug/feature
            for key, value in question["options"].items():
                print(f"\n\t[{key}] {value}")
            user_choice = input("\nSelect an answer: ").upper()
            if user_choice in question["options"]:
                question["user_answer"] = user_choice
                #Looked up how to index into a nested dictionary. #Looked up how to index into a nested dictionary. https://www.bing.com/search?pglt=299&q=how+to+index+into+a+nested+dictionary+python&cvid=cc77d250e0564b5fa85f46bf6802b515&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgcICBDrBxhA0gEJMTUyNzZqMGo3qAIAsAIA&FORM=ANNTA1&PC=HCTS
                for key, value in question["values"][user_choice].items():
                    traits[key] = traits.get(key, 0) + value
                break
            else:
                print(f"{user_choice} is not a valid selection.")
        count += 1

    return traits


def personality_results():
    traits = personality_test()
    trait_weight = {
        "Commitment": 2.5,
        "Reliability": 2.5,
        "Adaptability": 2.0,
        "Time Management": 1.5,
        "Problem Solving": 1.5,
        "Communication": 1.0,
        "Teamwork": 1.0,
        "Integrity": 0.5,
        "Emotional Intelligence": 0.2
    }
    score = 0.0
    for i in traits:
        points = traits[i]
        weight = trait_weight[i]
        if points < 0:
            score += (points * weight * 2.0)
        else:
            score +=(points * weight)
    score = round(score)
    if score >= 40:
        hire = "High value"
    elif score >= 10:
        hire = "Mid value"
    else:
        hire = "Low value"
    return score, hire


def menu_header(title):
    print("=" * len(title))
    print(title)
    print("=" * len(title))
#------------------------------------------------------------------------------------------------------------------------------------
#used AI to help balance the wmd scores for personality results and race,work,class,residence (numbers only, no code) (Google Gemini)
#------------------------------------------------------------------------------------------------------------------------------------
def race_selection():
    score = 0

    races = {
        "1": ("Elf", 20),
        "2": ("Mark Zuckerberg (Lizardmen)", -20),
        "3": ("Dwarf", -10),
        "4": ("Orc", -30),
        "5": ("Human", 10),
        "6": ("Goblin", -40)
    }
    while True:
        print("=-= Whats your race? =-=")
        print("=" * 50)
        print("1. Elf\n2. Mark Zuckerberg (a.k.a Lizardmen)\n3. Dwarf\n4. Orc\n5. Human\n6. Goblin")

        r = input("Choose (1, 2, 3, 4, 5, 6): ")

        if r in races:
            race_names, score = races[r]
            break
        else:
            print("Please choose a valid option.")

    return score, race_names


def class_score():
    score = 0

    classes = {
        "1": ("Cleric", -40),
        "2": ("Rogue", 20),
        "3": ("Warrior", -30),
        "4": ("Mage", -10),
        "5": ("Tank", 10),
        "6": ("Ranger", -20)
    }
    while True:
        print("=-= Whats your class? =-=")
        print("=" * 50)
        print("1. Cleric\n2. Rogue\n3. Warrior\n4. Mage\n5. Tank\n6. Ranger")

        c = input("Choose (1, 2, 3, 4, 5, 6): ")

        if c in classes:
            class_names, score = classes[c]
            break
        else:
            print("Please choose a valid option.")

    return score, class_names


def location_score():
    score = 0

    towns = {
        "1": ("Gilded Arch", 20),
        "2": ("Shingletown", -20),
        "3": ("Cresthaven", -10),
        "4": ("Jacobstown", -30),
        "5": ("Whiterun", 10),
        "6": ("Kvatch", -40)
    }
    while True:
        print("=-= Where do you live? =-=")
        print("=" * 50)
        print("1. Gilded Arch\n2. Shingletown\n3. Cresthaven\n4. Jacobstown\n5. whiterun\n6. Kvatch")

        town = input("Choose (1, 2, 3, 4, 5, 6): ")

        if town in towns:
            town_names, score = towns[town]
            break
        else:
            print("Please choose a valid option.")

    return score, town_names


def work_history_score():
    jobs = {
        "1": ("Mercenary", 20),
        "2": ("Alchemist", -10),
        "3": ("Cartographer", -20),
        "4": ("Begger", -40),
        "5": ("Potion Salesman", 10),
        "6": ("Blacksmith", -30)
    }
    while True:
        print("=-= Work History =-=")
        print("=" * 50)
        print("1. Mercenary\n2. Alchemist\n3. Cartographer\n4. Begger\n5. Potion Salesman\n6. Blacksmith")
        
        job = input("Choose your previous job (1, 2, 3, 4, 5, 6): ")

        if job in jobs:
            job_names, score = jobs[job]
            break
        else:
            print("Please choose a valid option.")
    
    return score, job_names
#------------------------------------------------------------------------------------------------------------------
def editor():
    menu_header("Character Editor")
    options = {
        "1": "Race",
        "2": "Class",
        "3": "Residence",
        "4": "Previous job",
        "5": "Personality Test",
    }
    functions = {
        "1": race_selection,
        "2": class_score,
        "3": location_score,
        "4": work_history_score,
        "5": personality_results
    }
    loop = True
    while loop:
        for key, value in options.items():
            print(f"[{key}] {value}")
        selection = input("Select an option: ")
        if selection == "1":
            points, character["Race"] = race_selection()
            point_scores["Race"] = points
            loop = False
        elif selection == "2":
            points, character["Class"] = class_score()
            point_scores["Class"] = points
            loop = False
        elif selection == "3":
            points, character["Residence"] = location_score()
            point_scores["Residence"] = points
            loop = False
        elif selection == "4":
            points, character["Previous job"] = work_history_score()
            point_scores["Previous job"] = points
            loop = False
        elif selection == "5":
            points, character["Personality"] = personality_results()
            point_scores["Personality"] = points
            loop = False
        else:
            print("Invalid selection. Please choose a valid option.")
#------------------------------------------------------------------------------------------------------------------
character = {}
point_scores = {}


def title():
    print("=" * 50)
    print(f"      //Fantasy WMD Hiring Simulator//"'\nBased on "Weapons of Math Destruction" CH 6')
    print("=" * 50)
    for c,d in character.items():
        print(f"{c}: {d}")
    print("=" * 50)


def wmd():
    character.clear()
    point_scores.clear()
    jobtime = True
    cheater = False
    points = 0
    point_total = 0
    print("=" * 50)
    character["Name"] = name = input("      //Fantasy WMD Hiring Simulator//"'\nBased on "Weapons of Math Destruction" CH 6'"\nJob application for Mana inc.""\nEnter your name: ")
    print("=" * 50)
    while jobtime:
        point_scores["Name"] = 0
        orc_names = ["ok","og","gg","kk","ur","or"]
        for letters in orc_names:
            if letters in name.lower():
                point_scores["Name"] = -20
        points, character["Race"] = race_selection()
        point_scores["Race"] = points
        title()
        points, character["Class"] = class_score()
        point_scores["Class"] = points
        title()
        points, character["Residence"] = location_score()
        point_scores["Residence"] = points
        title()
        points, character["Previous job"] = work_history_score()
        point_scores["Previous job"] = points
        title()
        points, character["Personality"] = personality_results()
        point_scores["Personality"] = points
        finish = True
        title()
        while finish:
            point_total = sum(point_scores.values())
            if point_total < 0 :
                print("You're not Hired")
                print("=" * 50)
            else:
                print("Congratulations, you're Hired!")
                print("=" * 50)
            if cheater:
                print("Press i to edit your character""\nPress s to view your hidden scores")
            else:
                print("Press c for cheats")
            option = input("Press r to restart""\nPress q to quit\n").lower()
            print("=" * 50)
            if option == "r":
                wmd()
                return
            if option == "c":
                title()
                cheater = True
            if option == "i":
                title()
                editor()
                title()
            if option == "s":
                print(f"      //Fantasy WMD Hiring Simulator//"'\nBased on "Weapons of Math Destruction" CH 6')
                print("=" * 50)
                print(f"Your hiring score is: {point_total}")
                for c,d in character.items():
                    score= point_scores[c]
                    print(f"{c}: {d} ,score: {score}")
                print("=" * 50)
            if option == "q":
                print("Quitting...")
                finish = False
                jobtime = False