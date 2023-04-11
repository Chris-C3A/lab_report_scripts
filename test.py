import json
import matplotlib.pyplot as plt
import numpy as np
import csv

# bode plot function
def bode_plot(frequencies, gains_dB, color, label, ha, va, log_scale=True):
    # Plot the magnitude response
    if log_scale:
        plt.semilogx(frequencies, gains_dB, color, label=label)
    else:
        plt.plot(frequencies, gains_dB, color, label=label)

    min_dB = np.min(gains_dB)
    max_dB = np.max(gains_dB)

    min_index = np.argmin(gains_dB)
    max_index = np.argmax(gains_dB)

    # min lines
    plt.axhline(y=min_dB, color=color, linestyle='--')
    plt.text(frequencies[min_index], min_dB, str(min_dB) + "dB",
                color=color, ha=ha, va=va)

    # max lines
    plt.axhline(y=max_dB, color=color, linestyle='--')
    plt.text(frequencies[max_index], max_dB, str(max_dB) + "dB",
                color=color, ha=ha, va=va)

# helper function to read csv file
def read_data_from_csv(filename, delimiter):
    frequencies = []
    gains_dB = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            frequencies.append(float(row[0]))
            gains_dB.append(float(row[1]))
    return frequencies, gains_dB

if __name__ == "__main__":
    # open config file
    f = open("config_task7.json", "r")

    # read config file
    config = json.load(f)

    print(config)

    # experimental data 1
    frequencies1, gains_dB1 = read_data_from_csv(config["experimentalDataLocation1"], ',')

    # experimental data 2
    frequencies2, gains_dB2 = read_data_from_csv(config["experimentalDataLocation2"], ',')

    if config["hasSimulationData"]:
        # simulation data 1
        frequencies3, gains_dB3 = read_data_from_csv(config["simulationDataLocation1"], '\t')

        # simulation data 2
        frequencies4, gains_dB4 = read_data_from_csv(config["simulationDataLocation2"], '\t')

    plt.figure(figsize=(10, 6))

    # plot experimental data 1
    bode_plot(frequencies1, gains_dB1, 'b', 'Experimental Data 1', 'left', 'bottom')

    # plot experimental data 2
    bode_plot(frequencies2, gains_dB2, 'b', 'Experimental Data 2', 'left', 'top')

    if config["hasSimulationData"]:
        # plot simulation data 1
        bode_plot(frequencies3, gains_dB3, 'g', 'Simulation Data 1', 'right', 'bottom')

        # plot simulation data 2
        bode_plot(frequencies4, gains_dB4, 'g', 'Simulation Data 2', 'right', 'top')

    # plot settings
    plt.xlabel(config["xlabel"])
    plt.ylabel(config["ylabel"])
    plt.title(config["title"])
    plt.legend()
    plt.grid(True, which="both", ls="-")
    plt.show()
