import math

x = float(input("Enter x: "))

z = pow((math.exp(-x)-12.34)/(math.log10(x)-math.cos(x**3)) , -0.5)

print("z =", z)