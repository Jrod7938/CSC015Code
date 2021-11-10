#Jancarlos Rodriguez
#Lab6 Q1
#Lab6_1_Jancarlos.py
#Program gives information, formula, and value of the Golden Ratio
#20211103

# -----------------------------------------------------------------
# Function goldenRatioInfo()
# Parameters: n/a
# Return: n/a
def goldenRatioInfo(): # prints the message about the constant 
    goldenRatioComment = "The 'golden ratio' is a unique mathematical relationship. Two numbers are in the\ngolden ratio if the ratio of the sum of the numbers (a b) divided by the larger number\n(a) is equal to the ratio of the larger number divided by the smaller number (a/b)."
    print(goldenRatioComment)

# -----------------------------------------------------------------
# Function goldenRatioFormula()
# Parameters: n/a
# Return: n/a
def goldenRatioFormula(): #prints the formula
    formula = "(1 + (5 ** 0.5)) / 2"
    print(formula)

# -----------------------------------------------------------------
# Function goldenRatio()
# Parameters: n/a
# Return: n/a
def goldenRatio(): #computes and returns the value of the constant 
    GOLDEN = (1 + (5 ** 0.5)) / 2
    return GOLDEN

# main() ----------------------------------------------------------
# Driver for testing the functions
def main(): #puts together the program
    goldenRatioInfo() # prints the message about the constant 
    goldenRatioFormula() #prints the formula
    print(f"Value of the Golden Ratio Constant: {goldenRatio()}") #prints the value of the golden ratio

main() #Call to Main()