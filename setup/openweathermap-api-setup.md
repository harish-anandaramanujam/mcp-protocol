# Obtaining an OpenWeatherMap API Key

- **API Documentation:** [One Call API 3.0](https://openweathermap.org/api/one-call-3)
- **API Keys:** Create or find your API keys after subscribing at [OpenWeatherMap API Keys](https://home.openweathermap.org/api_keys)


## 1. Create an Account

1. Visit [OpenWeatherMap Sign Up](https://home.openweathermap.org/users/sign_up).
2. Fill in your email, username, and password.
3. Confirm your email address via the verification email sent to you.

## 2. Choose a Subscription Plan

- **Free Plan**:  
    - Cost: $0  
    - Includes basic weather data (current, forecast, historical) with limited requests per minute/day.
- **Paid Plans**:  
    - Start at $10/month (as of June 2024).
    - Higher request limits, advanced data (e.g., One Call API, weather maps, alerts).
    - Compare plans at [OpenWeatherMap Pricing](https://openweathermap.org/price).

**Recommendation:**  
Start with the Free plan for development/testing. Upgrade if you need higher limits or advanced features.

## 3. Generate an API Key

1. Log in to your OpenWeatherMap account.
2. Go to the [API keys page](https://home.openweathermap.org/api_keys).
3. Click **"Create Key"**.
4. Enter a name for your key and submit.
5. Copy the generated API key for use in your applications.

## 4. Store the API Key Locally

To keep your API key secure and out of your codebase:

- **Environment Variable (Recommended):**
    1. Create a file named `.env` in your project directory.
    2. Add the following line (replace with your actual key):
        ```
        OPENWEATHERMAP_API_KEY=your_api_key_here
        ```
    3. Use a library like `dotenv` (for Node.js or Python) to load the variable in your application.
    4. Add `.env` to your `.gitignore` file to prevent accidental commits.

- **Configuration File (Alternative):**
    - Store the key in a local configuration file (e.g., `config.json`) that is excluded from version control.

**Never commit your API key to public repositories.**

## 5. Usage Notes

- It may take up to 2 hours for a new API key to become active.
- Keep your API key secure; do not expose it in public repositories.

## 6. References

- [OpenWeatherMap Documentation](https://openweathermap.org/api)
- [Pricing Details](https://openweathermap.org/price)
- [FAQ](https://openweathermap.org/faq)