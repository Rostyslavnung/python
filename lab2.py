import math
step = 0.6
while True:
     try:
         x = float(input("Enter x (3.8 <= x <= 7.6): "))
         if 3.8 <= x <= 7.6:
             break
         else:
             print("x must be in the range [3.8, 7.6]. Please try again.")
     except ValueError:
         print("Invalid input. Please enter a numeric value.")
while 3.8 <= x <= 7.6:
    y = (math.cos(x)**2)/(x**2 + 1)
    print("x =", x, "y =", y)
    x += step
