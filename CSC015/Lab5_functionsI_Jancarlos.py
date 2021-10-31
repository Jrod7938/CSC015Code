# File Lab5_functionsI_Jancarlos.py
# Practice functions definition and testing using driver main()
# Name: Jancarlos Rodriguez
# Date: 20211027

import math
import random

# Function Definitions ============================================

# -----------------------------------------------------------------
# Function to compute area of a circle
# Parameters: radius r
# Return: the are of the circle with radius r
def area_circle(r):
    area = math.pi*r**2
    return area

# -----------------------------------------------------------------
# Function radius_circle( area)
# Parameters: area of a circle
# Return: radius of a circle
def radius_circle(area):
    #Formula for radius of a circle
    radius = area / (2 * math.pi)
    return radius


# -----------------------------------------------------------------
# Function word_count(text)
# Parameters: text
# Return: The amount of words in the text
def word_count(text):
    text_count = 0
    #Checks if text is empty. If text is not empty then it runs the code
    while text != "":
        #text_count is equal to the amount of words in text
        text_count = len(text.split())
        print(f"{text} has {text_count} words.")
        #Asks the user to input another text
        text = input("Enter Text: ")
    return text_count
    
# -----------------------------------------------------------------
# Function initialize_list0(n)
# Parameters: n number of times to initialize
# Return: the completed list with "0"
def initialize_list0(n):
    #Creates an empty list
    list0 = []
    i = 1

    #Iterating over n amount of times. If the value is less than n, it gets appended to the list
    while i <= n:
        list0.append(0)
        print(list0)
        i += 1
    return ""

# -----------------------------------------------------------------
# Function initialize_list(n, value)
# Parameters: N Amount of times to print value in list
# Return: Completed list with value repeated N amount of times
def initialize_list(n, value):
    #Creates an empty list
    empty_list = []
    times = 1

    #For loop to check the value in value
    for i in value:
        #appends value to the empty list if times is less than n
        while times <= n:
            empty_list.append(i)
            times += 1
        print(empty_list)
        #Clears the values of empty_list and increments time
        empty_list = []
        times = 1
        
# -----------------------------------------------------------------
# Function sum_rolls(n)
# Parameters: n amount of times to roll a dice
# Return: sum of all face values
def sum_rolls(n):
    for i in n:
        times = 1
        total = 0
        if i > 0:
            while times <= i:
                dice = random.randint(1,6)
                print(dice)
                total += dice
                times += 1
            print(f"n={i} total is {total}")
        else:
            print(f"n={i} total is {total}")
    return total

# -----------------------------------------------------------------
# Function list_count(lst) gets a list of numbers and returns a dictionary with how many negative, positive and 0's
# Parameters: Takes in a list of numbers
# Return: The dictionary of values
def list_count(lst):

    #Creates list to edit later
    values = {"0": 0, "-": 0, "+": 0}

    #Checks if the list is empty
    if lst == "":
        print(lst)
        print(f'There are: \n{values["0"]}numbers are 0\n{values["+"]} are positive numbers\n{values["-"]} negative numbers.')
    
    #If list is not empty, number gets evaluated and - + or 0 are incremented
    else:
        num_list = lst.split()
        for n in range(len(num_list)):
            num_list[n] = float(num_list[n])
            if num_list[n] < 0:
                values["-"] += 1
            elif num_list[n] > 0:
                values["+"] += 1
            else:
                values["0"] += 1
    print(lst)
    print(f'There are: \n{values["0"]} numbers are 0\n{values["+"]} are positive numbers\n{values["-"]} negative numbers.')
    return values


# main() ----------------------------------------------------------
# Driver for testing the functions
def main():

    # 1. testing area_circle(r)
    print('*** Testing area_circle() ***')
    
    for r in range(6):
        print(f'r = {r},   area = {area_circle(r)}')

    # 2. testing radius_circle(area)
    print('*** Testing radius_circle(area) ***')
    for r in range(6):
        print(f'area = {area_circle(r)},   r= {r}')

    # 3. testing word_count(text)
    print('\n*** Testing word_count(text)***')
    word_count(input("Enter Text: "))
    
    # 4. testing initialize_list0(n)
    print('\n*** Testing initialize_list0(n)***')
    print(f"{initialize_list0(5)}")

    # 5. testing initialize_list(n,value)
    print('\n*** Testing initialize_list(n, value)***')
    init_list = [ "*", 10, 12.0 , -1]
    initialize_list(10, init_list)
    
    # 6. testing sum_rolls(n)
    print('\n*** Testing sum_rolls(n)***')
    #List of rolled numbers
    rolled_num = [-1, 0, 1, 5]

    sum_rolls(rolled_num)
    
    # 7. testing list_count(lst)
    print('\n*** Testing list_count(lst) ***')
    list_count(input("Enter numbers seperated by a space: "))

    return
# end  of main()
 
main()    # call to main()

