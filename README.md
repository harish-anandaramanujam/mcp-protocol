# MCP Protocol

This project uses the OpenWeatherMap API to fetch weather data.

## OpenWeatherMap API

- **API Documentation:** [One Call API 3.0](https://openweathermap.org/api/one-call-3)
- **API Keys:** Create or find your API keys after subscribing at [OpenWeatherMap API Keys](https://home.openweathermap.org/api_keys)

## Setup

1. **Create a virtual environment in the current directory:**
    ```sh
    python -m venv mcp-env
    ```

2. **Activate the virtual environment (Windows):**
    ```sh
    mcp-env\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Inspect the weather server in development mode:**
    ```sh
    mcp dev weather_server.py
    ```
    This command starts the weather server in development mode. It will generate a link on localhost with your API key appended. Copy the entire link and open it in your browser. Connect to the MCP server using the STDIO connection to explore available options. You can view the created tools under the **Tools** tab.

5. **Example: Installing the Weather Data Server**

To install the weather server, run:

```sh
mcp install weather_server.py --name "Weather Data Server"
```


## Using Claude Desktop as an MCP Client

To interact with MCP servers, you can use **Claude Desktop**, a user-friendly MCP client. Claude Desktop can discover, connect to, and interact with running MCP servers. When configured to use an MCP server, it provides access to the tools and resources offered by that server during your conversations.

While other MCP clients can also connect to the same servers, Claude Desktop offers a chat interface that makes it easy to use the server's capabilities as conversational tools. The desktop app manages protocol communication and presents the MCP server's features as tools you can use naturally.

## Screenshots

### MCP Inspector

<img width="1726" alt="Screenshot 1" src="https://github.com/user-attachments/assets/ba3f3f00-a1a7-4276-9f2a-d2940bd1fa56" />

### Claude Desktop Showing Installed Tools

<img width="996" alt="Screenshot 2" src="https://github.com/user-attachments/assets/589ba76b-b3c2-4024-aab0-f273358afa1b" />

### Conversing with Claude Using Custom Installed Tools

<img width="999" alt="Screenshot 3" src="https://github.com/user-attachments/assets/60bd2698-fc54-4d32-95eb-f335ad229e99" />

