from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a route for handling the form submission
@app.route('/getImage', methods=['POST'])
def getImage():
    # Assuming the image name is sent as a query parameter
    image_name = request.args.get('imageName')

    print("OK Received. I am now going to try to query Firebase for an image with a name: " + str(image_name))
    # Additional logic for querying Firebase or any other operations can be added here

    return "Function returns"


@app.route('/getStatus', methods=['GET'])
def getStatus():
    status = 1# Replace this with your actual logic
    
    return str(status)


if __name__ == '__main__':
    # Run the application on http://127.0.0.1:5000/
    app.run(debug=True)
