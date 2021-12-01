# ---- Function Definitions ---------------------------------------------

# Function to convert a list to list of ints. If successfull it changes the list
# Parameters: list lst
# Return: True if list converted successfully and False otherwise
# Note: if a list item cannot be converted to integer (ValueError), the
# function will not give run time error, it returns False. The caller can
# check the returned value and process it accordingly

def list2int(lst):
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except ValueError:
            return False
    return True

# Predicate function to check if a list of numbers is strictly increasing
# Parameters: list lst, nonempty 
# Return: True if list strictly increasing and False otherwise

def isIncreasing(lst):
    num = lst[0]
    for i in lst:
        if i + 1 < num: #If the next number is less then the previous, return false
            return False     
    return True #Return True if next number is greater then the previous

# Predicate function to check if  list elements are within specified interval
# Parameters: list lst,  and numbers l and h , l<=h 
# Return: True if all elements are between l and h, included and false otherwise

def isInInterval(lst, l, h):
    listRange = list(range(l, h +1))
    for i in lst:
      if i not in listRange:
        return False
    return True

# Function to read a grade scale from keyboard
# Parameters: none
# Return: list scale, of length 4 of strictly increasing order, all values are
#          between 0 and 100

def getScale():
    print("Enter dividers for grade scale:\n"
          "    Four numbers between 0 and 100 in strictly increasing order.\n"
          "    When prompt, enter the numbers in order separated by space.\n")
    scale = []
    
    # read the input and store in string scale
    scaleInput = input("Enter Numbers: ")
    scale = scaleInput.split()
    
    #Check to see if input can be converted to int, if input is between scale 0-100, if the length of input converted to list is = to 4, and input has increasing numbers
    while list2int(scale) == False or isInInterval(scale, 0, 100) == False or len(scale) != 4 or isIncreasing(scale) == False:
        scaleInput = input("Invalid Scale\nEnter Numbers: ")
        scale = scaleInput.split()    
    return scale #Returns scale

# Predicate function to test if a number is in an interval [l, h]
# Parameters: number to test and interval limita l and  h
# Return: True if l<=number<=h and False otherwise

def inInterval(number, l, h):
    # write the code, make sure you do not return always True, take care of the below return
    rangeList = list(range(l, h + 1))
    if number in rangeList: #If the number is in the range between l and h return true
      return True
    return False #Return false if number is not in range

# Function to input student IDs and test scores 
# Parameters: none
# Return: dictionary grades{} with records id:score

def getData():
    print("Enter on one line, student ID and test score, separated by space.\n"
          "Continue this way with all students.\n"
          "When done just hit enter.\n"
          "Valid IDs are integers between 100 and 999 (included).\n"
          "Valid scores are between 0 and 100 (included).\n"
          "If you entered invalid ID or score per student you must re-enter"
          "correct values.\n")
          
    grades = {}
    entryline = input("Enter ID and score separated by space, or hit enter to quit: ")
                 
    while  entryline != '':
        temp = entryline.split() #turns the string into a list

        try: #check to see if the list can be turned into numbers
            val1 = int(temp[0])
            val2 = int(temp[1])
    
            if (val1 > 99) and (val1 < 1000) and (val2 > -1) and (val2 < 101):
                grades[temp[0]] = val2
            else:
                print("Enter a 3 digit ID and a 2 digit Score")
        except : #if list cannot be turned into numbers then user input was incorrect
            print("Enter a 3 digit ID and a 2 digit Score") #Tells the user to correct their input

        entryline = input("Enter ID and Score: ")
        
    return grades #returns the completed dictionary with the student's ID as the key and their score as the value
    

def main():
    scale = getScale()
    print(scale)
    grades = getData()
    print(grades)
    return
main()
