import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt
import os

def generate_signal(n, F_max, Fs, F_filter):
    random_signal = np.random.normal(0, 10, n)
    time_values = np.arange(n) / Fs
    w = F_filter / (Fs / 2)
    filter_params = signal.butter(3, w, 'low', output='sos')
    filtered_signal = signal.sosfiltfilt(filter_params, random_signal)
    return time_values, filtered_signal

def discretize_signal(signal, Dt):
    n = len(signal)
    discrete_signal = np.zeros(n)
    for i in range(0, round(n/Dt)):
        discrete_signal[i * Dt] = signal[i * Dt]
    return discrete_signal

def restore_analog_signal(discrete_signal, Fs, F_filter):
    w = F_filter / (Fs / 2)
    filter_params = signal.butter(3, w, 'low', output='sos')
    restored_signal = signal.sosfiltfilt(filter_params, discrete_signal)
    return restored_signal

if not os.path.exists("figures"):
    os.makedirs("figures")

if __name__ == "__main__":
    n = 500
    F_max = 23
    Fs = 1000
    F_filter = 30

    time_values, filtered_signal = generate_signal(n, F_max, Fs, F_filter)

    # Дискретизація сигналу з різними кроками
    Dt_values = [2, 4, 8, 16]
    discrete_signals = []
    discrete_spectrums = []
    variances = []
    snr_ratios = []

    for Dt in Dt_values:
        discrete_signal = discretize_signal(filtered_signal, Dt)
        discrete_signals.append(list(discrete_signal))

        # Розрахунок спектру
        spectrum = fft.fftshift(fft.fft(discrete_signal))
        frequencies = fft.fftshift(fft.fftfreq(len(spectrum), d=1/Fs))
        discrete_spectrums += [list(spectrum)]

        # Відновлення аналогового сигналу
        restored_signal = restore_analog_signal(discrete_signal, Fs, F_filter)

        # Розрахунок різниці та дисперсій
        E1 = restored_signal - filtered_signal
        variance_signal = np.var(filtered_signal)
        variance_difference = np.var(E1)
        variances.append(variance_difference)

        # Розрахунок співвідношення сигнал-шум
        snr_ratio = variance_signal / variance_difference
        snr_ratios.append(snr_ratio)

    # Відображення результатів дискретизації та спектрів
    fig, ax = plt.subplots(2, 2, figsize=(21/2.54, 14/2.54))
    s = 0
    for i in range(2):
        for j in range(2):
            ax[i][j].plot(time_values, discrete_signals[s], linewidth=1)
            s += 1

    fig.suptitle("Сигнал та його дискретизації", fontsize=14)
    fig.supxlabel("Час", fontsize=14)
    fig.supylabel("Амплітуда сигналу", fontsize=14)

    # Збереження зображення
    plt.savefig("./figures/Дискретизовані сигнали.png", dpi=600)

    # Показати графіки
    plt.show()

    # Відображення результатів спектрів
    fig, ax = plt.subplots(2, 2, figsize=(21/2.54, 14/2.54))
    s = 0
    for i in range(2):
        for j in range(2):
            ax[i][j].plot(frequencies, np.abs(discrete_spectrums[s]), linewidth=1)
            s += 1

    fig.suptitle("Спектр дискретизованих сигналів", fontsize=14)
    fig.supxlabel("Частота (Гц)", fontsize=14)
    fig.supylabel("Амплітуда спектру", fontsize=14)

    # Збереження зображення
    plt.savefig("./figures/Дискретні спектри.png", dpi=600)

    # Показати графіки
    plt.show()

    # Відновлення аналогового сигналу та відображення результатів
    fig, ax = plt.subplots(2, 2, figsize=(21/2.54, 14/2.54))
    s = 0
    for i in range(2):
        for j in range(2):
            restored_signal = restore_analog_signal(discrete_signals[s], Fs, F_filter)
            ax[i][j].plot(time_values, restored_signal, linewidth=1)
            s += 1

    fig.suptitle("Відновлений аналоговий сигнал", fontsize=14)
    fig.supxlabel("Час", fontsize=14)
    fig.supylabel("Амплітуда сигналу", fontsize=14)

    # Збереження зображення
    plt.savefig("./figures/Відновлені сигнали.png", dpi=600)

    # Показати графіки
    plt.show()

    # Відображення результатів відновлення та розрахунку дисперсій
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(Dt_values, variances, marker='o', color='b', label='Дисперсія різниці')
    ax1.set_xlabel('Крок дискретизації')
    ax1.set_ylabel('Дисперсія', color='b')
    ax1.tick_params('y', colors='b')
    ax1.set_xscale('log', base=2)

    plt.title("Залежність дисперсії різниці від кроку дискретизації")

    # Збереження графіку
    plt.savefig("figures/Різниця дисперсії.png", dpi=600)

    # Показати графік
    plt.show()

    # Відображення результатів співвідношення сигнал-шум
    fig, ax1 = plt.subplots(figsize=(10, 6))

    ax1.plot(Dt_values, snr_ratios, marker='o', color='r', label='Співвідношення сигнал-шум')
    ax1.set_xlabel('Крок дискретизації')
    ax1.set_ylabel('Співвідношення сигнал-шум', color='r')
    ax1.tick_params('y', colors='r')
    ax1.set_xscale('log', base=2)

    plt.title("Залежність співвідношення сигнал-шум від кроку дискретизації")

    # Збереження графіку
    plt.savefig("figures/Коефіціент шуму.png", dpi=600)

    # Показати графік
    plt.show()