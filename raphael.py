def dsj_topic():
    print("Wage Distribution")
    decision()

def decision():
    print("Press n to quit, or i for my source of information")
    decision = True
    while decision :
        print("Enter your yearly income to see where you rank:$")
        msg = input()
        if msg.lower() == "n" :
            decision = False
            print("quitting...")
            break
        if msg.lower() == "i" :
            print("All statistics were taken from census.gov""\nhttps://www.census.gov/data/tables/time-series/demo/income-poverty/cps-pinc/pinc-01.html""\nhttps://www.census.gov/data/tables/time-series/demo/income-poverty/cps-pinc/pinc-11.html")
        else:
            salary(msg)

# Statistics taken from census.gov
# https://www.census.gov/data/tables/time-series/demo/income-poverty/cps-pinc/pinc-01.html
# https://www.census.gov/data/tables/time-series/demo/income-poverty/cps-pinc/pinc-11.html
# I used AI to help get the % wage values from the spreadsheets.

def salary(income):
    yearly =""
    decimal = 0
    for n in income :
        if n in "1234567890" :
            yearly += n
        elif n == "." :
            decimal += 1
            if decimal > 1 :
                print("Use at most one decimal.")
                return
            yearly += n
    if yearly == "" or yearly == ".":
            print("I see no numbers.")
            return
    yearly = float(yearly)
    wages = {
    0: 0,
    15000: 9.20,
    30000: 22.00,
    40000: 33.06,
    50000: 43.28,
    55000: 49.13,
    70000: 60.55,
    85000: 70.21,
    100000: 76.04,
    120000: 82.15,
    150000: 89.80,
    200000: 95.10,
    250000: 97.40,
    500000: 99.00
    }
    for i in wages:
        if yearly == i :
            if wages[i] >= 50 :
                return print(f"You're in the top {100 - wages[i]:.2f}%")
            else :
                return print(f"You're in the bottom {wages[i]:.2f}%")
        if yearly > 500000 :
            return print(f"You're in the top 1%")
        if yearly < i:
            upper = wages[i]
            upper_salary = i
            break
        if yearly > i:
            lower = wages[i]
            lower_salary = i
    a = (yearly - lower_salary) / (upper_salary - lower_salary)
    b = upper - lower
    c = lower + (a * b)
    if c >= 50 :
        return print(f"You're in the top {100 - c:.2f}%")
    else :
        return print(f"You're in the bottom {c:.2f}%")