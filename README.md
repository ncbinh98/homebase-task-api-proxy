#API Proxy with Python

A simple Python script that acts as a proxy to forward HTTP requests to an Express API. This project is useful when you need to access an Express API through a Python-based proxy server.

## Features

- Proxy HTTP GET, POST, PUT, and DELETE requests to an Express API server.
- Relay responses from the Express API server back to the client.

## Prerequisites

- Python 3.x
- [requests](https://pypi.org/project/requests/) library (install using `pip install requests`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ncbinh98/homebase-task-api-proxy.git
   cd homebase-task-api-proxy
   ```

2. Edit the `main.py` file to set the `API_BASE_URL` to the URL of your Express API server.

3. Run the proxy server:

   ```bash
   python proxy.py
   ```

4. The proxy server will start and listen on the specified port (default is 5000).

5. Send HTTP requests to the proxy server at `http://localhost:5000` (or the host and port you configured in `proxy.py`). The proxy server will forward requests to the Express API server and relay responses back to the client.

## Configuration

In the `proxy.py` script, you can configure the following variables:

- `API_BASE_URL`: Set this variable to the base URL of your Express API server.
- `app.run(host='0.0.0.0', port=5000)`: You can change the host and port to suit your requirements.
