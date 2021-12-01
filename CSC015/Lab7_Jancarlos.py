#Jancarlos Rodriguez
#Lab7 
#Lab7_Jancarlos.py
#Implementing 3 functions and using one main() driver
#20211201

#Function acronym()- Given users input, an acronym is formed form the first letters of all words in the unput that start with a capital letter.
#Parameters: N/A
#Input: A User string 
#Returns: A string with the acronym of the user's input
def acronym():
    user_phrase = input("Enter Phrase: ")
    phrase = user_phrase.split()

    phrase_acronym = []

    #For every item in the list, check if their first letter is capitalized.
    for i in range(len(phrase)):
        if phrase[i][0].isupper():
            #If the first letter of the item is capitalized, add it to the phrase_acronym list 
            phrase_acronym += phrase[i][0]
    #Joins all the items in phrase_acronym list and assigns it to complete_acronym
    complete_acronym = "".join(phrase_acronym)

    return complete_acronym #Acronym is returned

#Function processList() takes in a list of numbers and returns a sorted list with all non-negative distinct values
#Parameters: lst  = a list of numbers
#Input: N/A
#Returns: a new list newlist consisting of all non‐negative distinct values in lst sorted in ascending order
def processList(lst):
    newlist = []
    
    #Checks every number in lst is non-negative and not in newlist already
    for number in lst:
        if (number >= 0) and (number not in newlist):
            #Adds the number to newlist
            newlist.append(number)
    #Sorts the list from smallest number to largest
    newlist.sort()        
   
    return newlist #returns list

#Function wordCount() takes as a parameter a list of words called tokens and builds and returns a dictionary with records word:count
#Parameters: list of words
#Input: N/A
#Return: Dictionary with records of word:count
def wordCount(tokens):
    record = {}

    #For every word in tokens
    for word in tokens:
        #If the word is not in the dictionary record, add it to the dictionary
        if word not in record:
            record[str(word)] = 1
        else: #Word is in the dictionary, so add 1
            record[str(word)] += 1
    
    return record #Returns dictionary

#Function main() is the driver for the program
def main():

    #Question 1:
    print(acronym())

    #Question 2:
    list_numbers = [10, -7, 4, 39, -6, 12, 2]
    print(processList(list_numbers))

    #Question 3 & 4
    wordcount_text = input("Type Words: ")
    wordcount_list = wordcount_text.split()

    #Saves the returned dictionary in the variable word_count
    word_count = wordCount(wordcount_list)

    #Prints the Key and Count of every value in the dictionary
    print([(k, word_count[k]) for k in word_count])

main() #Call to main
