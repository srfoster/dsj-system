def keep_going():
    while True:
        print("\n.  .  .  .  .")
        user_input = (input(">> ('exit' to quit | ENTER to continue): ")).strip().lower()
        if user_input == "exit":
            to_continue = False
            break
        elif user_input == "":
            to_continue = True
            print(".  .  .  .  .\n")
            break
        else:
            print("Sorry, invalid input")
    return to_continue


content = {
            "section_divider": "——————————————————— - - - ——————————————————— \n", 
            "welcome_intro": '''Welcome!\n
This interactive tool is designed to introduce some important concepts and ideas around disability and accessibility in the context of architecture.\n
As you move through the experience you will unlock new areas of a small map each with new topics to explore.\n
You will use the ENTER key to progress through the experience. 
You can also exit the program at any time by typing 'exit' and then pressing ENTER.''',
            "parking_lot": '''\n-*- A. Parking Lots -*-\n
• Clearly marked and specifically reserved parking spaces allow people with disabilities, who have the correct parking permit, to park in a space that provides:
	⁃ Additional area around a vehicle to enter, exit, and move about
	⁃ Close proximity to the building’s entrance and any accessibility features of the entrance\n
Let's head inside...''',
            "building_entrance_1": '''\n-*- B. Building Entrances -*-\n
• Ramps are the most common solution to a building entrance that has stairs, but in some locations a ramp is not feasible. 

• Other options might include a lift for wheelchairs or offering an alternative entrance without stairs.''',
            "building_entrance_2": '''• Any doorway also needs to be safely accessible for everyone. This means doorways that are free of clutter with no obstructions, are reasonably wide and able to be opened and passed through easily.

• For doors that are difficult to use, for example if they are heavy to open or cannot be held open easily while passing through, buttons can be installed to automatically open, hold open, and then close a door.''',
            "counter": '''\n-*- C. Surfaces of Use -*-\n
• Counters, tables, and similar surfaces are absolutely everywhere, and so can quickly change the way a disabled person interacts with a space.

• Some examples of these surfaces include…
	⁃ Pharmacy windows
	⁃ Bank counters or ATM locations
	⁃ Checkout counters for merchandise or groceries
	⁃ Reception desks at medical offices
	⁃ Information or check-in desks at hotels, airports, and businesses
	⁃ Desks in an office or tables in a restaurant

• These surfaces need to be an appropriate height, with space below for legs and toes, and not be too deep to reach across.''',
            "stairs_1": '''\n-*- G. Stairs -*-\n
• Stairs, or even escalators, inside buildings pose challenges as well. 

• Elevators are the most common solution, sometimes replacing stairs completely, since they provide broad access and assistance for non-disabled as well as disabled people.''',
            "stairs_2": '''• Very frequently, accommodations in the built environment that are beneficial for people with disabilities are also beneficial for many other groups of people, too. For example, someone with joint pain, a pregnant woman, or someone who is simply carrying heavy items are all also positively impacted by an elevator being available.''',
            "stairs_3": '''• Communication in and around an elevator is also important. Both auditory and visual signals when a button has been pushed, to indicate the direction of travel, alerts when doors are opening and closing, and to show the current floor.''',
            "communication": '''\n-*- D. Communications -*-\n
• Communications in the built environment convey critical information that needs to be available to all. Examples of accessible communications include:
	⁃ Physical signs that have braille to label room numbers, locations, directions etc.
	⁃ Closed captioning provided in movies, lectures, or other visual screenings.
	⁃ Warning systems, such as fire alarms, that include visual as well as auditory alerts.''',
            "restroom": '''\n-*- E. Restrooms -*-\n
• Most accessibility features of restrooms are designed to assist people who have disabilities related to mobility. This looks like:
	⁃ Sinks are an appropirate height, including a reasonably reached faucet, soap, and hand drying area, or a specifically accessible sink station is available.
 	⁃ At least one stall has wall railings and enough area for a wheelchair, or a similar layout of space for safe movement can be accessed in a single-occupant restroom.

• This is a clear example of how accessible restrooms can assist non-disabled people as well: many of these features help children and their parents to use the restroom in an easier, and also often safer, way.''',

            "use_elements_1": '''\n-*- F. Elements of Use -*-\n
• The floor and area around elements of a space, for example drinking fountains, fire extinguishers, or washers/dryers, must be clear, sufficiently sized, and correctly positioned to make the element accessible.''',
            "use_elements_2": '''• Operation of these elements must also accessible. Usually this requires they be reachable and usable with one hand, do not need more than five pounds of force, and do not require tight grasping, twisting of a wrist, or pinching to operate.''',
            "turning_space": '''\n-*- H. Turning Space -*-\n
• Adequate space to move around, most commonly thought of as turning space, is required. 

• Examples of where this important concept can be found are:
	⁃	Toilet facilites
	⁃	Dressing and locker rooms
	⁃	Holding and housing cells
	⁃	Patient bedrooms

• Finally, another important concept to consider in these instances is door swing, and how opening a door in the area could impact turning space and access to other elements.''', 
            "end_text": '''We've reached the end of our map!\n
Thank you for taking time to explore accessibility in architecture and design through a small sample of our built environment.\n
If you're interested in learning more, information from the following sources was used in the creation of this program:\n'''
            } 

sources = ["Hendren, S. (2020). What Can a Body Do? : How We Meet the Built World. Penguin Publishing Group.", 
           "Gissen, D. (2023). The Architecture of Disability. U of Minnesota Press.",
           "U.S. Access Board - About the ABA guide. (2026). Access-Board.gov. https://www.access-board.gov/aba/guides/", 
           "About the 2010 ADA Standards for Accessible Design. (2020). Northeastada.org. https://www.northeastada.org/resource/about-the-2010-ada-standards-for-accessible-design"]

ascii_map = {"blank_map": 
                  r'''                           --:--          
                           │∩∩∩│          
────────│───────│─[(≈≈≈)]─:│∩∩∩│          
    ╔╦╦╗│  ºöº  │:  ▒?▒    =====────────│ 
▒?▒ ╚╩╩╝│Φ     «·»          ▒?▒ │ │ │ │ │ 
   ──:  │(0  ▒?▒│           ____/────── │ 
     │  │───────│     ▒?▒  ║≡≡≡≡ │ │ │  │ 
     │  │            *Ω*Ω* ║   │════════│ 
  ───: / \            ║════║/∙\│¬¬  ºöº║  
  ││││ ▒?▒   ⌐  ▒?▒  ¬║∞∩∩∞     ≈≈    Φ║  
  ─────\│/   [[=====]]║ ██   ▒?▒     0)║  
 ───────│─────────────║════════════════║  ''',
                "a_parking_lot": 
                  r'''────────│   
      ╔╦╦╗│   
  ▒A▒ ╚╩╩╝│   
     ──:  │   
       │  │   
       │  │   
    ───: / \  
    ││││ ▒?▒  
    ─────\│/  
   ───────│  ''',
                "b_building_entrance": 
                  r''' ────────│                   
     ╔╦╦╗│                   
 ▒A▒ ╚╩╩╝│                   
    ──:  │                   
      │  │───────│           
      │  │                   
   ───: / \            ║════ 
   ││││ ▒B▒      ▒?▒   ║     
   ─────\│/   [  ---  ]║     
  ───────│─────────────║     ''',
                "c_counter": 
                  r'''  ────────│                    
      ╔╦╦╗│                    
  ▒A▒ ╚╩╩╝│                    
     ──:  │       │            
       │  │───────│     ▒?▒  ║ 
       │  │             Ω    ║ 
    ───: / \            ║════║ 
    ││││ ▒B▒   ⌐  ▒C▒  ¬║      
    ─────\│/   [[=====]]║      
   ───────│─────────────║ ''',
                "d_communication": 
                  r''' ────────│───────│─-(---)-──│ 
     ╔╦╦╗│       │:  ▒?▒      
 ▒A▒ ╚╩╩╝│      «·»           
    ──:  │    ▒?▒│            
      │  │───────│     ▒D▒  ║ 
      │  │            *Ω*Ω* ║ 
   ───: / \            ║════║ 
   ││││ ▒B▒   ⌐  ▒C▒  ¬║      
   ─────\│/   [[=====]]║      
  ───────│─────────────║ ''',
                "e_restroom": 
                  r'''  ────────│───────│─[─────]──|              
      ╔╦╦╗│  ºöº  │:  ▒?▒    
  ▒A▒ ╚╩╩╝│Φ     «·»               
     ──:  │(0  ▒E▒│                 
       │  │───────│     ▒D▒  ║           
       │  │            *Ω*Ω* ║ 
    ───: / \            ║════║   
    ││││ ▒B▒   ⌐  ▒C▒  ¬║  
    ─────\│/   [[=====]]║   
   ───────│─────────────║ ''',
                "f_elements": 
                  r'''  ────────│───────│─[(≈≈≈)]──|       
      ╔╦╦╗│  ºöº  │:  ▒F▒    =====─ 
  ▒A▒ ╚╩╩╝│Φ     «·»          ▒?▒ │ 
     ──:  │(0  ▒E▒│           ____/ 
       │  │───────│     ▒D▒  ║      
       │  │            *Ω*Ω* ║      
    ───: / \            ║════║      
    ││││ ▒B▒   ⌐  ▒C▒  ¬║           
    ─────\│/   [[=====]]║           
   ───────│─────────────║''',
                "g_stairs": 
                  r'''                            --:--         
                            │∩∩∩│         
 ────────│───────│─[(≈≈≈)]─:│∩∩∩│         
     ╔╦╦╗│  ºöº  │:  ▒F▒    =====────────│
 ▒A▒ ╚╩╩╝│Φ     «·»          ▒G▒ │ │ │ │ │
    ──:  │(0  ▒E▒│           ____/────── │
      │  │───────│     ▒D▒  ║≡≡≡≡ │ │ │  │
      │  │            *Ω*Ω* ║   │════════│
   ───: / \            ║════║/∙\│       ║ 
   ││││ ▒B▒   ⌐  ▒C▒  ¬║                ║ 
   ─────\│/   [[=====]]║      ▒?▒       ║ 
  ───────│─────────────║════════════════║ ''',
                "h_turning_space": 
                  r'''                           --:--          
                           │∩∩∩│          
────────│───────│─[(≈≈≈)]─:│∩∩∩│          
    ╔╦╦╗│  ºöº  │:  ▒F▒    =====────────│ 
▒A▒ ╚╩╩╝│Φ     «·»          ▒G▒ │ │ │ │ │ 
   ──:  │(0  ▒E▒│           ____/────── │ 
     │  │───────│     ▒D▒  ║≡≡≡≡ │ │ │  │ 
     │  │            *Ω*Ω* ║   │════════│ 
  ───: / \            ║════║/∙\│¬¬  ºöº║  
  ││││ ▒B▒   ⌐  ▒C▒  ¬║∞∩∩∞     ≈≈    Φ║  
  ─────\│/   [[=====]]║ ██   ▒H▒     0)║  
 ───────│─────────────║════════════════║'''}



def dsj_topic():
    print(content["section_divider"])
    print(content["welcome_intro"])
    print("Ready to get started?")

    if keep_going():
        print(content["section_divider"])
        print(ascii_map["a_parking_lot"])
        print(content["parking_lot"])
    else:
        return
    
    if keep_going():
        print(content["section_divider"])
        print(ascii_map["b_building_entrance"])
        print(content["building_entrance_1"])
        if keep_going():
            print(content["building_entrance_2"])
        else:
            return
    else:
        return
    
    if keep_going():
        print(content["section_divider"])
        print(ascii_map["c_counter"])
        print(content["counter"])
    else:
        return
    
    if keep_going():
        print(content["section_divider"])
        print(ascii_map["d_communication"])
        print(content["communication"])
    else:
        return
    
    if keep_going():
        print(content["section_divider"])
        print(ascii_map["e_restroom"])
        print(content["restroom"])
    else:
        return
    
    if keep_going():
        print(content["section_divider"])
        print(ascii_map["f_elements"])
        print(content["use_elements_1"])
        if keep_going():
            print(content["use_elements_2"])
        else:
            return
    else:
        return

    if keep_going():
        print(content["section_divider"])
        print(ascii_map["g_stairs"])
        print(content["stairs_1"])
        if keep_going():
            print(content["stairs_2"])
            if keep_going():
                print(content["stairs_3"])
            else:
                return
        else:
            return
    else:
        return

    if keep_going():
        print(content["section_divider"])
        print(ascii_map["h_turning_space"])
        print(content["turning_space"])
    else:
        return
    
    if keep_going():
        print(content["end_text"])
        for source in sources:
            print(f"\t• {source}")
    else:
        return
