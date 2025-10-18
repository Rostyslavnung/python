import math

m = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
a = 0
b = 7
eps = 1e-8

def taylor_series(x, eps):
    n = 0
    term = 1 
    s = term
    while True:
        n += 1
        term = (2 * x) ** n / math.factorial(n)
        s_new = s + term
        if abs(s_new - s) <= eps:
            return s_new, n
        s = s_new

h = (b - a) / (len(m) - 1)
print(f"{'x':>10} | {'f(x) точне':>15} | {'f(x) наближене':>20} | {'похибка':>15} | {'ітерацій':>10}")
print("-" * 80)
for i in range(len(m)):
    x = a + i * h
    exact = math.exp(2 * x)
    approx, iterations = taylor_series(x, eps)
    error = abs(exact - approx)
    print(f"{x:10.5f} | {exact:15.8f} | {approx:20.8f} | {error:15.8e} | {iterations:10d}")


    