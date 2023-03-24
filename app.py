from flask import Flask
from flask import request, redirect, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    params_post = {}
    sum = 5000000
    proc = 50
    term = 180
    idx = 1
    for p in request.form:
        params_post[p] = request.form[p]
        if idx == 1:
            sum = int(params_post[p])*1000000
        if idx == 2:
            proc = int(params_post[p])
        if idx == 3:
            term = int(params_post[p])
        idx += 1

    

    return render_template('index.html', params_post=request.form)


if __name__ == '__main__':
    app.run(debug=True)