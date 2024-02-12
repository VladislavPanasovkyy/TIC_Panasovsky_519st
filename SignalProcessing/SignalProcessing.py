import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt

def generate_signal(n, F_max, Fs):
    random_signal = np.random.normal(0, 10, n)
    time_values = np.arange(n) / Fs
    w = F_max / (Fs / 2)
    filter_params = signal.butter(3, w, 'low', output='sos')
    filtered_signal = signal.sosfiltfilt(filter_params, random_signal)
    return time_values, filtered_signal

def plot_signal(x, y, title):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(x, y, linewidth=1)
    ax.set_xlabel("Час", fontsize=14)
    ax.set_ylabel("Значення сигналу", fontsize=14)
    plt.title(title, fontsize=14)
    plt.savefig(f"./figures/{title}.png", dpi=600)

def plot_spectrum(x, y, title):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(x, y, linewidth=1)
    ax.set_xlabel("Частота (Гц)", fontsize=14)
    ax.set_ylabel("Амплітуда", fontsize=14)
    plt.title(title, fontsize=14)
    plt.savefig(f"./figures/{title}.png", dpi=600)

if __name__ == "__main__":
    n = 500
    F_max = 23
    Fs = 1000

    time_values, filtered_signal = generate_signal(n, F_max, Fs)

    # Розрахунок спектру
    spectrum = fft.fftshift(fft.fft(filtered_signal))
    freqs = fft.fftshift(fft.fftfreq(n, 1/Fs))

    # Побудова графіків
    plot_signal(time_values, filtered_signal, "Відфільтрований сигнал")
    plot_spectrum(freqs, np.abs(spectrum), "Спектр")