from flask import Flask
from flask import request, redirect, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    params_get = {}
    for p in request.args:
        params_get[p] = request.args[p]

    params_post = {}
    for p in request.form:
        params_post[p] = request.form[p]

    return render_template('index.html', params_get=params_get, params_post=params_post)


if __name__ == '__main__':
    app.run(debug=True)