from flask import Flask, render_template, request
from storage import *
from story_jared import *
from flask_cors import CORS
from tempMain import *

app = Flask(__name__)
CORS(app)   #Enable CORS for all routes
# Define a route for the root URL

# Define a route for handling the form submission
@app.route('/getImage', methods=['POST'])
def getImage():
    # Assuming the image name is sent as form data
    image_name = request.args.get('imageName')
    image_name = "Canvas2"
    print("OK Received. I am now going to try to query Firebase for an image with a name: " + str(image_name))    
    
    storagemain(image_name)
    processImage()
    


    return "function returns"



if __name__ == '__main__':
    # Run the application on http://127.0.0.1:5000/
   # app.run(host = '10.239.186.227', port = 5000, debug = True)
   app.run(host = '127.0.0.1', port = 5000, debug = True)