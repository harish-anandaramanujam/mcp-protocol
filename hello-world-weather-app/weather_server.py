from mcp.server.fastmcp import FastMCP
import requests
import json
import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("open-weather-map-api-key")

mcp = FastMCP("Weather Data Server")

@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    Fetches the current weather for a given city using OpenWeatherMap API 3.0.
    First gets coordinates using geocoding API, then fetches current weather using One Call API 3.0.
    """
    try:
        # Step 1: Get coordinates for the city using geocoding API
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()  # Raise exception for bad status codes
        geo_data = geo_response.json()
        
        if not geo_data:
            return f"Error: City '{city}' not found"
        
        # Extract coordinates
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        
        # Step 2: Get current weather using One Call API 3.0
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&exclude=minutely,alerts"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()  # Raise exception for bad status codes
        weather_data = weather_response.json()
        
        return weather_data
        
    except requests.RequestException as e:
        return f"Error making API request: {str(e)}"
    except KeyError as e:
        return f"Error parsing API response: {str(e)}"
    except IndexError:
        return f"Error: City '{city}' not found in geocoding results"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

@mcp.tool()
def get_weather_forecast(city: str) -> str:
    """
    Fetches the 5-day weather forecast for a given city using OpenWeatherMap API 3.0.
    """
    try:
        # Step 1: Get coordinates for the city using geocoding API
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if not geo_data:
            return f"Error: City '{city}' not found"
        
        # Extract coordinates
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        
        # Step 2: Get forecast using One Call API 3.0 (includes 8-day daily forecast)
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&exclude=current,minutely,alerts"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        return weather_data
        
    except requests.RequestException as e:
        return f"Error making API request: {str(e)}"
    except KeyError as e:
        return f"Error parsing API response: {str(e)}"
    except IndexError:
        return f"Error: City '{city}' not found in geocoding results"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

@mcp.tool()
def get_historical_weather(city: str, timestamp: int) -> str:
    """
    Fetches historical weather data for a given city using OpenWeatherMap API 3.0.
    
    Args:
        city: City name
        timestamp: Unix timestamp for the date you want historical data
    """
    try:
        # Step 1: Get coordinates for the city using geocoding API
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if not geo_data:
            return f"Error: City '{city}' not found"
        
        # Extract coordinates
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        
        # Step 2: Get historical weather using One Call API 3.0 timemachine
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        return weather_data
        
    except requests.RequestException as e:
        return f"Error making API request: {str(e)}"
    except KeyError as e:
        return f"Error parsing API response: {str(e)}"
    except IndexError:
        return f"Error: City '{city}' not found in geocoding results"
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"


@mcp.prompt()
def ask_about_current_weather(city: str) -> str:
    """Generate a user message asking for the current weather in a city."""
    return get_current_weather(city)

# Start the MCP server
if __name__ == "__main__":
    print("Weather MCP Server starting...")
    mcp.run()
