#Jancarlos Rodriguez
#Lab4_3_Jancarlos.py
#Program rolls two dice a set amount of time and displays a histogram with the sum of their outcomes
#20211020

#Importing the random library as r
import random as r

def main():

    #Asks user to input how many times they would like to roll two dice
    num_rolls = int(input("Enter number of rolls: "))

    #Variable keeps track of how many times the two dices have been rolled
    rolls = 0

    #A dictionary to store the sum of the dice values
    dice_rolls = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0, "12": 0}
    dice_history = {"2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "", "11": "", "12": ""}

    #While loop to roll the two dice the amount of times the user specifies
    while rolls != num_rolls:

        #Assigning a random value to the two dice between numbers 1 and 6
        dice_one = r.randint(1,6)
        dice_two = r.randint(1,6)

        #Convert the sum into a string
        dice_sum_str = str(dice_one + dice_two)

        #Increment the amount of rolls
        rolls += 1

        #Increases the value of dice_rolls dictionary
        dice_rolls[dice_sum_str] += 1

        #Adds "*" to a number once it is rolled
        dice_history[dice_sum_str] += "*"

    #Prints the amount of times the sum of dice were rolled.
    for i in dice_history.items():
        print(i)

main()