import re
import utils.variables as VARS
from datetime import datetime


def iso_time_to_hms(iso_time: str) -> str:
    """
    Convierte un tiempo ISO 8601 a formato HH:MM:SS.

    Args:
        iso_time (str): Tiempo en formato ISO 8601 (PTnHnMnS).

    Returns:
        str: Tiempo en formato HH:MM:SS.
    """
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', iso_time)
    if not match:
        return "00:00:00"

    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def hms_time_to_seconds(hms_time: str) -> int:
    """
    Convierte un tiempo en formato HH:MM:SS a segundos.

    Args:
        hms_time (str): Tiempo en formato HH:MM:SS.

    Returns:
        int: Tiempo en segundos.
    """
    seconds: int = 0
    response: str = hms_time

    if isinstance(hms_time, str):
        array_time = reversed(hms_time.split(":"))

        for i, t in enumerate(array_time):
            seconds += int(t)*(60**int(i))

    return seconds


def iso_time_to_seconds(iso_time: str) -> int:
    """
    Convierte un tiempo ISO 8601 directamente a segundos.

    Args:
        iso_time (str): Tiempo en formato ISO 8601 (PTnHnMnS).

    Returns:
        int: Tiempo en segundos.
    """
    return hms_time_to_seconds(iso_time_to_hms(iso_time))


def datetime_to_seconds(timestamp: datetime) -> int:
    """
    Convierte un timestamp en formato ISO 8601 a segundos desde la época (epoch).

    Args:
        timestamp (str): Timestamp en formato ISO 8601 (YYYY-MM-DDTHH:MM:SSZ).

    Returns:
        int: Tiempo en segundos desde la época.
    """
    if isinstance(timestamp, str):
        dt: datetime = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")

    return int(dt.timestamp())


def seconds_to_hms_time(seconds: int) -> str:
    """
    Convierte un tiempo en segundos a formato HH:MM:SS.

    Args:
        seconds (int): Tiempo en segundos.

    Returns:
        str: Tiempo en formato HH:MM:SS.
    """
    hh: int = seconds // 3600
    mm: int = (seconds % 3600) // 60
    ss: int = seconds % 60
    return f"{hh:02}:{mm:02}:{ss:02}"
