#Jancarlos Rodriguez
#Lab0_JancarlosRodriguez.py
#Program finds the average of two numbers
#Input: Two numbers you want to find the average of.
#Output: The average of your numbers.
#20210908

def main():
    #Variable to continue running the program
    continueprogram = "Yes" 

    #While loop to show the average of two numbers
    while continueprogram == "Yes":

        #Saves your number inputs as variables num1 and num2 so it can calculate the average.
        num1 = input("Enter your first number.\n")
        num2 = input("Enter your second number.\n")

        #Formula for the sum of two numbers
        sum = int(num1) + int(num2)

        #Formula for the average of two numbers
        average = sum / 2

        print("The average of", num1, "and", num2, "is", average, ".")

        #Asks the user if they want to compute two more numbers, if not, then the program will quit.
        continueprogram = input("Do you want to compute the average of two more numbers? Type Yes or No\n")
        if continueprogram == "Yes":
            pass
        if continueprogram == "No":
            quit
        else:
            quit

main()