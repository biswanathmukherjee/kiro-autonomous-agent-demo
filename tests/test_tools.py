"""Tests for custom tools."""

from tools.calculator import calculate
from tools.weather import get_weather


class TestGetWeather:
    def test_known_city(self):
        result = get_weather(city="New York")
        assert "New York" in result
        assert "Partly Cloudy" in result
        assert "72" in result
        assert "55%" in result

    def test_known_city_case_insensitive(self):
        result = get_weather(city="tokyo")
        assert "tokyo" in result
        assert "Sunny" in result

    def test_unknown_city(self):
        result = get_weather(city="Atlantis")
        assert "not available" in result
        assert "Atlantis" in result

    def test_all_known_cities(self):
        cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
        for city in cities:
            result = get_weather(city=city)
            assert "not available" not in result


class TestCalculate:
    def test_addition(self):
        result = calculate(expression="2 + 3")
        assert "= 5" in result

    def test_multiplication(self):
        result = calculate(expression="4 * 5")
        assert "= 20" in result

    def test_complex_expression(self):
        result = calculate(expression="(2 + 3) * 4")
        assert "= 20" in result

    def test_division(self):
        result = calculate(expression="10 / 2")
        assert "= 5" in result

    def test_invalid_characters(self):
        result = calculate(expression="import os")
        assert "Error" in result
        assert "invalid characters" in result

    def test_division_by_zero(self):
        result = calculate(expression="1 / 0")
        assert "Error" in result
