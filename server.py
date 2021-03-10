from flask import Flask

app = Flask(__name__, static_folder='./frontend/build', static_url_path='/')


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
        "description": 'This is test data',
    }


if __name__ == '__main__':
    app.run(debug=True)
