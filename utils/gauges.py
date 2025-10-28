def gauge_drawer(value, max_value) -> str:
    result = "[" + "*" * int(round(value, -1)/10) + "-" * int(round((max_value - value), -1) / 10) + "]"
    return result