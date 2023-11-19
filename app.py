from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the root URL

# Define a route for handling the form submission
@app.route('/greet', methods=['POST'])
def greet():
    
    return "hello"

if __name__ == '__main__':
    # Run the application on http://127.0.0.1:5000/
    app.run(debug=True)
