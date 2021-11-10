#Jancarlos Rodriguez
#Lab6 Q3
#Lab6_3_Jancarlos.py
#The program computes the students letter grades by reading a grade scale, student id, and student scores.
#20211106


def getScale():
    prev_num = 0
    scale = []

    while len(scale) != 4:
        num = input("Enter a integer between 0 and 100: ")

        if num == "":
            print("User Canceled")
            quit()
        try:
            num = int(num)
            if num >= 0 and num <= 100 and num > prev_num:
                scale.append(num)
                prev_num = num
            else:
                print("Enter a integer between 0 and 100 and greater than the previous number")
        except ValueError:
            print("Enter a integer between 0 and 100 and greater than the previous number")

    return scale

def getData():
    data = input("Enter ID and Score: ")
    scores = {}

    while data != "":
        temp = data.split()

        try:
            val1 = int(temp[0])
            val2 = int(temp[1])
    
            if (val1 > 99) and (val1 < 1000) and (val2 > -1) and (val2 < 101):
                scores[temp[0]] = val2
            else:
                print("Enter a 3 digit ID and a 2 digit Score")
        except :
            print("Enter a 3 digit ID and a 2 digit Score")

        data = input("Enter ID and Score: ")
        
    return scores


def setGrade(scale, a_score):
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

def average(scores):
    return sum(scores.values()) / len(scores)

def printScale(scale):
    print(f"A       score > {scale[3]}")
    print(f"B {scale[3] - 1} >= score > {scale[2]}")
    print(f"C {scale[2] - 1} >= score > {scale[1]}")
    print(f"D {scale[1] - 1} >= score > {scale[0]}")
    print(f"F {scale[0] - 1} >= score")

def printGrades(grades):
    print("   ID    |   Grade   ")
    for values in grades:
        print(f"   {values}   |   {grades[values]} ")

def main():
    scale = getScale()

    scores = getData()

    grades = dict.fromkeys(scores)

    for values in scores:
        grades[values] = setGrade(scale, scores[values])

    print(f"The Average Score is {average(scores)}")

    printScale(scale)
    printGrades(grades)




main()