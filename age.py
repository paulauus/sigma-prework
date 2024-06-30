# This program calculates the age between the current date and the given date.

from datetime import datetime

def calculate_years_passed():
    # Ask the user to enter a date
    user_date_input = input("Enter a date (YYYY-MM-DD): ")

    try:
        # Convert the input string to a datetime object
        user_date = datetime.strptime(user_date_input, "%Y-%m-%d")
        
        # Get today's date
        today_date = datetime.today()
        
        # Calculate the number of years since the entered date
        # A tuple comparison can be used in a calculation (True = 1, False = 0)
        years = today_date.year - user_date.year - ((today_date.month, today_date.day) < (user_date.month, user_date.day))
        
        # Print the answer
        print(f"It has been {years} years since the entered date.")

    # Error handling if entered date is not in correct format
    except ValueError:
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")

    return

calculate_years_passed()