import csv
import os
import numpy as np
from matplotlib import pyplot as plt


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


def make_timestamp_dict(data):
    """ function that sorts the python dictionary data using timestamps as keys
               :returns the python dictionary timestamp_dict"""

    timestamp_dict = {}
    for timestamp, intervallData in data.items():
        if timestamp not in timestamp_dict.keys():
            key = timestamp[11:16].replace('_', ':')
            timestamp_dict[key] = {}
            timestamp_dict[key]['runningTimes'] = []
            timestamp_dict[key]['runningTime_mean'] = []
            timestamp_dict[key]['runningTime_standard'] = []
            timestamp_dict[key]['runningTimes'].extend(intervallData['runningTime'])
            timestamp_dict[key]['runningTime_mean'].append(np.mean(intervallData['runningTime']))
            timestamp_dict[key]['runningTime_standard'].append(np.std(intervallData['runningTime']))

    return timestamp_dict


def prep_for_plotting(timestamp_dict):
    """ function that prepares all needed data for plotting
                :returns the lists timestamps, sorted_runningTimes,
                            runningTime_mean, runningTime_standard,
                            plotting_timestamps"""

    timestamps = list(timestamp_dict.keys())
    sorted_runningTimes = []
    runningTime_mean = []
    runningTime_standard = []
    plotting_timestamps = []

    for key, value in timestamp_dict.items():
        sorted_runningTimes.extend(timestamp_dict[key]['runningTimes'])
        runningTime_mean.extend(timestamp_dict[key]['runningTime_mean'])
        runningTime_standard.extend(timestamp_dict[key]['runningTime_standard'])

        for _ in timestamp_dict[key]['runningTimes']:
            plotting_timestamps.append(key)

    return timestamps, sorted_runningTimes, runningTime_mean, runningTime_standard, plotting_timestamps


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



def plot_dev(data,timestamps, sorted_runningTimes, runningTime_mean, runningTime_standard, plotting_timestamps):
    """ function that plots all data using matplotlib"""

    timestamps = np.array(timestamps)
    sorted_runningTimes = np.array(sorted_runningTimes)
    runningTime_mean = np.array(runningTime_mean)
    runningTime_standard = np.array(runningTime_standard)
    plotting_timestamps = np.array(plotting_timestamps)
    timeForTicker = pretty_ticker(timestamps)

    # setup plot
    fig1 = plt.figure(1, figsize=(10, 6))
    averageCommunityPrice = fig1.add_subplot()

    # create title
    averageCommunityPrice.set_title('Simplex: Laufzeit 01. April 2020')
    averageCommunityPrice.set_ylim(0, 1)

    # set axes labels
    averageCommunityPrice.set_xlabel("Uhrzeit")
    averageCommunityPrice.set_ylabel("Laufzeit [s] ")

    # set tickers for x
    averageCommunityPrice.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    averageCommunityPrice.margins(x=0)

    #plot the data
    plt.scatter(plotting_timestamps, sorted_runningTimes, color='blue', alpha=0.08, marker='.', edgecolors=None,
                rasterized=True, label='scatter plt')
    plt.plot(timestamps, runningTime_mean, color='red', label='mean')

    # second axis
    par2 = averageCommunityPrice.twinx()
    par2.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    par2.set_ylabel("Standardabweichung [s] ", color='green')
    par2.set_ylim(0, 0.05)
    par2.plot(timestamps, runningTime_standard, color='green', label='Standardabweichung')

    fig = plt.gcf()
    fig.set_size_inches(10, 6)

    # saving as svg graphic
    #fig.savefig("0101simplex_runtime_deviation_scalable.svg")
    fig.savefig("0104simplex_runtime_deviation_scalable.pdf")

    # legende
   # from matplotlib.lines import Line2D
   # legend_elements = [Line2D([0], [0], color='red', label='average runtime'),
     #                  Line2D([0], [0], color='green', label='standard deviation'),
    #                   Line2D([0], [0], marker='o', color='w', label='data points',
      #                        markerfacecolor='blue', markersize=5)]

    #plt.legend(handles=legend_elements, loc='best')

   # fig = plt.gcf()
    #fig.set_size_inches(8, 5)

    plt.show()

    return 0


def main():

    file = '01_04.csv'

    data = get_day_data(file)

    timestamp_dict = make_timestamp_dict(data)

    timestamps, sorted_runningTimes, runningTime_mean, runningTime_standard, plotting_timestamps = prep_for_plotting(
        timestamp_dict)

    runtime_and_deviation =  plot_dev(data,timestamps, sorted_runningTimes, runningTime_mean, runningTime_standard, plotting_timestamps)

    print(runtime_and_deviation)

if __name__ == '__main__':
    main()