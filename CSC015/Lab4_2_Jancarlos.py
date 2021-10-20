#Jancarlos Rodriguez
#Lab4_2_Jancarlos.py
#Program rolls two dice a set amount of time and displays how many times the sum is 6 or 7
#20211020

#Importing the random library as r
import random as r

def main():

    #Variable to hold the amount of times the sum of both dice is 6 or 7
    successes = 0

    #Asks user to input how many times they would like to roll two dice
    num_rolls = int(input("Enter number of rolls: "))

    #Variable keeps track of how many times the two dices have been rolled
    rolls = 0

    #While loop to roll the two dice the amount of times the user specifies
    while rolls != num_rolls:

        #Assigning a random value to the two dice between numbers 1 and 6
        dice_one = r.randint(1,6)
        dice_two = r.randint(1,6)

        #Increment the amount of rolls
        rolls += 1

        #Print the values of the dice
        print(dice_one, dice_two)
        
        #If statement to check if the sum of both dice values is equal to 6 or 7
        if dice_one + dice_two == 6 or dice_one + dice_two == 7:
            successes += 1
            
    print(f"Number of successes (sum is either 6 or 7) is {successes}")

main()