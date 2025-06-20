import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="vars/.env")
# print(os.getenv("open-weather-map-api-key"))

from mcp.server.fastmcp import FastMCP
import requests
import json

# OpenWeatherMap API key (replace with your own API key)
API_KEY = os.getenv("open-weather-map-api-key")
BASE_URL = "http://api.openweathermap.org/data/2.5"

# Create an MCP server with a custom name
mcp = FastMCP("Weather Data Server")

# Function to fetch current weather data
@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    Fetches the current weather for a given city.
    """
    try:
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message')}"
        main_data = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        return f"The current weather in {city} is {weather} with a temperature of {temperature}°C and humidity of {humidity}%. "
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"
    
# Function to fetch weather forecast for the next 5 days
@mcp.tool()
def get_weather_forecast(city: str) -> str:
    """
    Fetches the 5-day weather forecast for a given city.
    """
    try:
        url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != "200":
            return f"Error: {data.get('message')}"
        forecast = ""
        for entry in data["list"]:
            time = entry["dt_txt"]
            weather = entry["weather"][0]["description"]
            temperature = entry["main"]["temp"]
            forecast += f"At {time}, the weather will be {weather} with a temperature of {temperature}°C. "
        return forecast
    except Exception as e:
        return f"Error fetching forecast data: {str(e)}"
    
# Function to fetch historical weather data (last 5 days)
@mcp.tool()
def get_historical_weather(city: str) -> str:
    """
    Fetches historical weather data for a given city (last 5 days).
    """
    try:
        url = f"{BASE_URL}/timemachine?lat={city_lat}&lon={city_lon}&dt={timestamp}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message')}"
        historical_data = data["current"]
        temperature = historical_data["temp"]
        weather = historical_data["weather"][0]["description"]
        return f"Historical weather data: {weather} with a temperature of {temperature}°C."
    except Exception as e:
        return f"Error fetching historical data: {str(e)}"
    

# Start the MCP server
if __name__ == "__main__":
    mcp.run()

    