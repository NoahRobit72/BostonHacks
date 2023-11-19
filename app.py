from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the root URL

# Define a route for handling the form submission
@app.route('/getImage', methods=['POST'])
def getImage():
    # Assuming the image name is sent as form data
    image_name = request.args.get('imageName')
    
    
    print("OK Received. I am now going to try to query Firebase for an image with a name: " + str(image_name))    
    return "function returns"

if __name__ == '__main__':
    # Run the application on http://127.0.0.1:5000/
    app.run(debug=True)


# use: http://127.0.0.1:5000/getImage?imageName=hello