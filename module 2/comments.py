if __name__ == "__main__":

    # Prompt user for their hours; need to convert from str to int
    number_of_hours = input("Please Enter the Number of Hours that you Worked:")
    number_of_hours = int(number_of_hours)

    #Assuming there are 24 hours in a day
    percentage_of_day = number_of_hours / 24 * 100

    print(f"The number of hours you wroked is {percentage_of_day}%")

    # Wage Calculator
    
    # prompt user for their hourly rate

    #promt user of number of hours they worked 
    
    # calculate wage based on rate * hours