from strands import tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city.

    Args:
        city: The name of the city to get weather for.

    Returns:
        A string describing the current weather conditions.
    """
    weather_data = {
        "new york": {"temp": 72, "condition": "Partly Cloudy", "humidity": 55},
        "london": {"temp": 59, "condition": "Rainy", "humidity": 80},
        "tokyo": {"temp": 68, "condition": "Sunny", "humidity": 45},
        "paris": {"temp": 64, "condition": "Overcast", "humidity": 70},
        "sydney": {"temp": 77, "condition": "Clear", "humidity": 40},
    }

    city_lower = city.lower()
    if city_lower in weather_data:
        data = weather_data[city_lower]
        return (
            f"Weather in {city}: {data['condition']}, "
            f"Temperature: {data['temp']}F, "
            f"Humidity: {data['humidity']}%"
        )
    return f"Weather data not available for {city}. Try: New York, London, Tokyo, Paris, or Sydney."
