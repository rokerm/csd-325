def format_city_country(city, country, population=None, language=None):
    """
    Function to format the city and country names into "City, Country - population xxx, Language" format.
    :param city: Name of the city (str)
    :param country: Name of the country (str)
    :param population: Population of the city (int)
    :param language: Language spoken in the city (str)
    :return: A formatted string "City, Country - population xxx, language" (str)
    """
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    elif language:
        return f"{city.title()}, {country.title()} - {language.title()}"
    else:
        return f"{city.title()}, {country.title()}"

# Calling the function with different city, country and population values
formatted_1 = format_city_country("santiago", "chile",)
formatted_2 = format_city_country("tokyo", "japan", 14000000)
formatted_3 = format_city_country("paris", "france", 2200000, "french")

# Printing the results
print(formatted_1)
print(formatted_2)
print(formatted_3)