#Jancarlos Rodriguez
#CSC Assignment: Conditionals
#hw2_1_Jancarlos.py
#Program asks the user where they would like to sit.
#20210929

def main():

    #Prompts
    prompt = "Select a sitting area:\nFor orchestra enter letter O or o\nFor Tier 1, enter 1\nFor Tier 2, enter 2\nFor Balcony, enter B or b\n"
    orchestra_prompt = "Enter F or f for orchestra front\nEnter C or c for orchestra center\nEnter B or b for orchestra back\n"
    balcony_prompt = "Enter F or f for balcony front\nEnter B or b for balcony back\n"
    price_prompt = "Price per ticket is: "

    #Constants
    orchestra_front = 95.00
    orchestra_center = 150.50
    orchestra_back = 80.00
    tier_one = 250.00
    tier_two = 150.00
    balcony_front = 60.00
    balcony_back = 45.50

    #Ask the user to select a seating area(orchestra, first, second tire or balcony)
    print(prompt)
    area = input("Enter Sitting area choice: ")

    #Orchestra prompt
    if area == "O" or area == "o":
        print(orchestra_prompt)
        orchestra_section = input("Enter your choice: ")
        if orchestra_section == "F" or orchestra_section == "f":
            print(price_prompt, "$", orchestra_front)
            num_tickets = float(input("How many tickets? "))
            total = num_tickets * orchestra_front
            print(f"{num_tickets} tickets at the Orchestra front cost ${total:.2f}")
        elif orchestra_section == "C" or orchestra_section == "c":
            print(price_prompt, "$", orchestra_center)
            num_tickets = float(input("How many tickets? "))
            total = num_tickets * orchestra_center
            print(f"{num_tickets} tickets at the Orchestra center cost ${total:.2f}")
        elif orchestra_section == "B" or orchestra_section == "b":
            print(price_prompt, "$", orchestra_back)
            num_tickets = float(input("How many tickets? "))
            total = num_tickets * orchestra_back
            print(f"{num_tickets} tickets at the Orchestra back cost ${total:.2f}")
        #Catch All
        else: 
            print("Invalid sitting area. Quiting program. Start again.")
            return

    #Tier 1 Prompt
    elif area == "1" or area == 1:
        print(price_prompt, "$", tier_one)
        num_tickets = float(input("How many tickets? "))
        total = num_tickets * tier_one
        print(f"{num_tickets} tickets at first tier cost ${total:.2f}")

    #Tier 2 Prompt
    elif area == "2" or area == 2:
        print(price_prompt, "$", tier_two)
        num_tickets = float(input("How many tickets? "))
        total = num_tickets * tier_two
        print(f"{num_tickets} tickets at second tier cost ${total:.2f}")

    #Balcony Prompts
    elif area == "B" or area == "b":
        print(balcony_prompt)
        balcony_section = input("Enter your choice: ")
        if balcony_section == "F" or balcony_section == "f":
            print(price_prompt, "$", balcony_front)
            num_tickets = float(input("How many tickets? "))
            total = num_tickets * balcony_front
            print(f"{num_tickets} tickets at the Balcony front cost ${total:.2f}")
        elif balcony_section == "B" or balcony_section == "b":
            print(price_prompt, "$", balcony_back)
            num_tickets = float(input("How many tickets? "))
            total = num_tickets * balcony_back
            print(f"{num_tickets} tickets at the Balcony back cost ${total:.2f}")
        #Catch all
        else: 
            print("Invalid sitting area. Quiting program. Start again.")
            return

    #Catch All
    else:
        print("Invalid sitting area. Quiting program. Start again.")
        return

main()