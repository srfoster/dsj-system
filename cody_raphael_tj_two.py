#def dsj_topic():

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
include_rules = [] #include lists requirements that you must accept
exclude_rules = [] #exclude lists attributes you must deny

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

# Parameters:
# char = applicant dictionary
# active_rules = list of currently active rules
# yesno = player's choice ("1" = approve, "2" = deny)
# score_total = current score

def choice(char, active_rules, yesno, score_total):
    
    approved = True
    
    # Checking if applicant passes all active rules
    for rule in active_rules:
        if char[rule["trait"]] != rule["value"]:
            approved = False

    # Player matched the WMD decision
    if (approved and yesno == "1") or \
       (not approved and yesno == "2"):

        score_total += 1
        result = "correct"

    # Player made wrong decision
    else:
        score_total -= 2
        result = "incorrect"

    # Losing condition
    if score_total < 1:
        return "lose"

    # Winning condition
    if score_total > 39:
        return "win"

    # Returns the result and updates the score
    return result, score_total
