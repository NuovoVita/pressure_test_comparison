from flask import Flask, jsonify, make_response, render_template

app = Flask(__name__)


@app.route('/')
def main_handler():
    return make_response('Hello, welcome to pure flask world!')


@app.route('/template')
def template_handler():
    return render_template(
        'main_for_flask.html', messages="whatever", title="home", number=10000)


@app.route('/json')
def json_handler():
    return jsonify({"status": 1, "message": "OK", "data": {}})


if __name__ == '__main__':
    app.run(port=8000, debug=False)
