import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 5, 500)
y = x * np.sin(5 * x)

plt.plot(x, y, 'b-', label='y = x * sin(5x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y(x) = x * sin(5x)')
plt.legend()
plt.grid(True)

plt.savefig("function_plot.png", dpi=300)
plt.show()
