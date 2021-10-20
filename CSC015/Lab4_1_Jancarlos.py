#Jancarlos Rodriguez
#Lab4_1_Jancarlos.py
#Program rolls a dice a set amount of time and displays how many times an evemn or odd number is rolled
#20211019

#Importing the random library as r
import random as r

#Main Function
def main():

    #Input: How many times the user wants to roll the dice
    number_of_rolls = int(input("Enter number of rolls: "))

    #Dictionary to keep track of how many times an even or odd number was rolled
    rolled_numbers = {"Odd": 0, "Even": 0}
    
    #A list to hold all the faces that were rolled
    faces = []

    times_rolled = 0

    #While loop to run the program the set amount of times the user specified
    while times_rolled != number_of_rolls:
        face = r.randint(1, 6)

        #Checks if the face rolled is even or odd
        if face % 2 == 0:
            
            #Appends the face rolled to the faces list
            faces.append(face)

            #Increases the Even value and times rolled value
            rolled_numbers["Even"] += 1
            times_rolled += 1
            
        else:
            #Appends the face rolled to the faces list
            faces.append(face)

            #Increases the Odd value and times rolled value
            rolled_numbers["Odd"] += 1
            times_rolled += 1

    print(faces)
    print(f"You rolled {rolled_numbers['Even']} even numbers, and {rolled_numbers['Odd']} odd numbers.")

main()

