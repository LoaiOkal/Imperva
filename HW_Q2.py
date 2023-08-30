# The function takes a date in a format "dd.mm.yyyy" , the number of days to add
# and calculates the new date
def CalculateDate(current_date, days_to_add):

    # Invalid input
    if(days_to_add < 0):
        print("Error: Number of days to add is negative!")
        return

    # days_in_month_dict is a dictionary which maps each month to the number of days it has
    days_in_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                          9: 30, 10: 31, 11: 30, 12: 31}

    # Date parsing
    current_day, current_month, current_year = map(int, current_date.split('.'))

    # Checks if the current year is a leap year, if yes update the number of days for month 2 (February)
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        days_in_month_dict[2] = 29

    # Adds the current day to the number of days to add, and sets the current day = 1
    # to simplify the calculation
    days_to_add += (current_day - 1)
    current_day = 1

    # While we still have days to add, update the current date
    while (days_to_add > 0):
        # If the number of remained days to add is equal or bigger than the days in the current month,
        # increase the month by 1 and decrease the remained number of days to add
        if (days_to_add >= days_in_month_dict[current_month]):
            days_to_add -= days_in_month_dict[current_month]
            current_month += 1
            # Update current_year if needed
            if (current_month > 12):
                current_month = 1
                current_year += 1
                # Check if current year is a leap year, if yes update the number of days for month 2 (February)
                if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
                    days_in_month_dict[2] = 29
                else:
                    days_in_month_dict[2] = 28
        else:   # Remained days to add is smaller than days in current month
            current_day += days_to_add
            days_to_add = 0

    # Merge the current_day, current_month and current_year to print the new date
    new_date_list = [str(current_day), str(current_month), str(current_year)]
    new_date = ".".join(new_date_list)
    print(new_date)

if __name__ == '__main__':
    print(" Input: '10.01.2008', 10 \n Output: ")
    CalculateDate("10.01.2008", 10)
    print("\n Input: '29.06.2020', 8 \n Output: ")
    CalculateDate("29.06.2020", 8)

