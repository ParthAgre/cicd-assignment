from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    """This function runs when someone visits the main page."""
    return 'Hi! The CI/CD pipeline is working automatically!'

# This block runs the app when the script is executed directly
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
