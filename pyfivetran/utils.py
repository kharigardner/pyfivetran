from __future__ import annotations # for | union syntax

from logging import getLogger
from dateutil.parser import isoparse
import datetime as dt
import sys


logger = getLogger(__name__)


def deserialize_timestamp(dt_str: str) -> dt.datetime:
    """
    Deserialize a timestamp in the format: 2019-08-24T14:15:22Z

    :param dt_str: The timestamp to deserialize
    :return: The deserialized timestamp
    """
    if sys.version_info.minor < 11:
        return isoparse(dt_str)
    return dt.datetime.fromisoformat(dt_str)


def serialize_timezone(tz: str | dt.tzinfo) -> int:
    """
    Serialize a timezone to the offset integer representation.

    Fivetran expects: 11, 10 ... ,0 , ... +11, +12

    :param tz: The timezone to serialize
    :return: The offset integer representation
    """
    if isinstance(tz, str):
        try:
            tz_return = int(tz)
        except ValueError as e:
            logger.warning(f"Invalid timezone: {tz}")
            raise ValueError(
                f"Invalid timezone: {tz}... unable to serialize string format"
            ) from e

    elif isinstance(tz, dt.tzinfo):
        tz_return = int(tz.utcoffset(None).seconds / 3600)  # type: ignore

    return tz_return
