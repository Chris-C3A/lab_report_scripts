import json
import matplotlib.pyplot as plt
import numpy as np
import csv


# globals
# title = 'Magnitude of transfer function in degrees for Op-AMP' # other titles: Magnitude of transfer function in dB for RC parallel circuit
# xlabel = 'Frequency (Hz)' # for freqresp: Frequency (Hz)
# ylabel = 'Magnitude (dB)' # for freqresp: Magnitude (dB)
# hasSimulationData = True

# experimentalData = 'lab2/task4.csv' # other data: lab2/task4.csv, lab2/task7-k=1.csv
# simulationData = 'lab2/simulation_data/task4.txt' # other data: RLC_series.txt

# bode plot function
def bode_plot(frequencies, gains_dB, color, label, ha, va, log_scale=True):
    # Plot the magnitude response
    if log_scale:
        # plt.semilogx(frequencies, list(map(abs, gains_dB)), color, label=label)
        plt.semilogx(frequencies, gains_dB, color, label=label)
    else:
        plt.plot(frequencies, gains_dB, color, label=label)

    min_dB = np.min(gains_dB)
    max_dB = np.max(gains_dB)

    min_index = np.argmin(gains_dB)
    max_index = np.argmax(gains_dB)

    # min lines
    plt.axhline(y=min_dB, color=color, linestyle='--')
    plt.text(frequencies[min_index], min_dB, str(min_dB) + "dB", # change unit here
                color=color, ha=ha, va=va)

    # max lines
    plt.axhline(y=max_dB, color=color, linestyle='--')
    plt.text(frequencies[max_index], max_dB, str(max_dB) + "dB", # change unit here
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
    f = open("config.json", "r")
    # f = open("config_task7-k0.json", "r")

    # read config file 
    config = json.load(f)

    print(config)

    # experimental data
    frequencies1, gains_dB1 = read_data_from_csv(config["experimentalDataLocation"], ',')

    if config["hasSimulationData"]:
        # simulation data
        frequencies2, gains_dB2 = read_data_from_csv(config["simulationDataLocation"], '\t')

        # if needed conversion uncomment this
        # frequencies2 = [x*1000 for x in frequencies2] # convert frequencies to Hz

    plt.figure(figsize=(10, 6))

    # plot experimental data
    bode_plot(frequencies1, gains_dB1, 'b', 'Experimental Plot', 'left', 'bottom')

    if config["hasSimulationData"]:
        # plot simulation data
        bode_plot(frequencies2, gains_dB2, 'g', 'Simulation Plot', 'right', 'top')

    # plot settings
    plt.xlabel(config["xlabel"])
    plt.ylabel(config["ylabel"])
    plt.grid(True, which='both')
    plt.legend()
    plt.title(config["title"])

    plt.show()