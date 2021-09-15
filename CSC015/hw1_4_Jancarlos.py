#Jancarlos Rodriguez
#Homework 1
#hw1_4_Jancarlos.py
#Purpose: Reads the total rainfall for a 30 day period and gives you the average amount of daily rain.
#20210915
def art():
    #Art because its cool :,)
    print("               __   _")
    print("             _(  )_( )_")
    print("            (_   _    _)")
    print("           / /(_) (__)")
    print("          / / / / / /")
    print("         / / / / / /")

def main():
    
    #Constant number of days in the month
    number_days = 30

    #Prints art
    art()
    
    #Asks user to input how much rain in total fell during the month 
    monthly_rain_in = float(input("\nHow much rain fell in 30 days?: "))

    #Saves the average amount of rain that fell daily
    daily_avg_rain_in = monthly_rain_in / number_days

    #Prints the amount of monthly rain and daily rain
    print(f"Monthly rain: {monthly_rain_in:.2f}in\nAverage Daily Rain: {daily_avg_rain_in:.2f}in")

    #Pritns Art
    art()

main()