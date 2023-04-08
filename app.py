from flask import Flask
from flask import request, redirect, render_template, url_for, send_from_directory

app = Flask(__name__)
params = {'sum': 100000, 'proc': 20, 'term': 30, 'an': True, 'dif': False}

@app.route('/', methods=['post', 'get'])
def index():
    global params
    params_post = {}
    idx = 1
    type = "an" if params['an'] else "dif"
    for p in request.form:
        params_post[p] = request.form[p]
        if idx == 1:
            params['sum'] = int(params_post[p])
        if idx == 2:
            params['proc'] = int(params_post[p])
        if idx == 3:
            params['term'] = int(params_post[p])
        if idx == 4:
            type = params_post[p]
        idx += 1

    if type == "an":
        params['an'] = True
        params['dif'] = False
        return render_template('index.html', params_post=an(params['sum'], params['proc'], params['term']), params=params)
    else:
        params['an'] = False
        params['dif'] = True
        return render_template('index.html', params_post=dif(params['sum'], params['proc'], params['term']), params=params)


def an(s, p, t):
    s1 = s
    ss = 0
    m = p/1200
    k = round((m*(1+m)**t)/((1+m)**t-1), 3)
    result = {'№месяца': [], 'Платеж': [], 'Остаток кредита': [], 'Переплата': 0}
    for i in range(t):
        result['№месяца'].append(i+1)
        if i > 0 and round(k*s, 1) > result['Остаток кредита'][i-1]:
            result['Платеж'].append(result['Остаток кредита'][i-1])
            ss+=result['Остаток кредита'][i-1]
        else:
            result['Платеж'].append(round(k * s, 1))
            ss+=round(k * s, 1)
        s1 = s1*(1+m) - k*s
        if s1 < 0:
            result['Остаток кредита'].append(0)
        else:
            result['Остаток кредита'].append(round(s1, 1))

    result['Переплата'] = round(ss-s, 3)
    return result

def dif(s, p, t):
    s1 = s
    ss = 0
    m = p/1200
    d = s/t
    result = {'№месяца': [], 'Платеж': [], 'Остаток кредита': [], 'Переплата': 0}
    for i in range(t):
        result['№месяца'].append(i + 1)
        if i > 0 and round(d + s1*m, 1) > result['Остаток кредита'][i-1]:
            result['Платеж'].append(result['Остаток кредита'][i-1])
            ss+=result['Остаток кредита'][i-1]
        else:
            result['Платеж'].append(round(d + s1*m, 1))
            ss+=round(d + s1*m, 1)
        s1 -= d
        if s1 < 0:
            result['Остаток кредита'].append(0)
        else:
            result['Остаток кредита'].append(round(s1, 1))

    result['Переплата'] = round(ss-s, 3)
    return result


if __name__ == '__main__':
    app.run(debug=True)
