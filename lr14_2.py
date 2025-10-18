import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(-2, 5, 500)

fig, ax = plt.subplots()
ax.set_xlim(-2, 5)
ax.set_ylim(-6, 6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Анімація графіка y(x) = x * sin(5x)")

line, = ax.plot([], [], 'b-', label='y = x * sin(5x)')
ax.legend()
ax.grid(True)

def update(frame):
    y = x * np.sin(5 * x + 0.1 * frame)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)


plt.show()
