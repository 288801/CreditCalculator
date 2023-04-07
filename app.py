from flask import Flask
from flask import request, redirect, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['post', 'get'])
def index():
    params_post = {}
    sum = 100000
    proc = 20
    term = 30
    idx = 1
    type = "an"
    for p in request.form:
        params_post[p] = request.form[p]
        if idx == 1:
            sum = float(params_post[p])*1000000
        if idx == 2:
            proc = int(params_post[p])
        if idx == 3:
            term = int(params_post[p])
        if idx == 4:
            type = params_post[p]
        idx += 1

    if type == "an":
        return render_template('index.html', params_post=an(sum, proc, term))
    else:
        return render_template('index.html', params_post=dif(sum, proc, term))


def an(s, p, t):
    s1 = s
    m = p/1200
    k = round((m*(1+m)**t)/((1+m)**t-1), 3)
    result = {'№месяца': [], 'Платеж': [], 'Остаток кредита': []}
    for i in range(t):
        result['№месяца'].append(i+1)
        if i > 0 and round(k*s, 1) > result['Остаток кредита'][i-1]:
            result['Платеж'].append(result['Остаток кредита'][i-1])
        else:
            result['Платеж'].append(round(k * s, 1))
        s1 = s1*(1+m) - k*s
        if s1 < 0:
            result['Остаток кредита'].append(0)
        else:
            result['Остаток кредита'].append(round(s1, 1))
    return result

def dif(s, p, t):
    s1 = s
    m = p/1200
    d = s/t
    result = {'№месяца': [], 'Платеж': [], 'Остаток кредита': []}
    for i in range(t):
        result['№месяца'].append(i + 1)
        if i > 0 and round(d + s1*m, 1) > result['Остаток кредита'][i-1]:
            result['Платеж'].append(result['Остаток кредита'][i-1])
        else:
            result['Платеж'].append(round(d + s1*m, 1))
        s1 -= d
        if s1 < 0:
            result['Остаток кредита'].append(0)
        else:
            result['Остаток кредита'].append(round(s1, 1))
    return result


if __name__ == '__main__':
    app.run(debug=True)
