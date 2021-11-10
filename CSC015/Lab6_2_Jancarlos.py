#Jancarlos Rodriguez
#Lab6 Q2
#Lab6_2_Jancarlos.py
#The program prints a table of the integer powers of 10 from -5 to 5
#20211103

# -----------------------------------------------------------------
# Function intpower(x, k)
# Parameters: x = real number, k = int
# Return: x to the power of k
def intpower(x, k): 
    value = x
    if k > 0: #if k is greater than 0 then multiply x by itself for k amount of times
        for i in range(int(k - 1)):
            value *= x
            i += 1

    elif k == 0: #any number to the power of 0 is 1
        value = 1
    else: #if k is less than 0, divide 1 by x and multiply the value by itself for k amount of times
        x = 1 / x
        for i in range(abs(k - 1)):
            value *= x
            i += 1
    return value #returns the value of x to the k power

# main() ----------------------------------------------------------
# Driver for testing the functions
def main():

    print(" k      10^k")
    print("---  -----------")
    for i in range(-5,6):
        print(f"{i}   {intpower(10, i)}")
        i += 1

main() #call to main()
