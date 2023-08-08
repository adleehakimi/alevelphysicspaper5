from flask import Flask, render_template, redirect, url_for, request
import math
from calculate_gradient import f_gradient_bfl, f_gradient_wfl, f_gradient_change
from calculate_y_intercept import f_y_intercept_bfl, f_y_intercept_wfl, f_dy_intercept
from calculate_Y import f_Y, f_dY
from calculate_Z import f_Z, f_dZ
from calculate_θ import f_temperature
from scientific_notation import f_scientific_form_gradient, f_scientific_form_dm, f_scientific_form_y_intercept, f_scientific_form_dy_intercept, f_scientific_form_Y, f_scientific_form_dY, f_scientific_form_Z, f_scientific_form_dZ, f_scientific_form_temperature, round_to_significant_figures

app = Flask(__name__, template_folder='template')
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

if __name__ == "__main__":
    app.run(debug=True, port=8020)