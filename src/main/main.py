import statistics
import functools

SETTINGS = ['LCM', 'HCF', 'ADD', 'MULTIPLY', 'DIVIDE', 'SUBTRACT', 'MEAN', 'MEDIAN', 'Q1', 'Q2', 'Q3', 'Q4',
            'UPPER_Q_RANGE', 'LOWER_Q_RANGE']


def get_numbers():
    result_numbers = []
    while True:
        user_input = input("Enter a number or type 'DONE' to finish: ").upper()
        if user_input == 'DONE' and len(result_numbers) >= 2:
            break
        elif user_input == 'DONE':
            print("Please enter at least two numbers before typing 'DONE'.")
        else:
            try:
                result_numbers.append(float(user_input))
            except ValueError:
                print("That is not a number. Please try again!")
    return result_numbers


def get_setting_type():
    while True:
        chosen_setting = input(f"What would you like to run? ({', '.join(SETTINGS)}): ").upper()
        if chosen_setting in SETTINGS:
            return chosen_setting


def calculate_lcm(input_numbers):
    start_value = max(input_numbers)
    while True:
        if all(start_value % num == 0 for num in input_numbers):
            return start_value
        start_value += 1


def calculate_hcf(input_numbers):
    start_value = min(input_numbers)
    for i in range(start_value, 0, -1):
        if all(num % i == 0 for num in input_numbers):
            return i


def calculate_add(input_numbers):
    return sum(input_numbers)


def calculate_multiply(input_numbers):
    return functools.reduce(lambda x, y: x * y, input_numbers, 1)


def calculate_divide(input_numbers):
    result_divide = input_numbers[0]
    for num in input_numbers[1:]:
        if num != 0:
            result_divide /= num
        else:
            print("Cannot divide by zero. Please try again!")
            return None
    return result_divide


def calculate_subtract(input_numbers):
    return functools.reduce(lambda x, y: x - y, input_numbers[1:], input_numbers[0])


def calculate_mean(input_numbers):
    return statistics.mean(input_numbers)


def calculate_median(input_numbers):
    return statistics.median(input_numbers)


def calculate_quantile(input_numbers, n):
    return statistics.quantiles(input_numbers, n=4)[n]


def calculate_max(input_numbers):
    return max(input_numbers)


def calculate_upper_q_range(input_numbers):
    quantiles = statistics.quantiles(input_numbers, n=4)
    return quantiles[2] - quantiles[0]


def calculate_lower_q_range(input_numbers):
    return statistics.quantiles(input_numbers, n=4)[0]


OPERATIONS = {
    'LCM': calculate_lcm,
    'HCF': calculate_hcf,
    'ADD': calculate_add,
    'MULTIPLY': calculate_multiply,
    'DIVIDE': calculate_divide,
    'SUBTRACT': calculate_subtract,
    'MEAN': calculate_mean,
    'MEDIAN': calculate_median,
    'Q1': lambda x: calculate_quantile(x, 0),
    'Q2': calculate_median,
    'Q3': lambda x: calculate_quantile(x, 2),
    'Q4': calculate_max,
    'UPPER_Q_RANGE': calculate_upper_q_range,
    'LOWER_Q_RANGE': calculate_lower_q_range
}

while True:
    numbers = get_numbers()
    chosen_setting = get_setting_type()

    calculation_function = OPERATIONS[chosen_setting]
    result = calculation_function(numbers)

    if result is not None:
        print(f"Result of {chosen_setting}: {result}")