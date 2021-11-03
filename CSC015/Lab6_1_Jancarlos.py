#Jancarlos Rodriguez
#Lab6 Q1
#Lab6_1_Jancarlos.py
#Program gives information, formula, and value of the Golden Ratio
#20211103

def goldenRatioInfo(): # prints the message about the constant 
    goldenRatioComment = "The 'golden ratio' is a unique mathematical relationship. Two numbers are in the golden ratio if the ratio of the sum of the numbers (a b) divided by the larger number (a) is equal to the ratio of the larger number divided by the smaller number (a/b)."
    print(goldenRatioComment)

def goldenRatioFormula(): #prints the formula
    formula = "(1 + (5 ** 0.5)) / 2"
    print(formula)
def goldenRatio(): #computes and returns the value of the constant 
    golden = (1 + (5 ** 0.5)) / 2
    return golden

def main(): #puts together the program
    goldenRatioInfo()
    goldenRatioFormula()
    print(f"Value of the Golden Ratio Constant: {goldenRatio()}")

main() #Call to Main()