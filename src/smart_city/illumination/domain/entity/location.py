from illumination.domain.exceptions.malformed_location_exception import MalformedLocationException


class Location:
    def __init__(self, latitude: int, longitude: int):
        self.__set_location(latitude, longitude)

    def __set_location(self, latitude, longitude):
        if latitude > 90 or latitude < -90:
            raise MalformedLocationException()
        if longitude > 180 or longitude < -180:
            raise MalformedLocationException()
        self.longitude = longitude
        self.latitude = latitude

    def __eq__(self, other):
        is_data_equal = other.latitude == self.latitude and other.longitude == self.longitude
        return isinstance(other, Location) and is_data_equal
