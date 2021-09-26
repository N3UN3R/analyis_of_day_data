import csv
import os
import numpy as np
from matplotlib import pyplot as plt
import ast


def get_day_data(file):
    """ function that returns the python dictionary data
            which contains all needed information of the test data
            for plotting"""

    timestamps = []
    data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        data[timestamp] = {}
        data[timestamp]['totalTradedWatts'] = []
        data[timestamp]['averagePrice'] = []
        data[timestamp]['maximumPrice'] = []
        data[timestamp]['minimumPrice'] = []
        data[timestamp]['runningTime'] = []
        data[timestamp]['numberOfProducers'] = []
        data[timestamp]['numberOfConsumers'] = []
        data[timestamp]['dataPrepTime'] = []
        data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in data.keys():
                if row['timestamp'] == timestamp:
                    data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    data[timestamp]['runningTime'].append(float(row['runningTime']))
                    data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    data[timestamp]['usedReductions'].append(row['usedReductions'])

    return data



def get_timestamps(data):
    """ function that returns a list of all timestamps"""

    timestamps = []
    for timestamp, values in data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))

    return timestamps



def pretty_ticker(timestamps):
    """ create ticker for x-axis on the plot
        returns the list timeForTicker"""

    timeForTicker = []
    for ts in timestamps:
        if ts[3:5] == str('00'):
            timeForTicker.append(ts)
        else:
            timeForTicker.append(None)

    return timeForTicker



def get_usedReductions(data):
    """ function that returns lists with used reductions for each day"""
    nested_konzessionsDifference = []
    nested_netCostDifference = []
    nested_lokalDistance = []
    nested_numberOfPairs = []

    for k, v in data.items():
        ts_konzessionsDifference = []
        ts_netCostDifference = []
        ts_lokalDistance = []
        ts_numberOfPairs = []

        for i in v['usedReductions']:
            usedReductions = ast.literal_eval(i)
            ts_konzessionsDifference.append(usedReductions['konzessionsDifference'])
            ts_netCostDifference.append(usedReductions['netCostDifference'])
            ts_lokalDistance.append(usedReductions['lokalDistance'])
            ts_numberOfPairs.append(usedReductions['numberOfPairs'])

        nested_konzessionsDifference.append(ts_konzessionsDifference[0])
        nested_lokalDistance.append(ts_lokalDistance[0])
        nested_netCostDifference.append(ts_netCostDifference[0])
        nested_numberOfPairs.append(ts_numberOfPairs[0])

    return nested_netCostDifference, nested_numberOfPairs, nested_lokalDistance, nested_konzessionsDifference


def plot_usedReductions(timestamps,timeForTicker,nested_netCostDifference, nested_numberOfPairs, nested_lokalDistance, nested_konzessionsDifference):
    """ function that plots all used reductions using matplotlib"""

    # setup plot
    fig1= plt.figure(1, figsize=(10, 6))
    averageCommunityPrice = fig1.add_subplot()

    # create title
    averageCommunityPrice.set_title('Netzwerk-Simplex: eingesetzte rechtliche Rahmenbedingungen 01. Juli 2020')

    # set axes labels
    averageCommunityPrice.set_xlabel("Uhrzeit")
    averageCommunityPrice.set_ylabel("rechtliche Rahmenbedingungen")
    averageCommunityPrice.set_ylim(0,100)

    # set tickers for x
    averageCommunityPrice.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    averageCommunityPrice.margins(x=0)

    plt.plot(timestamps, nested_numberOfPairs, color = 'green', alpha = 0.7)
    plt.plot(timestamps, nested_lokalDistance, color = 'black', alpha = 0.7)
    plt.plot(timestamps, nested_konzessionsDifference, color = 'red', alpha = 0.7)
    plt.plot(timestamps, nested_netCostDifference, color = 'blue')

    # legend
    #from matplotlib.lines import Line2D
    #legend_elements = [Line2D([0], [0], color='green', label='number of pairs'),
     #                  Line2D([0], [0], color='black', label='local distance'),
      #                 Line2D([0], [0], color='red', label='konzessions difference'),
       #                Line2D([0], [0], color='blue', label='netCost difference')]

    #plt.legend(handles=legend_elements, loc='best')

    fig = plt.gcf()
    fig.set_size_inches(10, 6)

    fig.savefig("netz_usedReductions.svg")
    fig.savefig("netz_usedReductions.pdf")

    plt.show()

    return 0


def main():

    data = get_day_data('01_07.csv')

    nested_netCostDifference, nested_numberOfPairs, nested_lokalDistance, nested_konzessionsDifference = get_usedReductions(
        data)

    timestamps = get_timestamps(data)
    timeForTicker = pretty_ticker(timestamps)

    print(nested_numberOfPairs)

    print("Anzahl der Handelspaare in diesem Intervall")
    print(max(nested_numberOfPairs))

    print("Anzahl lokaler Zusammenhang")
    print(max(nested_lokalDistance))
    print("Anzahl Netzentgeltdifferenzen")
    print(max(nested_netCostDifference))

    print("Anzahl Konzessionsabgabendifferenzen")
    print(max(nested_konzessionsDifference))

    print(plot_usedReductions(timestamps,timeForTicker,nested_netCostDifference, nested_numberOfPairs, nested_lokalDistance, nested_konzessionsDifference))

if __name__ == '__main__':
    main()