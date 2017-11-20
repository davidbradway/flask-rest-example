from flask import Flask, request, jsonify, render_template, url_for
import numbers
app = Flask(__name__)


@app.route('/d3')
def show_entries():
    return render_template('index.html')


@app.route("/api/hello/<name>", methods=['GET'])
def hello(name):
    return "Hello World! " + name


@app.route("/api/data", methods=['GET'])
def data():
    my_dict = {
               "temp": [20, 21, 21],
               "time": [10, 20, 30],
               "unit": "s"
              }
    return jsonify(my_dict)


@app.route("/api/add", methods=['POST'])
def add():
    if (request.is_json):
        content = request.get_json()
        if 'a' in content and 'b' in content:
            if isinstance(content['a'], numbers.Number) and isinstance(content['b'], numbers.Number):
                return str(content['a'] + content['b']), 200
    return {}, 400
