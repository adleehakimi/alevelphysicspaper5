import math

def round_to_significant_figures(number, significant_figures):
    if number == 0:
        return 0
    
    magnitude = significant_figures - int(math.floor(math.log10(abs(number)))) - 1
    rounded_number = round(number, magnitude)
    return rounded_number

def convert_to_superscript(number):
    superscript_mapping = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
        '-': '⁻'
    }
    return ''.join(superscript_mapping.get(digit, digit) for digit in str(number))

def f_scientific_form_gradient(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"{mantissa:.2f}x10{convert_to_superscript(exponent)}m³℃⁻¹"
    return value

def f_scientific_form_dm(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"±{mantissa:.2f}x10{convert_to_superscript(exponent)}m³℃⁻¹"
    return value

def f_scientific_form_y_intercept(value, sf):
    value = round_to_significant_figures(value * (10 ** -5), sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"{mantissa:.2f}x10{convert_to_superscript(exponent)}m³"
    return value

def f_scientific_form_dy_intercept(value, sf):
    value = round_to_significant_figures(value * (10 ** -5), sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"±{mantissa:.2f}x10{convert_to_superscript(exponent)}m³"
    return value

def f_scientific_form_Y(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"{mantissa:.2f}x10{convert_to_superscript(exponent)}m³"
    return value

def f_scientific_form_dY(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"±{mantissa:.2f}x10{convert_to_superscript(exponent)}m³"
    return value

def f_scientific_form_Z(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"{mantissa:.2f}x10{convert_to_superscript(exponent)}℃"
    return value

def f_scientific_form_dZ(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"±{mantissa:.2f}x10{convert_to_superscript(exponent)}℃"
    return value

def f_scientific_form_temperature(value, sf):
    value = round_to_significant_figures(value, sf)
    exponent = math.floor(math.log10(abs(value)))
    mantissa = value / 10 ** exponent
    value = f"{mantissa:.2f}x10{convert_to_superscript(exponent)}℃"
    return value