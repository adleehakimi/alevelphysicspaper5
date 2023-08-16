from flask import Flask, render_template, redirect, url_for, request, session
import math
from calculate_gradient import f_gradient_bfl, f_gradient_wfl, f_gradient_change
from calculate_y_intercept import f_y_intercept_bfl, f_y_intercept_wfl, f_dy_intercept
from calculate_Y import f_Y, f_dY
from calculate_Z import f_Z, f_dZ
from calculate_θ import f_temperature
from scientific_notation import f_scientific_form_gradient, f_scientific_form_dm, f_scientific_form_y_intercept, f_scientific_form_dy_intercept, f_scientific_form_Y, f_scientific_form_dY, f_scientific_form_Z, f_scientific_form_dZ, f_scientific_form_temperature, round_to_significant_figures

app = Flask(__name__, template_folder='template')
app.secret_key = 'your_secret_key'
app.static_folder = 'static'

#Members API Route

@app.route("/alevelphysicspaper5")
def index():
    return render_template('index.html')

@app.route("/calculate")
def calculate():
    return render_template('calculate.html')

@app.route("/variable-gradient-y-intercept")
def first():
    return render_template('firstcal.html')

@app.route("/value-gradient", methods=["POST", "GET"])
def second():
    bfl = None
    wfl = None
    dm = None
    if request.method == "POST":
        x_1 = float(request.form['x_1'])
        y_1 = float(request.form['y_1'])
        x_2 = float(request.form['x_2'])
        y_2 = float(request.form['y_2'])
        x_3 = float(request.form['x_3'])
        y_3 = float(request.form['y_3'])
        x_4 = float(request.form['x_4'])
        y_4 = float(request.form['y_4'])
        bfl = f_gradient_bfl(x_1, y_1, x_2, y_2)
        wfl = f_gradient_wfl(x_3, y_3, x_4, y_4)
        dm = f_gradient_change(bfl, wfl)

        bfl = f_scientific_form_gradient(bfl, 2)
        wfl = f_scientific_form_gradient(wfl, 2)
        dm = f_scientific_form_dm(dm, 2)

        return render_template('second.html', bfl=bfl, wfl=wfl, dm=dm)
    else:
        return render_template('second.html', bfl="", wfl="", dm="")

@app.route("/value-y-intercept", methods=["POST", "GET"])
def third():
    y_intercept_bfl = None
    dy_intercept = None
    if request.method == "POST":
        x_1 = float(request.form['x_1'])
        y_1 = float(request.form['y_1'])
        mbfl = float(request.form['mbfl'])
        mwfl = float(request.form['mwfl'])
        y_intercept_bfl = f_y_intercept_bfl(x_1, y_1, mbfl)
        y_intercept_wfl = f_y_intercept_wfl(x_1, y_1, mwfl)
        dy_intercept = f_dy_intercept(y_intercept_bfl, y_intercept_wfl)

        y_intercept_bfl = f_scientific_form_y_intercept(y_intercept_bfl, 3)
        y_intercept_wfl = f_scientific_form_y_intercept(y_intercept_wfl, 3)
        dy_intercept = f_scientific_form_dy_intercept(dy_intercept, 3)
        return render_template('third.html', y_intercept_bfl=y_intercept_bfl, dy_intercept=dy_intercept)
    else:
        return render_template('third.html', y_intercept_bfl="", dy_intercept="")

@app.route("/value-constant")
def fourth():
    return render_template('fourth.html')

@app.route("/value-constant-Y", methods=["POST", "GET"])
def fourthy():
    Y = None
    dY = None
    if request.method == "POST":
        mbfl = float(request.form['mbfl'])
        dm = float(request.form['dm'])
        Y = f_Y(mbfl)
        dY = f_dY(Y, mbfl, dm)

        Y = f_scientific_form_Y(Y, 2)
        dY = f_scientific_form_dY(dY, 2)
        return render_template('fourth-Y.html', Y=Y, dY=dY)
    else:
        return render_template('fourth-Y.html', Y="(calculate to get value)", dY="(calculate to get value)")

@app.route("/value-constant-Z", methods=["POST", "GET"])
def fourthz():
    Z = None
    dZ = None
    if request.method == "POST":
        y_intercept = float(request.form['y_intercept'])
        dy_intercept = float(request.form['dy_intercept'])
        mbfl = float(request.form['mbfl'])
        dm = float(request.form['dm'])
        Z = f_Z(y_intercept, mbfl)
        dZ = f_dZ(y_intercept, dy_intercept, mbfl, dm, Z)

        Z = f_scientific_form_Z(Z, 2)
        dZ = f_scientific_form_dZ(dZ, 2)
        return render_template('fourth-Z.html', Z=Z, dZ=dZ)
    return render_template('fourth-Z.html', Z="(calculate to get value)", dZ="(calculate to get value)")

@app.route("/value-conditions", methods=["POST", "GET"])
def fifth():
    temperature = None
    if request.method == "POST":
        Y = float(request.form['Y'])
        Z = float(request.form['Z'])
        temperature = f_temperature(Y,Z) + 273
        temperature = f_scientific_form_temperature(temperature, 2)
        return render_template('fifth.html', temperature=temperature)
    else:
        return render_template('fifth.html', temperature="(calculate to get value)")
    
@app.route("/main", methods=["POST", "GET"])
def main():
    bfl_1 = None
    wfl_1 = None
    dm_1 = None
    y_intercept_bfl_2 = None
    dy_intercept_2 = None
    Y_3 = None
    dY_3 = None
    Z_4 = None
    dZ_4 = None
    temperature = None
    if request.method == "POST":
        if 'submit1' in request.form:
            x_1_1 = float(request.form['x_1_1'])
            y_1_1 = float(request.form['y_1_1'])
            x_2_1 = float(request.form['x_2_1'])
            y_2_1 = float(request.form['y_2_1'])
            x_3_1 = float(request.form['x_3_1'])
            y_3_1 = float(request.form['y_3_1'])
            x_4_1 = float(request.form['x_4_1'])
            y_4_1 = float(request.form['y_4_1'])
            bfl_1 = f_gradient_bfl(x_1_1, y_1_1, x_2_1, y_2_1)
            wfl_1 = f_gradient_wfl(x_3_1, y_3_1, x_4_1, y_4_1)
            dm_1 = f_gradient_change(bfl_1, wfl_1)

            bfl_1 = f_scientific_form_gradient(bfl_1, 2)
            wfl_1 = f_scientific_form_gradient(wfl_1, 2)
            dm_1 = f_scientific_form_dm(dm_1, 2)

            session['bfl_1'] = bfl_1
            session['wfl_1'] = wfl_1
            session['dm_1'] = dm_1
            return render_template('main.html', bfl_1=bfl_1, wfl_1=wfl_1, dm_1=dm_1)
        
        elif 'submit2' in request.form:
            x_1_2 = float(request.form['x_1_2'])
            y_1_2 = float(request.form['y_1_2'])
            mbfl_2 = float(request.form['mbfl_2'])
            mwfl_2 = float(request.form['mwfl_2'])
            y_intercept_bfl_2 = f_y_intercept_bfl(x_1_2, y_1_2, mbfl_2)
            y_intercept_wfl_2 = f_y_intercept_wfl(x_1_2, y_1_2, mwfl_2)
            dy_intercept_2 = f_dy_intercept(y_intercept_bfl_2, y_intercept_wfl_2)

            y_intercept_bfl_2 = f_scientific_form_y_intercept(y_intercept_bfl_2, 3)
            y_intercept_wfl_2 = f_scientific_form_y_intercept(y_intercept_wfl_2, 3)
            dy_intercept_2 = f_scientific_form_dy_intercept(dy_intercept_2, 3)

            session['y_intercept_bfl_2'] = y_intercept_bfl_2
            session['y_intercept_wfl_2'] = y_intercept_wfl_2
            session['dy_intercept_2'] = dy_intercept_2

            return render_template('main.html', y_intercept_bfl_2=y_intercept_bfl_2, dy_intercept_2=dy_intercept_2, bfl_1=session.get('bfl_1'), wfl_1=session.get('wfl_1'), dm_1=session.get('dm_1'))
        
        elif 'submit3' in request.form:
            mbfl_3 = float(request.form['mbfl_3'])
            dm_3 = float(request.form['dm_3'])
            Y_3 = f_Y(mbfl_3)
            dY_3 = f_dY(Y_3, mbfl_3, dm_3)

            Y_3 = f_scientific_form_Y(Y_3, 2)
            dY_3 = f_scientific_form_dY(dY_3, 2)

            session['Y_3'] = Y_3
            session['dY_3'] = dY_3

            return render_template('main.html', Y_3=Y_3, dY_3=dY_3, bfl_1=session.get('bfl_1'), wfl_1=session.get('wfl_1'), dm_1=session.get('dm_1'), y_intercept_bfl_2=session.get('y_intercept_bfl_2'), dy_intercept_2=session.get('dy_intercept_2'))
        
        elif 'submit4' in request.form:
            y_intercept_4 = float(request.form['y_intercept_4'])
            dy_intercept_4 = float(request.form['dy_intercept_4'])
            mbfl_4 = float(request.form['mbfl_4'])
            dm_4 = float(request.form['dm_4'])
            Z_4 = f_Z(y_intercept_4, mbfl_4)
            dZ_4 = f_dZ(y_intercept_4, dy_intercept_4, mbfl_4, dm_4, Z_4)

            Z_4 = f_scientific_form_Z(Z_4, 2)
            dZ_4 = f_scientific_form_dZ(dZ_4, 2)

            session['Z_4'] = Z_4
            session['dZ_4'] = dZ_4

            return render_template('main.html', Z_4=Z_4, dZ_4=dZ_4, Y_3=session['Y_3'], dY_3=session['dY_3'], bfl_1=session.get('bfl_1'), wfl_1=session.get('wfl_1'), dm_1=session.get('dm_1'), y_intercept_bfl_2=session.get('y_intercept_bfl_2'), dy_intercept_2=session.get('dy_intercept_2'))
        
        elif 'submit5' in request.form:
            Y_5 = float(request.form['Y_5'])
            Z_5 = float(request.form['Z_5'])
            temperature = f_temperature(Y_5,Z_5) + 273
            temperature = f_scientific_form_temperature(temperature, 2)

            session['temperature'] = temperature

            return render_template('main.html', temperature=temperature, Z_4 = session['Z_4'], dZ_4 = session['dZ_4'], Y_3=session['Y_3'], dY_3=session['dY_3'], bfl_1=session.get('bfl_1'), wfl_1=session.get('wfl_1'), dm_1=session.get('dm_1'), y_intercept_bfl_2=session.get('y_intercept_bfl_2'), dy_intercept_2=session.get('dy_intercept_2'))
    else:
        return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True, port=8020)