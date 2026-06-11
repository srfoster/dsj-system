#After some more practice during the collab project, I have room to make this shorter.
#Will complete by end of quarter!
def dsj_topic():
    main_menu()

def main_menu():
    title_subtitle("Trans Technologies", "by Oliver L. Haimson")
    options = {
        "1": "Questions",
        "2": "Review Your Answers",
        "3": "View Total Number of Attempts",
        "4": "Clear Total Number of Attempts",
        "Q": "Quit"
    }
    while True:
        title("Main Menu")
        for key, value in options.items():
            print(f"\t[{key}] {value}\n")
        user_choice = input("\nSelect an option: ").lower()
        if user_choice == "1":
            questions()
            print("You have answered all of the questions. Returning to main menu...")
            continue
        elif user_choice == "2":
            review_answers()
            continue
        elif user_choice == "3":
            review_attempts()
            continue
        elif user_choice == "4":
            total_attempts.clear()
            title_subtitle("Total attempts have been reset", "Returning to main menu...")
            continue
        elif user_choice == "q":
            print("\nExiting...\n")
            break
        else:
            error_message(user_choice)

def title(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")
    
def title_subtitle(title, subtitle):
    if len(subtitle) > len(title):
        delta = int((len(subtitle) - len(title)) / 2)
        print("=" * len(subtitle))
        print(" " * delta, title, sep = "")
        print(subtitle)
        print("=" * len(subtitle) + "\n")
    else:
        delta = int((len(title) - len(subtitle)) / 2)
        print("=" * len(title))
        print(title)
        print(" " * delta, subtitle, sep = "")
        print("=" * len(title) + "\n")

def error_message(user_input):
    print(f"\n{user_input} is not a valid selection.")

def proceed(user_prompt):
    while True:
        user_choice = input(user_prompt).lower()
        if user_choice in ("yes", "y"):
            return True
        elif user_choice in ("no", "n"):
            print("Returning to main menu...")
            return False
        else:
            error_message(f"Please limit selection to 'YES' or 'NO'. {user_choice.upper()}")

# Used AI to explore the tools and terms used in this book. There was a lot of it I did not understand. Google AI Studio is not letting me share my prompt, can send a copy of it if necessary.
q = [
    {
        "question": "You need to find a specialist for a medical procedure. How do you choose your provider?",
        "option": {
            "A": "I use a search engine and look for the highest-rated local office.",
            "B": "I look for a directory or map created by people who have the same condition as me.",
            "C": "I just go to whoever is closest and covered by my insurance; a doctor is a doctor."
        }
    },
    {
        "question": "You are building a personal profile. How much control do you want over your displayed name and history?",
        "option": {
            "A": "I want it to sync with my legal ID and social security to prove I am a real person.",
            "B": "I want the ability to change my name and wipe my history at any time as I evolve.",
            "C": "I don't care about the settings. People shouldn't be so sensitive about what's on a screen."
        }
    },
    {
        "question": "You have a great idea for a community tool. How do you want to fund the development?",
        "option": {
            "A": "I’ll pitch to a tech investor or venture capitalist to get the money to scale it globally.",
            "B": "I’ll rely on small community donations and my own unpaid labor of love to keep it independent.",
            "C": "I wouldn't build it. If it's a good idea, a big company like Apple or Microsoft would have done it already."
        }
    },
    {
        "question": "When choosing an avatar for an online space or game, which style do you prefer?",
        "option": {
            "A": "I want to look like a polished and perfect version of my physical human self.",
            "B": "I want to look like a robot, creature, or something non-human that represents my internal feelings.",
            "C": "I just use the default character. Worrying about digital identity is a waste of time."
        }
    }
]
a = [
    {
        "user answer": "",
        "scenario": "Finding a sensitive medical specialist.",
        "teaching_overview": "This choice reveals your trust in mainstream information vs. community-vetted 'trans care.'",
        "option_review": {
            "A": {
                "choice": "Use a standard search engine (Google/Yelp).",
                "feedback": "INCORRECT: Oliver Haimson, the books author, shares that he used Google to find his first surgeon, who 'botched' the surgery because search engines prioritize ads and SEO over specific medical competence (Intro, pp. 3-4). Mainstream results often lack the specific safety vetting trans communities provide (Ch. 2, p. 62)."
            },
            "B": {
                "choice": "Look for a community-created directory/map.",
                "feedback": "CORRECT: This aligns with 'Technological Trans Care.' Tools like Erin’s Informed Consent Map (Ch. 1, pp. 41-42) were built because mainstream systems often hide the specific providers who respect trans autonomy and survival (Ch. 2, p. 63)."
            },
            "C": {
                "choice": "Just go to whoever is closest/covered by insurance.",
                "feedback": "REALITY CHECK: For many, 'just going' is dangerous. Roughly 25% of trans people avoid doctors out of fear of mistreatment (Intro, p. 12, fn 3). Technology like RAD Remedy exists precisely because the 'standard' system is not safe for everyone (Ch. 2, p. 73)."
            }
        }
    },
    {
        "user answer": "",
        "scenario": "Control over name and history on a profile.",
        "teaching_overview": "This explores the concept of 'fuzziness' and 'plasticity' in digital identity.",
        "option_review": {
            "A": {
                "choice": "Sync with legal ID for verification.",
                "feedback": "INCORRECT: The book argues that 'Real Name' policies (like Facebook's) are a form of 'technological harm' (Intro, p. 19). They force a static identity on people who are in the process of transition, which can lead to being 'outed' to employers or family and being banned from the platform."
            },
            "B": {
                "choice": "Ability to change name and 'wipe' history as I evolve.",
                "feedback": "CORRECT: This is 'Transing Technology.' It values 'fuzziness' over data-mining. The creator of the Transgender Usenet Archive argues that the ability to delete or change history is a vital trans value that respects how identity evolves over time (Ch. 1, p. 48; Ch. 5, p. 173)."
            },
            "C": {
                "choice": "Settings don't matter; people shouldn't be sensitive.",
                "feedback": "REALITY CHECK: When a system forces a 'deadname' (a name no longer used) on a user, it’s not just a screen issue—it creates barriers to employment, credit history, and air travel (Intro, pp. 18-19). These settings have massive material consequences for survival."
            }
        }
    },
    {
        "user answer": "",
        "scenario": "Funding a community-help tool.",
        "teaching_overview": "This highlights the tension of 'Trans Capitalism.'",
        "option_review": {
            "A": {
                "choice": "Pitch to Venture Capitalists to scale up.",
                "feedback": "INCORRECT: When the app Solace took Venture Capital money, the community 'ratioed' them (Ch. 5, pp. 141-143). Critics argue that profit-driven tech eventually serves investors' interests and data-mining rather than the community’s safety (Ch. 5, p. 165)."
            },
            "B": {
                "choice": "Rely on Mutual Aid and unpaid 'labor of love.'",
                "feedback": "CORRECT: This is the 'Mutual Aid' model (Ch. 5, p. 145). While it prevents exploitation, Haimson notes these creators often face extreme burnout and exhaustion because they are performing a vital social service for free (Ch. 5, pp. 150-153)."
            },
            "C": {
                "choice": "Wait for big companies (Apple/Google) to build it.",
                "feedback": "REALITY CHECK: Mainstream companies have a 'cisgender-as-default' bias (Intro, p. 19; Ch. 3, p. 95). They rarely build trans-inclusive features until years after trans people have already 'hacked' the solutions themselves as a form of political resistance (Ch. 1, pp. 43-44)."
            }
        }
    },
    {
        "user answer": "",
        "scenario": "Choosing a digital avatar for an online space.",
        "teaching_overview": "This looks at 'Trans-Futurism' and the power of the 'Robot Avatar.'",
        "option_review": {
            "A": {
                "choice": "Look like a polished, 'perfect' human self.",
                "feedback": "CORRECT: This is 'Inclusionist.' Tech like 3D 'nipple sliders' for surgery help trans people communicate and visualize their 'ideal' human self to doctors (Ch. 2, pp. 75-76), using digital tools to achieve 'embodied realness' (Ch. 6, pp. 204-205)."
            },
            "B": {
                "choice": "Look like a robot/creature that represents internal feelings.",
                "feedback": "CORRECT: This is 'Utopian.' Creator LemmaEOF uses a Fat Robot avatar to display emotions via a screen face (Ch. 6, pp. 191-192). It 'transes' the human boundary to create a new way to communicate that the physical world doesn't allow."
            },
            "C": {
                "choice": "Just use a default gray character; identity is a waste of time.",
                "feedback": "REALITY CHECK: For those in hostile physical environments, digital identity is not 'fake'—it is 'water.' Haimson argues that transness is 'natural' online, and for many, an avatar is the only place they can truly breathe and exist safely (Conclusion, p. 218)."
            }
        }
    }
]
total_attempts = []

def questions():
    title_subtitle("Questions", "Please consider the following")
    index = 0
    attempts = 0
    for item in q:
        valid_selection = False
        while not valid_selection:
            print(f"Question #{index + 1}:")
            print("Total attempts:", attempts)
            print(f'\n{item["question"]}')
            for key, value in item["option"].items():
                print(f"\n\t[{key}] {value}")
            user_choice = input("\nSelect an answer: ")
            if user_choice in ["a", "A", "b", "B", "c", "C"]:
                valid_selection = True
                attempts += 1
                total_attempts.append(attempts)
                #print(total_attempts)
                a[index]["user answer"] = user_choice
            else:
                error_message(user_choice)
            attempts += 1
        attempts = 0
        index += 1
        #print(index)
        if index == 4:
            # bug here, doesn't seem to matter how you answer. VSCode Copilot gave me the solution if not proceed().
            if not proceed("Would you like to return to the main menu? (Yes/No): "):
                return
        else:
            if not proceed("Would you like to continue to the next question? (Yes/No): "):
                return

def review_answers():
    title_subtitle("Reviewing", "Answers")
    index = 0
    for item in a:
        print(f'Question #{index + 1}: {item["scenario"]}\n')
        user_choice = item["user answer"].upper()
        if not user_choice:
            error_message("You have not answered any questions. Please select 'Questions' from main menu. Returning to main menu...")
            continue
        print(f'You chose [{user_choice}]\n')
        print(f'From the book: {item["teaching_overview"]}\n')
        #Looked up how to index into a nested dictionary. https://www.bing.com/search?pglt=299&q=how+to+index+into+a+nested+dictionary+python&cvid=cc77d250e0564b5fa85f46bf6802b515&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhAMgYIAhAAGEAyBggDEAAYQDIGCAQQABhAMgYIBRAAGEAyBggGEAAYQDIGCAcQABhAMgcICBDrBxhA0gEJMTUyNzZqMGo3qAIAsAIA&FORM=ANNTA1&PC=HCTS
        print(f"[{user_choice}] {item['option_review'][user_choice]['choice']}\n")
        print(f'Feedback: {item["option_review"][user_choice]["feedback"]}\n')
        index += 1
        #print(index)
        if index == 4:
            # same bug as questions()
            if not proceed("Would you like to return to the main menu? (Yes/No): "):
                return
        else:
            if not proceed("Would you like to continue to the next question? (Yes/No): "):
                return
                
def review_attempts():
    title_subtitle("Total Number of Attempts", "Per Question")
    index = 1
    if total_attempts == []:
        print("You have not made any attempts yet.")
        if not proceed("Would you like to continue to the main menu? (Yes/No): "):
            return
        return
    for item in total_attempts:
        print(f"Question #{index}: {item} \n")
        index += 1
    if not proceed("Would you like to continue to the main menu? (Yes/No): "):
        return
#dsj_topic()