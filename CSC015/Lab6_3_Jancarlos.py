#Jancarlos Rodriguez
#Lab6 Q3
#Lab6_3_Jancarlos.py
#The program computes the students letter grades by reading a grade scale, student id, and student scores.
#20211106

# -----------------------------------------------------------------
# Function getScale()
# Parameters: n/a
# Return: a list of ints between 0 and 100 in increasing order
def getScale():
    prev_num = 0
    scale = []

    while len(scale) != 4: #While loop to keep asking the user to input a number until the length of scale[] is 4
        num = input("Enter a integer between 0 and 100: ")

        if num == "": #checks to see if the user entered the empty string
            print("User Canceled")
            quit() #cancels program
        try: #tries to append the input to the scale if the input is >= 0, and <= 100, and > prev_num
            num = int(num)
            if num >= 0 and num <= 100 and num > prev_num:
                scale.append(num)
                prev_num = num
            else: #User input was incorrect
                print("Enter a integer between 0 and 100 and greater than the previous number")
        except ValueError: #User input was incorrect
            print("Enter a integer between 0 and 100 and greater than the previous number")

    return scale #list of ints between 0 and 100 in increasing order

# -----------------------------------------------------------------
# Function getData()
# Parameters: n/a
# Return: a dictionary with  the student's ID as the key and their score as the value
def getData():
    data = input("Enter ID and Score: ")
    scores = {}

    while data != "": #While loop runs if the user does not input an empty string
        temp = data.split() #turns the string into a list

        try: #check to see if the list can be turned into numbers
            val1 = int(temp[0])
            val2 = int(temp[1])
    
            if (val1 > 99) and (val1 < 1000) and (val2 > -1) and (val2 < 101):
                scores[temp[0]] = val2
            else:
                print("Enter a 3 digit ID and a 2 digit Score")
        except : #if list cannot be turned into numbers then user input was incorrect
            print("Enter a 3 digit ID and a 2 digit Score") #Tells the user to correct their input

        data = input("Enter ID and Score: ")
        
    return scores #returns the completed dictionaryh with the student's ID as the key and their score as the value

# -----------------------------------------------------------------
# Function setGrade(scale, a_score)
# Parameters: grade scale[], and student's score
# Return: the students computed letter grade
def setGrade(scale, a_score):
    #Control statement to give the correct letter grade for the student's score
    if a_score > scale[3]: 
        letter_grade = "A"
    elif a_score <= scale[3] and a_score > scale[2]:
        letter_grade = "B"
    elif a_score <= scale[2] and a_score > scale[1]:
        letter_grade = "C"
    elif a_score <= scale[1] and a_score > scale[0]:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

# -----------------------------------------------------------------
# Function average(scores)
# Parameters: the dictionary scores{}
# Return: average of all the scores
def average(scores):
    return sum(scores.values()) / len(scores) #formula to compute the average of all the scores

# -----------------------------------------------------------------
# Function printScale(scale)
# Parameters: the grade scale[]
# Return: n/a
def printScale(scale): #Prints the grade scale for the user to see
    print(f"A       score > {scale[3]}")
    print(f"B {scale[3] - 1} >= score > {scale[2]}")
    print(f"C {scale[2] - 1} >= score > {scale[1]}")
    print(f"D {scale[1] - 1} >= score > {scale[0]}")
    print(f"F {scale[0] - 1} >= score")

# -----------------------------------------------------------------
# Function printGrades(grades)
# Parameters: the grade scale[]
# Return: n/a
def printGrades(grades):
    print("   ID    |   Grade   ")
    for values in grades: #prints the students ID with their letter grade
        print(f"   {values}   |   {grades[values]} ")

# main() ----------------------------------------------------------
# Driver for testing the functions
def main():
    scale = getScale() #saves the list that is returned by getScale()

    scores = getData() #saves the scores that is returned by getData()

    grades = dict.fromkeys(scores) #creates a new list with the same keys as scores{}
    
    for values in scores: #assigns the letter grade to the student's ID in the dictionary grades{}
        grades[values] = setGrade(scale, scores[values])

    print(f"The Average Score is {average(scores)}") #prints the average grade of all the students

    printScale(scale) #prints the scale for the user to see
    printGrades(grades) #prints all the student's IDs and Grades


main() #Call to main()