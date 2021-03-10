from flask import Flask
from flask_cors import CORS
app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')
CORS(app)


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/test')
def get_test_data():
    return {
        "name": 'test',
        "description": 'This is test data from server',
    }


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
