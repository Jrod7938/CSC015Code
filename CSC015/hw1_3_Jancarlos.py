#Jancarlos Rodriguez
#Homework 1
#hw1_3_Jancarlos.py
#Purpose: Finds the Area of a rectangle
#20210915

def art():
    #Fancy display, just because I can :,)
    print("*****                     *****")
    print("*   *                     *   *")
    print("*   * Area of a Rectangle *   *")
    print("*   *                     *   *")
    print("*****                     *****")

def main():

    art()
    #Takes user input and saves them as variables
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))

    #Area of a rectangle formula
    area_rectangle = length * width

    #Prints the inputs that the user entered
    print("\nYou Entered\nLength:", length, "\nWidth:", width)

    #Prints the area of a rectangle
    print("\nThe area of the rectangle is:", area_rectangle)

    art()

main()