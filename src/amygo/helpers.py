import random


def generate_exercise(settings):
    operations = []
    if settings.subtraction_enabled:
        operations.append(generate_subtraction)
    if settings.multiplication_enabled:
        operations.append(generate_multiplication)
    if settings.division_enabled:
        operations.append(generate_division)
    if settings.addition_enabled or len(operations) == 0:
        operations.append(generate_addition)

    return random.choice(operations)(settings)


def generate_addition(settings):
    _, left = generate_number(settings.addition_minimum, settings.addition_maximum)
    _, right = generate_number(settings.addition_minimum, settings.addition_maximum)
    return f"{left} + {right}"


def generate_subtraction(settings):
    left_val, left = generate_number(settings.subtraction_minimum, settings.subtraction_maximum)
    if settings.subtraction_allow_negative:
        _, right = generate_number(settings.subtraction_minimum, settings.subtraction_maximum)
    else:
        _, right = generate_number(settings.subtraction_minimum, left_val)
    return f"{left} - {right}"


def generate_multiplication(settings):
    _, left = generate_number(settings.multiplication_minimum, settings.multiplication_maximum)
    _, right = generate_number(settings.multiplication_minimum, settings.multiplication_maximum)
    return f"{left} x {right}"


def generate_division(settings):
    right_val, right = generate_number(settings.division_divisor_minimum, settings.division_divisor_maximum, False)
    if settings.division_force_int:
        border_min = int(settings.division_dividend_minimum / right_val)
        border_max = int(settings.division_dividend_maximum / right_val)
        if border_min > border_max:
            swp = border_min
            border_min = border_max
            border_max = swp
        val = random.randint(border_min, border_max)
        _, left = pretty_str(val*right_val)
    else:
        _, left = generate_number(settings.division_dividend_minimum, settings.division_dividend_maximum)
    return f"{left} ÷ {right}"


def generate_number(minimum, maximum, allow_zero=True):
    val = random.randint(minimum, maximum)
    if val == 0 and not allow_zero:
        val = 1
    return pretty_str(val)


def pretty_str(number):
    if number < 0:
        return number, f"({number})"
    else:
        return number, str(number)
