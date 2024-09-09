import math

user_input = ""
while user_input != ".":
    user_input = input("Please enter a number (or use a . to stop): ")
    if user_input == ".":
        print("Goodbye")
    else:
        number_input = int(user_input)
        if number_input < 2:
            print("Not prime: " + str(number_input))
        else:
            is_prime = True
            for deler in range(2, int(math.sqrt(number_input)) + 1):
                if number_input % deler == 0:
                    is_prime = False
                    break
            if is_prime:
                print("Is prime: " + str(user_input))
            else:
                print("Not prime: " + str(user_input))
