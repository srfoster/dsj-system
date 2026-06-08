#def dsj_topic():
    #print("Opaque Hiring")
    #wmd()

applicant = {"race" : None}

def main_menu():
    menu_header("Character Editor")
    options = {
        "1": "Race",
        "2": "Personality Test",
        "3": "Residence",
        "4": "Previous job",
    }
    loop = True
    while loop: # Loop to ensure valid menu selection.          #modified this into a character editor
        for key, value in options.items():
            print(f"[{key}] {value}")
        selection = input("Select an option: ")
        if selection == "1":
            race_selection()
            points, character["Race"] = location_score()
            point_scores["Race"] = points
            loop = False
        elif selection == "2":
            personality_test()
            points, character["Personality"] = location_score()
            point_scores["Personality"] = points
            loop = False
        elif selection == "3":
            points, character["Residence"] = location_score()
            point_scores["Residence"] = points
            loop = False
        elif selection == "4":
            points, character["Previous job"] = work_history_score()
            point_scores["Previous job"] = points
            loop = False
        else:
            print("Invalid selection. Please choose a valid option.")

def race_selection():
    menu_header("Applicant Race Selection")
    races = {
        "1": "Elf",
        "2": "Dwarf",
        "3": "Halfling",
        "4": "Orc"
    }
    for key, value in races.items():
        print(f"[{key}] {value}")
    selection = True
    while selection: # Loop to ensure valid class selection.
        race = input("Select your race: ")
        if race in races:
            applicant["race"] = races[race]
            print(races[race] + " selected.")
            selection = False
        else:
            print("Invalid race selection. Please choose a valid option.")

def personality_test():
    menu_header("Personality Test")
    traits = {
        # Looked up traits interviewers look for.https://status.net/articles/professional-characteristics-for-the-workplace-essential-traits-for-success/
        "Integrity": 0,
        "Commitment": 0,
        "Communication": 0,
        "Reliability": 0,
        "Teamwork": 0,
        "Problem-Solving": 0,
        "Time Management": 0,
        "Adaptability": 0,
        "Emotional Intelligence": 0
    }
    questions = [
        {
            # Looked up interview questions. https://www.bing.com/search?q=Interview%20questions%20for%20job%20interview%20that%20grade%20the%20following%20traits%3A%20Integrity%2C%20Commitment%2C%20Communication%2C%20Reliability%2C%20Teamwork%2C%20Problem-Solving%2C%20Time%20Management%2C%20Adaptability%2C%20and%20Emotional%20Intelligence.%20Multiple%20choice&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=interview%20questions%20for%20job%20interview%20that%20grade%20the%20following%20traits%3A%20integrity%2C%20commitment%2C%20communication%2C%20reliability%2C%20teamwork%2C%20problem-solving%2C%20time%20management%2C%20adaptability%2C%20and%20emotional%20intelligence.%20multiple%20choice&sc=7-223&sk=&cvid=1EF9F21A57EA42AA85AECAF4BF07992C
            "question": "You discover a colleague has made a mistake that could cost the company money. What do you do?",
            "options": {
                "A": "Ignore it — it is not your responsibility.",
                "B": "Quietly fix it without telling anyone.",
                "C": "Inform your manager and suggest a solution.",
                "D": "Tell other colleagues about it to warn them."
            },
            "values": {
                "A": {"Integrity": -2, "Problem-Solving": -1},
                "B": {"Integrity": 1, "Problem-Solving": 2},
                "C": {"Integrity": 2, "Problem-Solving": 1},
                "D": {"Integrity": -1, "Problem-Solving": -2}
            }
        }
    ]
    # TODO: Change scores in traits based on answers to questions.

def menu_header(title):
    #print("=" * len(title))
    print(title)
    print("=" * len(title))
#------------------------------------------------------------------------------------------------------------------------------------
# my part of the hiring model
def location_score():
    score = 0
    print("=-= Where do you live? =-=\n")

    print("1. Gilded Arch\n2. Ash-Bury\n3. Cresthaven\n4. Shingletown\n")

    town = input("Choose (1, 2, 3, or 4): ")

    if town == "1":
        score += 20
    elif town == "2":
        score += 5
    elif town == "3":
        score += 10
    elif town == "4":
        score -= 5

    print("Thank you for that information!")
    return score
# work history
def work_history_score():
    score = 0
    print("\n=-= Work History =-=\n")

    print("1. Healer\n2. Torchbearer\n3. Cartographer\n4. Blacksmith")

    job = input("Choose your previous job (1, 2, 3, or 4): ")

    if job == "1":
        score += 20
    elif job == "2":
        score -= 5
    elif job == "3":
        score += 15
    elif job == "4":
        score += 5

    print("Work history analyzed, Thank you.")
#------------------------------------------------------------------------------------------------------------------
character = {}
point_scores = {}


def title():
    print("=" * 50)
    print(f"      //Fantasy WMD Simulator//"'\nBased on "Weapons of Math Destruction" CH 6')
    for c,d in character.items():
        print(f"{c}: {d}")
    print("=" * 50)


def wmd():
    jobtime = True
    cheater = False
    points = 0
    point_total = 0
    print("=" * 50)
    character["Name"] = name = input("      //Fantasy WMD Simulator//"'\nBased on "Weapons of Math Destruction" CH 6'"\nJob application for Mana inc.""\nEnter you're name: ")
    print("=" * 50)
    while jobtime:
        #points, character["Race"] = race_selection()
        #point_scores["Race"] = points
        #title()
        #points, character["Personality result"] = personality_test()
        #point_scores["Personality result"] = points
        #title()
        points, character["Residence"] = location_score()
        point_scores["Residence"] = points
        title()
        points, character["Previous job"] = work_history_score()
        point_scores["Previous job"] = points
        finish = True
        title()
        while finish:
            point_total = sum(point_scores.values())
            if point_total < 0 :
                print("You're not Hired")
                print("=" * 50)
            else:
                print("Congradulations you're Hired!")
                print("=" * 50)
            if cheater:
                print("Press i to edit your character""\nPress s to view your scores")
            else:
                print("Press c for cheats")
            option = input("Press r to restart""\nPress q to quit\n").lower()
            print("=" * 50)
            if option == "r":
                wmd()
                return
            if option == "c":
                cheater = True
                #title()
                #print("Press i to edit your character""\nPress s to view your scores")
                #print("=" * 50)
            if option == "i":
                title()
                main_menu()
                title()
            if option == "s":
                title()
                print(f"Your hiring score is: {point_total}")
                for c,d in character.items():
                    if c =="Name":
                        continue
                    score= point_scores[c]
                    print(f"{c}: {d} ,score: {score}")
                print("=" * 50)
            if option == "q":
                print("Quitting...")
                finish = False
                jobtime = False


wmd()
