#seth
#the only code here that isn't mine is stuff I got from lookng Ulysses' project
#I also took the text formatting of the opening from looking at Randy's project
def dsj_topic():
    print("===================================================\n\t\tCalculate you E-score\n===================================================\n*stats are unverified and meant to be over dramatic\nbut they are also meant to reflect the sad truth of\nhow these scores likely work (aka bigotry warning)\n\n\n")
    start()
    print("\n\n\nthank you for playing.:)\n\nclosing")
    for i in range(5):
        print(".")
    print("closed")
    return

def start():
    p = str(input("Do you want to play? (Y/N): "))
    if p.lower() == "y":
        GO()
    elif p.lower() == "n":
        print("Ok then")
        return
    elif p == "PINGAS":
        print("\nSnooPING AS usual, I see!\n")
        start()
    else:
        print("\ninvaled input plese respond with only \"Y\" or \"N\"\n")
        start()
def GO():
    q = ["how tall are you?","what type of neighborhood do you live in?","what race are you?","What is your gender?"]
    q1a = ["A: mansion rode.", "B: standard suburban lane.", "C: apartment complex.", "D: the local ghetto."]
    q2a = ["A: white","B: other"]
    q3a = ["A: Man","B: Woman","C: Trans woman","D: other"]
    q4a = ["A: 5\'9\" or below","B: 5\'10\" to 5\'11\"","C: 6\' or above"]
    qn = 0
    score = 2.5
    for i in range(4):
        print(q[i])
        if qn == 1:
            for anwser in q1a:
                print(anwser)
            pa = str(input(""))
            if pa.lower() == "a":
                score = score + 1
            elif pa.lower() == "b":
                score = score + .5
            elif pa.lower() == "c":
                score = score
            elif pa.lower() == "d":
                score = score - 0.5
            else:
                print("\nthe computer did not understand your input and exploded")
                return "\nboom"
        if qn == 2:
            for anwser in q2a:
                print(anwser)
            pa = str(input(""))
            if pa.lower() == "a":
                score = score
            elif pa.lower() == "b":
                score = score - 1
            else:
                print("\nthe computer did not understand your input and exploded")
                return "\nboom"
        if qn == 3:
            for anwser in q3a:
                print(anwser)
            pa = str(input(""))
            if pa.lower() == "a":
                score = score + 1
            elif pa.lower() == "b":
                score = score + 0.5
            elif pa.lower() == "c" or pa.lower() == "d":
                score = score - 0.5
            else:
                print("\nthe computer did not understand your input and exploded")
                return "\nboom"
            
        if qn == 0:
            for anwser in q4a:
                print(anwser)
            pa = str(input(""))
            if pa.lower() == "c":
                score = score + 0.5
            elif pa.lower() == "b":
                score = score
            elif pa.lower() == "a":
                score = score - 0.5
            else:
                print("\nthe computer did not understand your input and exploded")
                return "\nboom"
            
        qn = qn+ 1
    print(f"\nyour e-score is {score}")
    if str(input("do you want to play again? (y/else): ")).lower() == "y":
        GO()
    else:
        return
