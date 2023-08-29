# The function takes a date in a format "dd.mm.yyyy" , the number of days to add 
# and calculates the new date
def CalculateDate(current_date, days_to_add):

    if(days_to_add < 0):
        print("Error: Number of days to add is negative!")
        return

    days_in_month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                          9: 30, 10: 31, 11: 30, 12: 31}

    current_day, current_month, current_year = map(int, current_date.split('.'))

    # Check if current year is a leap year
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        days_in_month_dict[2] = 29

    days_to_add += (current_day - 1)
    current_day = 1

    while (days_to_add > 0):
        if (days_to_add >= days_in_month_dict[current_month]):
            days_to_add -= days_in_month_dict[current_month]
            current_month += 1
            if (current_month > 12):
                current_month = 1
                current_year += 1
                # Check if current year is a leap year
                if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
                    days_in_month_dict[2] = 29
                else:
                    days_in_month_dict[2] = 28
        else:   # Remained days to add is smaller than days in current month
            current_day += days_to_add
            days_to_add = 0

    print(current_day, current_month, current_year)
