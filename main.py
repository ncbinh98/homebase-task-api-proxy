import requests
from flask import Flask, request, Response

app = Flask(__name__)


API_BASE_URL = "http://localhost:3000"

# Define a route that will capture all incoming requests and proxy them to the Express API
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    url = f"{API_BASE_URL}/{path}"
    
    # Get the request method and data
    method = request.method
    data = request.data

    # Prepare headers by forwarding all headers from the original request
    headers = {key: value for (key, value) in request.headers}

    # Make a request to the Express API and get the response
    response = requests.request(method, url, data=data, headers=headers)

    # Forward the Express API's response to the client
    return Response(response.content, response.status_code, content_type=response.headers['content-type'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # You can change the port as needed
