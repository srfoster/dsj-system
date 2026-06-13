#def dsj_topic():

import random  
def char():
    race = ["Elf", "Orc", "Dwarf", "Mark Zuckerberg (Lizardmen)", "Goblin", "Human", "Slime", "Hobgoblin", "Troll", "Ogre", "High Elf", "Dark Elf", "Halfling"]
    residence = ["whiterun", "Kvatch", "Jacobstown", "Jacinto", "Lordran", "Yharnam", "Raccoon City", "Wraeclast"]
    personality = ["Low Value", "Mid Value", "High Value"]
    gold = range(-200000,200000)
    traits = ["Dim Witted", "Quick Learner", "Undead", ]
    ailments = ["Cursed", "Vampirism", "Lycanthropy",]
    classtype = ["Necromancer", "Thief", "Cleric", "Warrior", "Tank", "Druid", "Ranger", "Mage", "Assassin", "Paladin", "Healer"]

    character = {
        Race: random.choice(races),
        Residence: random.choice(races),
        Personality: random.choice(races),
        Gold: random.randint(-200000,200000),
        Traits: random.sample(races, random.randint(1,3)),
        Ailments: random.choice(races),
        Class: random.choice(races),
    }
    print(character())
'''
def rule():
    rules = no faith, no vam/lycan , no goblin/hobgoblib, no short races, debt limit(+-), no undead/vampire, no rogue classes, no tanky classes, no tall races,
    new_rule = random.choice(rules)
    return rule or maybe all active rules(not sure yet)
''' 
#Looked up what random imports
#char()
#work in progress

