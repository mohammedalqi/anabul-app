# dog-breed

Aplikasi deploy ML models to cloud run

This repository contains an application that deploys machine learning models to Cloud Run for dog breed classification. The application allows you to upload a dog image and get the predicted breed using the deployed ML model.

## Usage

1. Place your trained ML model (in .h5 format) in the project directory.
2. Adjust the shape, model name, and path in the main.py file to match your specific ML model.
3. Run the main.py file using the following command:

   ```bash
   python main.py
   ```

   This will start the Flask server, allowing you to interact with the application.

4. Test the application using either Postman or the provided test.py script.

- If using Postman, send a POST request to the server's URL with the dog image file as the payload, using the appropriate key and value. The server will respond with the predicted dog breed.
- If using the test.py script, run it using the following command:
  ```bash
  python test.py
  ```
  This script will send a test request to the server and display the predicted dog breed.
