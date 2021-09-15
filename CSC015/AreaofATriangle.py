#Jancarlos Rodriguez
#AreaofATriangle.py
#Input: Input the base and height of the triangle
#Output: The area of a triangle.
#20210908

def main():
    #Variable to continue running the program
    continueprogram = "Yes" 

    #While loop to show the area of the triangle
    while continueprogram == "Yes":
        height = input("Enter the height of the triangle.\n")
        base = input("Enter the base of the triangle.\n")

        area = (int(height) * int(base)) / 2

        print("The area of the triangle is", area, ".")

        #Asks the user if they want to compute another area of a triangle, if not, then the program will quit.
        continueprogram = input("Do you want to compute the area of another triangle? Type Yes or No\n")
        if continueprogram == "Yes":
            pass
        if continueprogram == "No":
            quit
        else:
            quit

main()