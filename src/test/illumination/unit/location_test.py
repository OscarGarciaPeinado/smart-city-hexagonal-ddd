from illumination.domain.entity.location import Location
from illumination.domain.exceptions.malformed_location_exception import MalformedLocationException
import pytest


def test_malformed_latitude_location():
    # given
    latitude = -91
    longitude = 100

    # when
    with pytest.raises(MalformedLocationException):
        Location(latitude, longitude)


def test_malformed_longitude_location():
    # given
    latitude = 80
    longitude = 200

    # when
    with pytest.raises(MalformedLocationException):
        Location(latitude, longitude)


def test_comparable_longitude_location():
    # given
    latitude = 80
    longitude = 100

    # when
    location = Location(latitude, longitude)

    # then
    assert location == Location(latitude, longitude)
