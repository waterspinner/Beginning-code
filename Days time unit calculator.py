# var

# calculate hours

def calculate_hours(num_of_days):
    return num_of_days * 24

# calculate minutes


def calculate_minutes(num_of_days):

    return num_of_days * 24 * 60


# calculate seconds
def calculate_seconds(num_of_days):

    return num_of_days * 24 * 60 * 60

# validate input


def validate_days_input():
    if days_input.isdigit():
        days_input_number = int(days_input)
        return days_input_number
    else:
        print('Input is invalid, must be a number')
        return 0

# validate input


def validate_times_and_execute():
    if time_unit_input == 'hours' or 'minutes' or 'seconds':
        num_of_days = validate_days_input()
        user_input = days_to_units(num_of_days, time_unit_input)

        print(user_input)
    else:
        print('Input is invalid please try again')


# calculate units of time for certain days
def days_to_units(num_of_days, time_unit):

    if time_unit == 'hours':
        return f'{num_of_days} days is {calculate_hours(num_of_days)} {time_unit}'

    elif time_unit == 'minutes':
        return f'{num_of_days} days is {calculate_minutes(num_of_days)} {time_unit}'

    elif time_unit == 'seconds':
        return f'{num_of_days} days is {calculate_seconds(num_of_days)} {time_unit}'

    elif time_unit != int:
        return 'you must enter a number not a letter or word'

    else:
        return 'input is invalid try again please'


days_input = input('Please tell me the number of days to calculate\n')

validate_days_input()

time_unit_input = input("and what unit of time do you want to know?\n")

validate_times_and_execute()
