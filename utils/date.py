from datetime import datetime


def date_to_epoch(date_value: datetime) -> int:
    return int((date_value - datetime(1970, 1, 1)).total_seconds())
