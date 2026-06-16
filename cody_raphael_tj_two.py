def dsj_topic():
    game()

include_rules = [] #include lists requirements that you must accept
exclude_rules = [] #exclude lists attributes you must deny

def game():
    print("You are here to ACCEPT and DENY applicants for hiring by the company.")
    input("When you are ready to get to work, press any key to continue...")
    score = 10
    count = 0
    week = 0
    while count <= 5:
        while True:
            print("Current Applicant: ")
            applicant = char()
            for key, value in applicant.items():
                print(f"{key}: {value}")
            print("(Choose one) APPROVE or DENY applicant?")
            decision = input("Applicant status: ")
            if decision.lower() != "approve" and decision.lower() != "deny":
                print("You can only APPROVE or DENY.")
                continue
            else:
                result, score = choice(applicant, decision, score)
                print(result)
                count += 1
                print(f"Your score is: {score}")
            if count == 5:
                add_rule()
                if len(include_rules) > 0:
                    for key, value in include_rules.items():
                        print(f"{key}: {value}")
                if len(exclude_rules) > 0:
                    for key, value in exclude_rules.items():
                        print(f"{key}: {value}")
                week += 1
                print(f"End of week {week}.")

import random  

def char():

    character = {
        "Race": random.choice(["Elf", "Orc", "Dwarf", "Mark Zuckerberg (Lizardmen)", "Goblin", "Human", "Slime", "Hobgoblin", "Troll", "Ogre", "High Elf", "Dark Elf", "Halfling"]),
        "Residence": random.choice(["whiterun", "Kvatch", "Jacobstown", "Jacinto", "Lordran", "Yharnam", "Raccoon City", "Wraeclast"]),
        "Personality": random.choices(["Low Value", "Mid Value", "High Value"], [5,4,1])[0], #these numbers are weights
        "Gold": random.randint(-200000,200000),
        "Traits": random.sample(["Dim Witted", "Quick Learner", "Undead", "Cannibal", "Lucky", "Anger Issues", "Pyromaniac", "Deaf", "Blind", "Stupid", "Suspicious", "Mysterious", "Good Natured"], random.randint(1,3)),
        "Ailments": random.choices(["Cursed", "Vampirism", "Lycanthropy", "None", "Hollowed"], [1,1,1,4,1])[0],
        "Class": random.choice(["Necromancer", "Thief", "Cleric", "Warrior", "Tank", "Druid", "Ranger", "Mage", "Assassin", "Paladin", "Healer"]),
    }
    #print(character)
    return character #this is a dictionary with all the random character attributes
#char()
#uncomment print(character) and run char() to see what this returns


#check and call on these 2 for the rules, they are lists of dictionarys. print them below add_rule() if you want an idea of what they are.


def add_rule(): #when called upon this creates rules and adds them to include/exclude rules. The first time its called it creates 1 include rule and 1 exclude rule. It has rule caps, so you can call this at the start of each week.
    include = [
        {"High value personalities must be chosen": ["High Value"]},
        {"Accept applicants with more than 150,000 gold":[150000]}
    ]

    exclude = [
        {"No Faith, deny any clerics or paladins": ["Cleric", "Paladin"]},
        {"No goblins of any kind": ["Hobgoblin", "Goblin"]}
    ]
    if not include_rules and not exclude_rules:
        include_rules.append(random.choice(include))
        exclude_rules.append(random.choice(exclude))
    elif len(include_rules) == len(exclude_rules):
        if len(exclude_rules) < 4:
            exclude_rules.append(random.choice(exclude))
    elif len(exclude_rules) < 4 and len(include_rules) < 4:
        rule_choice = random.choice([include, exclude])
        if rule_choice == include:
            include_rules.append(random.choice(include))
        if rule_choice == exclude:
            exclude_rules.append(random.choice(exclude))
    elif len(exclude_rules) < 4:
        exclude_rules.append(random.choice(exclude))
    elif len(include_rules) < 4:
        include_rules.append(random.choice(include))
    else:
        return
    

    #print(include_rules)
    #print(exclude_rules)



    '''
    rules = no faith, no vam/lycan , no goblin/hobgoblib, no short races, debt limit(+-), no undead/vampire, no rogue classes, no tanky classes, no tall races, high values always accepted, no ailments, 
    new_rule = random.choice(rules)
    return rule or maybe all active rules(not sure yet)
''' 
#Looked up what random imports
#char()
#rule()
add_rule()
#work in progress

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

#dsj_topic()
