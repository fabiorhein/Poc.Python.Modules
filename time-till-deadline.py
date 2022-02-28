import datetime


def convert_date_to_days(date):
    days = datetime.datetime.date(date)
    return days


def formated_date(date_array):
    day = int(date_array[0])
    month = int(date_array[1])
    year = int(date_array[2])
    return datetime.date(year, month, day)


def date_diff(date_deadline):
    date_today = datetime.datetime.today()
    return abs((date_deadline - date_today).days)


def date_array(goal_and_date):
    return goal_and_date[1].split(".")


user_input_value = input("Enter your goal with a deadline separeted by colon\n")
goal_and_date = user_input_value.split(":")

# date = date_array(goal_and_date)
# date_to_datetime = formated_date(date)
date_to_datetime = datetime.datetime.strptime(goal_and_date[1], "%d.%m.%Y")
diff = date_diff(date_to_datetime)

print(f"Dear user! Time remaining dor yout goal: {goal_and_date[0]} is {diff} days")
