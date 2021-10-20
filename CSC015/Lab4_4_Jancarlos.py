#Jancarlos Rodriguez
#Lab4_4_Jancarlos.py
#Program rolls two dice until the current rolled face is smaller than the last rolled face. Program also adds successful rolls together.
#20211020

#Importing the random library as r
import random as r

def main():

    #Variable to run the program
    run = 0

    #Empty list that gets filled with dice_sum
    rolled_faces = []

    #Variables
    face_totals = 0
    dice_sum = 0
    success = 0
    last_dice_sum = 0

    #While loop to roll a dice and check to see if it is larger than the previous number rolled
    while run == 0:

        #Assigning a random value to the two dice between numbers 1 and 6
        dice_one = r.randint(1,6)
        dice_two = r.randint(1,6)

        #Sum of dice_one and dice_two
        dice_sum = dice_one + dice_two

        #Appends the value of dice_sum to the rolled_faces list
        rolled_faces.append(dice_sum)

        #Check if the sum of the dices is larger than the previous roll
        if dice_sum >= last_dice_sum:
            face_totals += dice_sum
            success += 1
        else:
            run = 1
        last_dice_sum = dice_sum

    print(f"All rolled faces: {rolled_faces}\nTotal of the successful rolls: {face_totals}\nNumber succesful rolls: {success}")

main()