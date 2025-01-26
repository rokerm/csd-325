import unittest
from city_functions import format_city_country

class TestCityFunctions(unittest.TestCase):
    """ 
    Test class for the format_city_country function.
    """
    def test_city_country(self):
        """
        Test that the function correctly formats city and country names.
        """
        formatted_name = format_city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()