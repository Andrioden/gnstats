from datetime import date


def date_to_epoch(date_value: date) -> int:
    return int((date_value - date(1970, 1, 1)).total_seconds())
