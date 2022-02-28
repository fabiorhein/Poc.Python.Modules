def days_to_units(num_of_days, name_of_unit):
    if name_of_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_unit}"
    elif name_of_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {name_of_unit}"
    else:
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} {name_of_unit}"


def validade_and_execute(dictionary):
    try:
        user_input_number = int(dictionary["days"])

        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a Zero, please enter a valid positive value")
        else:
            print("You entered a negative number, no convertion for you")
    except ValueError:
        print("your input is not number. Don't ruin my program!")


def create_days_dictionary(value_input):
    days_and_unit = value_input.split(":")
    days_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    return days_dictionary


user_input_message = "Hey User, enter number of days and conversion unit!\n"