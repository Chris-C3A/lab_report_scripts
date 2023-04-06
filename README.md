# EENG10005

## Lab Report Python Scripts

Python scripts to plot experimental and simulation data on the same plot.

## Setup and Configuration

### Requirements
- numpy
- csv
- matplotlib

#### If not already installed
`pip install numpy matplotlib csv`

#### Exporting Experimental Data
Export experimental data from excel as csv file including **only** necessary columns for the plots (frequency, magnitude)

#### Exporting Simulation Data
Export simulation data from simulation graph in awr into a txt file (which will already be formatted in a correct way for you)


> Put these files in the same directory of the python scripts

#### Config File
Edit the config.json file and save
```json
{
  "title": "Magnitude of transfer function in degrees for Op-AMP",
  "xlabel": "Frequency (Hz)",
  "ylabel": "Magnitude (dB)",
  "experimentalDataLocation": "experimentalData.csv",
  "simulationDataLocation": "simulationData.txt",
  "hasSimulationData": true
}
```

#### Run Command

```bash
python freq_res_multiple.py 
```
