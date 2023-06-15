import requests

# Set the URL for the predict endpoint
url = "http://127.0.0.1:5000/breed/dog"

# Set the path to the image file you want to test
image_path = "images/golden.jpg"

# Send a POST request to the Flask app
with open(image_path, "rb") as file:
    files = {"file": file}
    response = requests.post(url, files=files)

# Check the response status
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    print("Error:", response.status_code)
