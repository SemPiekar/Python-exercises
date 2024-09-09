choice = input("Is the patient an adult or an child").lower()
if choice == 'adult':
    choice2 = input("Does the patient have common TB symptoms?").lower()
    if choice2 == 'yes':
        print("Treat as likely TB patient and perform full TB exam")
    elif choice2 == 'no':
        print("Have patient report back if unwell; return in 1 month for checkup")
elif choice == 'child':
    choice2 = input("Can TB test be given?").lower()
    if choice2 == 'yes':
        print("Administer TB test \n Assess TB test results and child's condition")
    elif choice2 == 'no':
        choice3 = input("Is the child well?").lower()
        if choice3 == 'yes':
            print("6 months preventive isoniazid \n Have parent bring in if child shows any symptoms")
        elif choice3 == 'no':
            print("Take full history. Examine for TB \n If TB is likely diagnosis treat for TB \n If other diagnosis, treat for TB \n If other diagnosis more likely, treat as needed and watch for TB symptoms")
