#def dsj_topic():

import random  
def char():

    character = {
        "Race": random.choice(["Elf", "Orc", "Dwarf", "Mark Zuckerberg (Lizardmen)", "Goblin", "Human", "Slime", "Hobgoblin", "Troll", "Ogre", "High Elf", "Dark Elf", "Halfling"]),
        "Residence": random.choice(["whiterun", "Kvatch", "Jacobstown", "Jacinto", "Lordran", "Yharnam", "Raccoon City", "Wraeclast"]),
        "Personality": random.choices(["Low Value", "Mid Value", "High Value"], [5,4,1])[0], #these numbers are weights
        "Gold": random.randint(-200000,200000),
        "Traits": random.sample(["Dim Witted", "Quick Learner", "Undead", "Cannibal", "Lucky", "Anger Issues", "Pyromaniac", "Deaf", "Blind", "Stupid", ], random.randint(1,3))[0],
        "Ailments": random.choices(["Cursed", "Vampirism", "Lycanthropy", "None",], [1,1,1,3])[0],
        "Class": random.choice(["Necromancer", "Thief", "Cleric", "Warrior", "Tank", "Druid", "Ranger", "Mage", "Assassin", "Paladin", "Healer"]),
    }
    #print(character)
    return character #this is a dictionary with all the random character attributes
'''
def rule():
    rules = no faith, no vam/lycan , no goblin/hobgoblib, no short races, debt limit(+-), no undead/vampire, no rogue classes, no tanky classes, no tall races, high values always accepted, no ailments, 
    new_rule = random.choice(rules)
    return rule or maybe all active rules(not sure yet)
''' 
#Looked up what random imports
#char()
#work in progress

# Cody, my part! The choice system ;D
def choice(char, active_rules, yesno, score_total):

    approved = True

    for rule in active_rules:
        if char[rule["trait"]] != rule["value"]:
            approved = False

    if (approved and yesno == "1") or \
       (not approved and yesno == "2"):

        score_total += 1
        result = "correct"

    else:
        score_total -= 2
        result = "incorrect"

    if score_total < 1:
        return "lose"

    if score_total > 39:
        return "win"

    return result, score_total
