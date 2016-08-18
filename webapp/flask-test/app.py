# We'll render HTML templates and access data sent by POST
# using the request object from flask
from flask import Flask, render_template, request
import json

# Initialize the Flask application
app = Flask(__name__)


# This route will show a form to submit some JSON data
@app.route('/')
def index():
    return render_template('form.html')


# This route will accept a request containing JSON
# Then we'll convert that data into Python a structure
# and print it.
# Because we used a standard HTML form post to send the
# data, we need to get the JSON from request.form
# If on other hand the information was sent from an app,
# or even a python urllib2.Request we would need to use
# request.data to get the JSON string
@app.route('/request', methods=['POST'])
def jsonreq():
    # Get the JSON data sent from the form
    jsondata = request.form['jsondata']
    # Convert the JSON data into a Python structure
    data = json.loads(jsondata)
    return render_template('request.html', data=data, jsondata=jsondata)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80")
    )
