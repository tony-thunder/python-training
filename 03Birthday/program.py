import datetime

def print_header():
    print('------------------------------')
    print('          BIRTHDAY APP')
    print('------------------------------')
    print()


def get_birthday_from_user():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Year [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(ytarget_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days



def print_birhday_information(days):
    if


    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print(number_of_days)


main()