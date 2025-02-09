import requests
import json

# API endpoint to get the current location of the ISS
api_url = "http://api.open-notify.org/iss-now.json"

# Send a GET request to the API
response = requests.get(api_url)

# Test the connection by printing the status code
print("Status Code:", response.status_code)

# Print the unformatted response
print("\nUnformatted Response:")
print(response.text)

# Function to print the formatted JSON response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Print the formatted JSON response
print("\nFormatted Response:")
jprint(response.json())
