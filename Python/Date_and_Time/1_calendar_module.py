import calendar

def main():
    """
    Accept a date in the form of MM DD YYYY and determine the weekday for the given date.
    """

    date = input('\nEnter the space-separated date in the form MM DD YYYY: ').split()

    month = int(date[0])
    day = int(date[1])
    year = int(date[2])

    weekday_idx = calendar.weekday(year, month, day)
    weekday_name = (calendar.day_name[weekday_idx]).upper()

    print(f'\nThe Weekday on {month}-{day}-{year} is {weekday_name}\n')

if __name__ == '__main__':
    main()