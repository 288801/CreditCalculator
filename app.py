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
            sum = float(params_post[p])*1000000
        if idx == 2:
            proc = int(params_post[p])
        if idx == 3:
            term = int(params_post[p])
        idx += 1

    print(request.form)

    return render_template('index.html', params_post=an(sum, proc, term))


def an(s, p, t):
    s1 = s
    m = p/1200
    k = round((m*(1+m)**t)/((1+m)**t-1),3)
    result = {'№месяца': [], 'Платеж': [], 'Остаток кредита': []}
    for i in range(t):
        result['№месяца'].append(i+1)
        result['Платеж'].append(k*s)
        s1 -= k*s
        result['Остаток кредита'].append(s1)
    return result

# def dif(s, p, t):
#


if __name__ == '__main__':
    app.run(debug=True)