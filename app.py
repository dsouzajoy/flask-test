import json
from flask import Flask
import os
app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/test')
def get_test_data():
    return json.dumps([{
        "name": 'Royal Chicken Biriyani',
    }, {
        "name": "Nizami Chicken Biriyani",
    }, {
        "name": "Special Chicken Biriyani",
    }, {
        "name": "Special Supreme Chicken Biriyani",
    }, {
        "name": "Paneer Tikka"
    }, {
        "name": "Paneer Chilli",
    }, {
        "name": "Vegetable Manchurian",
    }, {
        "name": "Baby Corn Paneer",
    }, {
        "name": "Chicken Shawarma",
    }])


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support

    port = int(os.environ.get('PORT', 33507))
    app.run(threaded=True, port=port)
