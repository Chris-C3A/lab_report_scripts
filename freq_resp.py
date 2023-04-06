import matplotlib.pyplot as plt
import numpy as np
import csv


def read_data_from_csv(filename, delimiter):
    frequencies = []
    gains_dB = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            frequencies.append(float(row[0]))
            gains_dB.append(float(row[1]))
    return frequencies, gains_dB

def bode_plot(frequencies, gains_dB, amplitude):
    # Convert gains from dB to linear
    gains = np.power(10, np.array(gains_dB) / 20)

    # Plot the magnitude response
    plt.semilogx(frequencies, gains_dB, 'b')
    amplitude_dB = 20*np.log10(amplitude)
    plt.axhline(y=amplitude_dB, color='r', linestyle='--')
    plt.text(frequencies[-1]*10, amplitude_dB, str(amplitude_dB)+" dB",
             color='r', ha='left', va='center')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain (dB)')
    plt.grid(True, which='both')
    plt.title('Bode Plot')
    plt.show()


amplitude = 1

# Vin, Vout = read_data_from_csv('lab2/task3.csv', ',')
# frequencies, gains_dB = read_data_from_csv('lab2/task4.csv', ',')
frequencies, gains_dB = read_data_from_csv('lab2/task7-k=1.csv', ',')

bode_plot(frequencies, gains_dB, amplitude)
