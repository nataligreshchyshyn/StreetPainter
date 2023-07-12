import math

class AzimuthCalculator:
    """
    A class to calculate the azimuth (direction) between two points.

    Attributes:
        lat1 (float): The latitude of the starting point.
        lon1 (float): The longitude of the starting point.
        lat2 (float): The latitude of the ending point.
        lon2 (float): The longitude of the ending point.
    """

    def __init__(self, lat1, lon1, lat2, lon2):
        """
        Initializes the AzimuthCalculator object with the provided latitude and longitude values.

        Args:
            lat1 (float): The latitude of the starting point.
            lon1 (float): The longitude of the starting point.
            lat2 (float): The latitude of the ending point.
            lon2 (float): The longitude of the ending point.
        """
        self.lat1 = lat1
        self.lon1 = lon1
        self.lat2 = lat2
        self.lon2 = lon2

    def calculate_azimuth(self):
        """
        Calculates the azimuth (direction) between the two points.

        Returns:
            float: The calculated azimuth value in degrees.
        """
        lat1_rad = math.radians(self.lat1)
        lon1_rad = math.radians(self.lon1)
        lat2_rad = math.radians(self.lat2)
        lon2_rad = math.radians(self.lon2)

        delta_lon = lon2_rad - lon1_rad

        y = math.sin(delta_lon) * math.cos(lat2_rad)
        x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(delta_lon)
        azimuth_rad = math.atan2(y, x)

        azimuth_deg = math.degrees(azimuth_rad)

        normalized_azimuth = (azimuth_deg + 180) % 180

        return normalized_azimuth
