#Jancarlos Rodriguez
#Lab6 Q2
#Lab6_2_Jancarlos.py
#The program prints a table of the integer powers of 10 from 10􏰍􏰎 𝑡𝑜 10􏰎
#20211103

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
    #Fix
    return -1




def main():
    scale = getScale()
    print(scale)

    data = getData()
    print(data)

    grades = {}
    for values in range(len(data)):
        grades[data[values]] = setGrade(scale[values], data[values])

    print(grades)




main()