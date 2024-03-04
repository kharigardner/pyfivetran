import pytest

import datetime
import pytz

from pyfivetran.utils import deserialize_timestamp, serialize_timezone

class TestDeserializeTimestamp:

    # Returns a datetime object when given a valid timestamp string in the format 'YYYY-MM-DDTHH:MM:SSZ'
    def test_valid_timestamp(self):
        timestamp = '2019-08-24T14:15:22Z'
        expected = datetime.datetime(2019, 8, 24, 14, 15, 22, tzinfo=pytz.UTC)
        assert deserialize_timestamp(timestamp) == expected

    # Returns a datetime object with the correct year, month, day, hour, minute, and second values
    def test_correct_values(self):
        timestamp = '2022-12-31T23:59:59Z'
        expected = datetime.datetime(2022, 12, 31, 23, 59, 59, tzinfo=pytz.UTC)
        assert deserialize_timestamp(timestamp) == expected

    # Handles timestamps with single-digit months, days, hours, minutes, and seconds
    def test_single_digit_values(self):
        timestamp = '2022-01-01T01:02:03Z'
        expected = datetime.datetime(2022, 1, 1, 1, 2, 3, tzinfo=pytz.UTC)
        assert deserialize_timestamp(timestamp) == expected

    # Raises a ValueError when given an empty string
    def test_empty_string(self):
        timestamp = ''
        with pytest.raises(ValueError):
            deserialize_timestamp(timestamp)

    # Raises a ValueError when given a timestamp string with an invalid format
    def test_invalid_format(self):
        # non iso format
        timestamp = '2020/12/31 23:59:59Z'
        with pytest.raises(ValueError):
            deserialize_timestamp(timestamp)

    # Raises a TypeError when given a non-string input
    def test_non_string_input(self):
        timestamp = 12345
        with pytest.raises(TypeError):
            deserialize_timestamp(timestamp)

class TestSerializeTimezone:

    # Serializes a timezone string to its integer offset representation
    def test_serialize_timezone_string(self):
        assert serialize_timezone("11") == 11
        assert serialize_timezone("10") == 10
        assert serialize_timezone("0") == 0
        assert serialize_timezone("-11") == -11
        assert serialize_timezone("-12") == -12

    # Serializes a timezone object to its integer offset representation
    def test_serialize_timezone_object(self):
        class FakeTimezone(datetime.tzinfo):
            def utcoffset(self, dt):
                return datetime.timedelta(hours=5)

        tz = FakeTimezone()
        assert serialize_timezone(tz) == 5

    # Returns the correct integer offset for positive and negative timezones
    def test_serialize_timezone_positive_negative(self):
        assert serialize_timezone("5") == 5
        assert serialize_timezone("-5") == -5

    # Raises a ValueError if the timezone string is not a valid integer
    def test_serialize_timezone_invalid_string(self):
        with pytest.raises(ValueError):
            serialize_timezone("abc")

    # Returns the correct integer offset for the maximum positive timezone (+14)
    def test_serialize_timezone_max_positive(self):
        assert serialize_timezone("14") == 14

    # Returns the correct integer offset for the maximum negative timezone (-12)
    def test_serialize_timezone_max_negative(self):
        assert serialize_timezone("-12") == -12