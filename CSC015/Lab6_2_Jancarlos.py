#Jancarlos Rodriguez
#Lab6 Q2
#Lab6_2_Jancarlos.py
#The program prints a table of the integer powers of 10 from -5 to 5
#20211103

def intpower(x, k):
    value = x
    if k > 0:
        for i in range(int(k - 1)):
            value *= x
            i += 1

    elif k == 0:
        value = 1
    else:
        x = 1 / x
        for i in range(abs(k - 1)):
            value *= x
            i += 1
    return value

def main():

    print(" k      10^k")
    print("---  -----------")
    for i in range(-5,6):
        print(f"{i}   {intpower(10, i)}")
        i += 1

main()
