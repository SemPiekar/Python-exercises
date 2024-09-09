input("Hier opeten of meenemen?")
choice2 = input("Burgers of drankjes?").lower()
if choice2 == "burgers":
    choice3 = input("Welke burger wilt u hebben? \n Hamburger \n Cheeseburger \n Big Mac \n Quarter Pounder").lower()
    if choice3 == "quarter pounder":
        choice4 = input("Wilt u kaas?").lower()
        if choice4 == "ja":
            print("Quarter Pounder met kaas")
        elif choice4 == "no":
            print("Quarter Pounder zonder kaas")
    else:
        print(choice3)
elif choice2 == "drankjes":
    choice3 = input("Warme of koude drankjes?").lower()
    if choice3 == "koude drankjes":
        choice5 = input("Welke koude drankjes? \n Coca Cola \n Cola Zero \n 7-up \n Fanta \n Fristi").lower()
        print(choice5)
    elif choice3 == "warme drankjes":
        choice6 = input("Welke warme drankjes? \n Koffie \n Cappucino \n Chocolademelk")
        print(choice6)
