import math


def linear_interpolate(start, end, current_value, final_value):
    percentage_time_elapsed = current_value / final_value
    interpolated_value = ((1 - percentage_time_elapsed) * start) + (percentage_time_elapsed * end)
    return interpolated_value


def quadratic_interpolate(start, end, middle, current_value, final_value):
    p1 = linear_interpolate(start, middle, current_value, final_value)
    p2 = linear_interpolate(middle, end, current_value, final_value)
    interpolated_value = linear_interpolate(p1, p2, current_value, final_value)
    return interpolated_value


def cubic_interpolate(start, end, middle1, middle2, current_value, final_value):
    p1 = quadratic_interpolate(start, middle2, middle1, current_value, final_value)
    p2 = quadratic_interpolate(middle1, end, middle2, current_value, final_value)
    interpolated_value = linear_interpolate(p1, p2, current_value, final_value)
    return interpolated_value


def ease(start, end, current_value, final_value):
    middle1 = math.sqrt(
        (0.25 ** 2) + (0.1 ** 2)
    )
    middle2 = math.sqrt(
        (0.25 ** 2) + 1
    )

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_value, final_value)
    return interpolated_value


def ease_in(start, end, current_time, total_time):
    middle1 = 0.42
    middle2 = math.sqrt(2)

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_time, total_time)
    return interpolated_value


def ease_out(start, end, current_time, total_time):
    middle1 = 0
    middle2 = math.sqrt(
        (0.58 ** 2) + 1
    )

    interpolated_value = cubic_interpolate(start, end, middle1, middle2, current_time, total_time)
    return interpolated_value
