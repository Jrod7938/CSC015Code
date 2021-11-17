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
       # write  the code to process a line entered
       # if a valid record entered, store the record in the dictionary grades.
       # else print Invalid entry.
    
       entryline = input("Enter ID and score separated by space, or hit enter to quit: ")
        
    return grades
    

def main():
    scale = getScale()
    print(scale)
    grades = getData()
    return
main()

======================================================================================
If done implement functions to be used n Hangman game

getGuess(guessed )
       Ask the user to enter a letter form the keyboard 
       Do input validation
       Parameter: guessed is a string of used  letters,
       Returns: a lower case letter
----------------------------------

updateHiddenWord(word, hidden, letter)
Purpose: Update hidden string.
    Given a secret word word, a hidden string (of dashes and leter possibly letters), and
    a letter, replace - with the letter at the places where the letter matches word.

Parameters:                                          
   Word is the secret word
   Hidden is the hidden word
   Letter is the guessed letter
Return: the updated hidden word
----------------------------------

printScore(word, hidden)
   print Winner or Loosed based on hidden content
   if there are dashes in hiddent --> Losser, otherwise Winner
   If looser print the secret word
  

Hangman game

Set
   Secret word
   Max number guesses
   Hidden word, all letters in the secret word are dashed
   guessed       is a string of letters already used
   count           is a counter of number guesses used
Repeatedly  (as long as guesses left or hidden word not revealed)
   ask user to guess a new letter
   Do input validation to read a letter
   Update the hidden word, replace dashes with letter (if guessed)
   Update guessed string and update count
   Print the score