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
            return print("User Canceled")
        else:
            num = int(num)

        if num < 0 or num > 100 or num <= prev_num:
            print("Enter a integer between 0 and 100 and greater than the previous number")
        else:
            scale.append(num)
            prev_num = num

    return scale

def getData():
    data = input("Enter ID and Score: ")
    scores = {}

    while data != "":
        temp = data.split()
    
        if (int(temp[0]) > 99) and (int(temp[0]) < 1000) and (int(temp[1]) > -1) and (int(temp[1]) < 101):
            scores[temp[0]] = int(temp[1])
        else:
            print("Enter a 3 digit ID and a 2 digit Score")

        data = input("Enter ID and Score: ")
        
    return scores


def getGrade(scale, a_score):
    grades = {}




def main():
    print(getScale())
    print(getData())

main()