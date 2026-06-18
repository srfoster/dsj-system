import random  
include_rules = [] #include lists requirements that you must accept
exclude_rules = [] #exclude lists attributes you must deny

def dsj_topic():
    score = 10
    week = 1
    add_rule()
    print("You are a new WMD algorithm")
    print("You are here to ACCEPT and DENY applicants for hiring by the company.")
    input("When you are ready to get to work, press any key to continue...")
    print("=" * 50)
    game_state = ""
    while game_state not in ["win", "lose"]:
        game_state, score, week = game(score, week)
    if game_state == "win":
        print(f"You win wiht final score of {score} on week {week}!")
    elif game_state == "lose":
        print(f"GAME OVER. You ran out of points at week {week}.")

def game(score, week):
    count = 1
    while count <= 5:
        print("Hiring Criteria:")
        for rule in include_rules:
            for description in rule.keys():
                print(f"{description}")
        for rule in exclude_rules:
            for description in rule.keys():
                print(f"{description}")
        print(f"\nWeek {week}, Applicant #{count}: ")
        applicant = char()
        print("=" * 50)
        for key, value in applicant.items():
            print(f"{key}: {value}")
        print("=" * 50)
        print("(Choose one) APPROVE(Press '1') or DENY(Press '2') applicant?")
        decision = input("Applicant status: ")
        if decision != "1" and decision != "2":
            print("You can only APPROVE(Press '1') or DENY(Press '2').")
            print("=" * 50)
            continue
        result, score = choice(applicant, decision, score)
        if result == "win" or result == "lose":
            return result, score, week
        else:
            print(f"Your decision is {result}.")
            count += 1
            print(f"Your wmd hiring score is: {score}")
            print("=" * 50)
    add_rule()
    print("=" * 50)
    print(f"End of week {week}")
    if len(exclude_rules) <= 4 or len(include_rules) <= 4:
        print("Rule Added")
        print("=" * 50)
    week += 1
    return "", score, week


def char():

    character = {
        "Race": random.choice(["Elf", "Orc", "Dwarf", "Mark Zuckerberg (Lizardmen)", "Goblin", "Human", "Slime", "Hobgoblin", "Troll", "Ogre", "High Elf", "Dark Elf", "Halfling"]),
        "Residence": random.choice(["Whiterun", "Kvatch", "Jacobstown", "Jacinto", "Lordran", "Yharnam", "Raccoon City", "Wraeclast"]),
        "Personality": random.choices(["Low Value", "Mid Value", "High Value"], [5,4,1])[0], #these numbers are weights
        "Gold": random.randint(-200000,200000),
        "Traits": random.sample(["Dim Witted", "Quick Learner", "Undead", "Cannibal", "Lucky", "Anger Issues", "Pyromaniac", "Deaf", "Blind", "Stupid", "Suspicious", "Mysterious", "Good Natured", "Scoundrel"], random.randint(1,3)),
        "Ailments": random.choices(["Cursed", "Vampirism", "Lycanthropy", "None", "Hollowed"], [1,1,1,4,1])[0],
        "Class": random.choice(["Necromancer", "Thief", "Cleric", "Warrior", "Tank", "Druid", "Ranger", "Mage", "Assassin", "Paladin", "Healer"]),
    }
    #print(character)
    return character #this is a dictionary with all the random character attributes


#when called upon this creates rules and adds them to include/exclude rules. The first time its called it creates 1 include rule and 1 exclude rule. It has rule caps, so you can call this at the start of each week.
def add_rule():
    include = [
        {"High value personalities must be chosen": ["High Value"]},
        {"Accept applicants with more than 150,000 gold":[150000]},
        {"Accept all thiefs Assassins and Scoundrels": ["Thief", "Assassin","Scoundrel"]},
        {"Accept all Lucky or Mysterious applicants": ["Lucky", "Mysterious"]},
        {"Accept the residents of whiterun": ["Whiterun"]},
        {"Accept elves and high elves (no dark elves though)": ["Elf", "High Elf"]}
    ]

    exclude = [
        {"No Faith, deny any clerics or paladins": ["Cleric", "Paladin"]},
        {"No goblins of any kind": ["Hobgoblin", "Goblin"]},
        {"No undead, exclude hollows, vampirism, undead, and people from raccoon city or lordran": ["Undead", "Vampirism", "Hollowed", "Lordran", "Raccoon City"]},
        {"No short Races (Hobgoblins excluded)": ["Goblin", "Dwarf", "Halfling"]},
        {"Exclude gold debt above 100,000": [-100000]},
        {"Exclude the deaf, blind, and stupid" : ["Deaf", "Blind", "Stupid"]},
        {"No trolls, orcs, or ogres": ["Ogre", "Orc", "Troll"]},
        {"deny people connected to the dark arts, necrromancers, the cursed, and dark elves": ["Dark Elf", "Necromancer", "Cursed"]}   
    ]
    exrule = None
    inrule = None
    if not include_rules and not exclude_rules:
        include_rules.append(random.choice(include))
        exclude_rules.append(random.choice(exclude))
    elif len(include_rules) == len(exclude_rules):
        if len(exclude_rules) < 4:
            exrule = (random.choice(exclude))
    elif len(exclude_rules) < 4 and len(include_rules) < 4:
        rule_choice = random.choice([include, exclude])
        if rule_choice == include:
            inrule = (random.choice(include))
        if rule_choice == exclude:
            exrule = (random.choice(exclude))
    elif len(exclude_rules) < 4:
        exrule = (random.choice(exclude))
    elif len(include_rules) < 4:
        inrule = (random.choice(include))
    if exrule:
        while exrule in exclude_rules:
            exrule = random.choice(exclude)
        exclude_rules.append(exrule)
    if inrule:
        while inrule in include_rules:
            inrule = random.choice(include)
        include_rules.append(inrule)
    else:
        return
#Looked up what random imports


# Cody, my part! The choice system ;D

# check_rules()
# char = applicant dictionary
# Uses global include_rules and exclude_rules
# Include rules override exclude rules

def check_rules(char):

    # Check include rules first (highest priority)
    for rule in include_rules:

        for topic, rules in rule.items():

            if topic not in char:
                continue
            value = char[topic]

            # Handle list values (Traits)
            if isinstance(value, list):
                for item in value:
                    if item in rules:
                        return True

            # Handle normal values
            elif value in rules:
                return True

    # Check exclude rules
    for rule in exclude_rules:

        for topic, rules in rule.items():

            if topic not in char:
                continue 
            value = char[topic]

            # Handle list values (Traits)
            if isinstance(value, list):
                for item in value:
                    if item in rules:
                        return False

            # Handle normal values
            elif value in rules:
                return False

    # No rule matched
    return True

# update_score()
# approved = True or False from check_rules()
# yesno = player's choice ("1" = approve, "2" = deny)
# score_total = current score
# Returns result and updated score

def update_score(approved, yesno, score_total):

    if (approved and yesno == "1") or \
        (not approved and yesno == "2"):

            score_total += 1
            result = "correct"

    else:
        score_total -= 2
        result = "incorrect"

    return result, score_total

# check_game_state()
# score_total = current score
# Returns "win", "lose", or None

def check_game_state(score_total):

    if score_total < 1:
        return "lose"

    if score_total > 39:
        return "win"

    return None

# choice()
# Main function called by the game

#Parameter:
# char = applicant dictionary
# yesno = player's choice ("1" = approve, "2" = deny)
# score_total = current score

# Returns:
# "win" if score reaches 40
# "lose" if score drops below 1
# otherwise returns (result, score_total)

def choice(char, yesno, score_total):

    approved = check_rules(char)

    result, score_total = update_score(
        approved,
        yesno,
        score_total
    )

    game_state = check_game_state(score_total)

    if game_state:
        return game_state, score_total

    return result, score_total

dsj_topic()
