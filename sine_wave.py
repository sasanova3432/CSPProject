# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()
