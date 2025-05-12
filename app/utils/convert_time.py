import pytz
from datetime import datetime

def moscow_to_timestamp(date: str) -> int:
    date_format = '%d.%m.%Y %H:%M:%S'
    moscow_tz = pytz.timezone('Europe/Moscow')
    naive_datetime = datetime.strptime(date, date_format)
    localized_datetime = moscow_tz.localize(naive_datetime)
    timestamp = int(localized_datetime.timestamp())

    return timestamp