# Task A
def my_func(x1, x2, x3):
    if x1 + x2 + x3 == 0:
        return "Not a number – denominator equals zero"
    if type(x1) and type(x1) and type(x1) == float:
        return float(((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3))
    else:
        return 'Error: parameters should be double'


# Task B
def convert(hours, minutes):
    if hours < 0 or minutes < 0:
        return 'input error!'
    return hours * 3600 + minutes * 60
