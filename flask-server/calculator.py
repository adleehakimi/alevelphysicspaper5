#Inputting 4 coordinates
x_1 = float(input("Enter first X-coordinate: "))
y_1 = float(input("Enter first y coordinate: "))
print(f"({x_1}, {y_1})")
x_2 = float(input("Enter second x-coordinate: "))
y_2 = float(input("Enter second y-coordinate: "))
print(f"({x_1}, {y_1})")

x_3 = float(input("Enter third X-coordinate: "))
y_3 = float(input("Enter third y coordinate: "))
print(f"({x_1}, {y_1})")
x_4 = float(input("Enter fourth x-coordinate: "))
y_4 = float(input("Enter fourth y-coordinate: "))
print(f"({x_1}, {y_1})")

#!! Change formulas into functions and make input as arguments
#Gradient formula 

def f_gradient_bfl(x_1, y_1, x_2, y_2):
    gradient_bfl = (y_2 - y_1) / (x_2 - x_1)
    return gradient_bfl

def f_gradient_wfl(x_3, y_3, x_4, y_4):
    gradient_wfl = (y_3 - y_4) / (x_3 - x_4)
    return gradient_wfl

def f_gradient_change(gradient_bfl, gradient_wfl):
    gradient_change = abs(gradient_bfl - gradient_wfl)
    return gradient_change

#y-intercept formula
y_intercept_best = y_1 - gradient_bfl * x_1
y_intercept_worst = y_3 - gradient_wfl * x_3
y_intercept_change = abs(y_intercept_best - y_intercept_worst)

print(f"y-intercept =  {y_intercept_best}")
print(f"y-intercept (worst) =  {y_intercept_worst}")
print(f"Change in y-intercept =  {y_intercept_change}")

#Finding Y
p = 1.01 * (10 ** 5)
k = 1.38 * (10 ** -23)
p_uncertainty = 0.01
gradient = float(input("Gradient = "))
gradient_uncertainty = float(input("Gradient Uncertainty = "))

Y = (gradient * p) /k
Y_uncertainty = (((p_uncertainty/p) + (gradient_uncertainty/gradient))/100) * Y

print(f"Y = {Y}")
print(f"Y Uncertainty = +-{Y_uncertainty}")

#Finding Z
p = 1.01 * (10 ** 5)
k = 1.38 * (10 ** -23)

y_intercept = float(input("y-intercept = "))
y_intercept_uncertainty = float(input("y-intercept uncertainty = "))
gradient = float(input("gradient = "))
gradient_uncertainty = float(input("graident uncertainty = "))

Z = y_intercept/gradient
Z_uncertainty = (((y_intercept_uncertainty/y_intercept) + (gradient_uncertainty/gradient))/100) * Z

print(f"Z = {Z}")
print(f"Z Uncertainty = +-{Z_uncertainty}")

#Finding Temp
p = 1.01 * (10 ** 5)
p_uncertainty = 0.01
k = 1.38 * (10 ** -23)
d = 0.0279
d_uncertainty = 0.0001
h = 0.06
V = (3.142 * (d**2) * h) / 4

Y = float(input("Y = "))
Z = float(input("Z = "))

temperature = ((p * V) / (Y * k)) - Z
