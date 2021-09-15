#Jancarlos Rodriguez
#Homework 1
#hw1_2_Jancarlos.py
#Purpose: Gets the users information, and prints it out
#20210915

def art():

    #Art because it is nice.
    print(" ....,       ,....")
    print(".' ,,, '.   .' ,,, '.")
    print(" .`   `.     .`   `.")
    print(": ..... :   : ..... :")
    print(":`~'-'-`:   :`-'-'~`:")
    print(" `.~-`.'     `.~`'.'")
    print("    ```   ___   ```")
    print("       ( . . )")
    print("")
    print("        .._..")
    print("      .'     '.")
    print("     `.~~~~~~~.`")
    print("       `-...-`")

def main():

    art()

    #Gets the users information and stores them to the variables 
    name = input("What is your name?: ")
    major = input("What is your major: ")
    class_standing = input("What is your class standing?: ")
    experience = input("What is your experience level in programming?: ")
    math_lvl = input("What is your highest completed math level?: ")

    art()
    #Prints out the variables' values to the user
    print("\nName:", name, "\nMajor:", major, "\nClass Standing:", class_standing, "\nProgramming Experience:", experience, "\nCompleted Math:", math_lvl)

main()