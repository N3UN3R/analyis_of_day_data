import csv
import os
import numpy as np
from matplotlib import pyplot as plt


#------------------ get result data of kruskal ----------------------
def get_day_data_kruskal(file):
    """ function that gets all data of the kruskal results
        :returns a python dictionary called kruskal_data"""
    timestamps = []
    kruskal_data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        kruskal_data[timestamp] = {}
        kruskal_data[timestamp]['totalTradedWatts'] = []
        kruskal_data[timestamp]['averagePrice'] = []
        kruskal_data[timestamp]['maximumPrice'] = []
        kruskal_data[timestamp]['minimumPrice'] = []
        kruskal_data[timestamp]['runningTime'] = []
        kruskal_data[timestamp]['numberOfProducers'] = []
        kruskal_data[timestamp]['numberOfConsumers'] = []
        kruskal_data[timestamp]['dataPrepTime'] = []
        kruskal_data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in kruskal_data.keys():
                if row['timestamp'] == timestamp:
                    kruskal_data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    kruskal_data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    kruskal_data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    kruskal_data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    kruskal_data[timestamp]['runningTime'].append(float(row['runningTime']))
                    kruskal_data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    kruskal_data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    kruskal_data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    kruskal_data[timestamp]['usedReductions'].append(row['usedReductions'])

    return kruskal_data


def get_allData_kruskal(kruskal_data):
    """ function that prepares all test data of the kruskal algorithm
        for plotting the data
        :returns 3 lists"""
    timestamps = []
    kruskal_runningTime_mean = []
    numberOfProducers = []
    kruskal_reachedPrice_mean = []

    for timestamp, values in kruskal_data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))
        #get mean of number of producers
        numberOfProducers.append(np.mean(values['numberOfProducers']))
        # get a list of the means of runningTimes
        kruskal_runningTime_mean.append(np.mean(values['runningTime']))
        #get a list of the means of the reached price
        kruskal_reachedPrice_mean.append(np.mean(values['averagePrice']))

    return timestamps, kruskal_runningTime_mean, numberOfProducers, kruskal_reachedPrice_mean


#------------------ get result data of network ----------------------
def get_day_data_network(file):
    """ function that gets all data of the network simplex results
            :returns a python dictionary called network_data"""
    timestamps = []
    network_data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        network_data[timestamp] = {}
        network_data[timestamp]['totalTradedWatts'] = []
        network_data[timestamp]['averagePrice'] = []
        network_data[timestamp]['maximumPrice'] = []
        network_data[timestamp]['minimumPrice'] = []
        network_data[timestamp]['runningTime'] = []
        network_data[timestamp]['numberOfProducers'] = []
        network_data[timestamp]['numberOfConsumers'] = []
        network_data[timestamp]['dataPrepTime'] = []
        network_data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in network_data.keys():
                if row['timestamp'] == timestamp:
                    network_data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    network_data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    network_data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    network_data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    network_data[timestamp]['runningTime'].append(float(row['runningTime']))
                    network_data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    network_data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    network_data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    network_data[timestamp]['usedReductions'].append(row['usedReductions'])

    return network_data


def get_allData_network(network_data):
    """ function that prepares all test data of the network simplex algorithm
        for plotting the data
        :returns 3 lists"""

    timestamps = []
    network_runningTime_mean = []
    numberOfProducers = []
    network_reachedPrice_mean = []

    for timestamp, values in network_data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))
        #get mean of number of producers
        numberOfProducers.append(np.mean(values['numberOfProducers']))
        # get a list of the means of runningTimes
        network_runningTime_mean.append(np.mean(values['runningTime']))
        #get a list of the means of the reached price
        network_reachedPrice_mean.append(np.mean(values['averagePrice']))

    return timestamps, network_runningTime_mean, numberOfProducers, network_reachedPrice_mean


#---------------get result data of simplex data ----------------------------------
def get_day_data_simplex(file):
    """ function that gets all data of the simplex results
        :returns a python dictionary called simplex_data"""

    timestamps = []
    simplex_data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        simplex_data[timestamp] = {}
        simplex_data[timestamp]['totalTradedWatts'] = []
        simplex_data[timestamp]['averagePrice'] = []
        simplex_data[timestamp]['maximumPrice'] = []
        simplex_data[timestamp]['minimumPrice'] = []
        simplex_data[timestamp]['runningTime'] = []
        simplex_data[timestamp]['numberOfProducers'] = []
        simplex_data[timestamp]['numberOfConsumers'] = []
        simplex_data[timestamp]['dataPrepTime'] = []
        simplex_data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in simplex_data.keys():
                if row['timestamp'] == timestamp:
                    simplex_data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    simplex_data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    simplex_data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    simplex_data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    simplex_data[timestamp]['runningTime'].append(float(row['runningTime']))
                    simplex_data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    simplex_data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    simplex_data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    simplex_data[timestamp]['usedReductions'].append(row['usedReductions'])

    return simplex_data


def get_allData_simplex(simplex_data):
    """ function that prepares all test data of the simplex algorithm
        for plotting the data
        :returns 3 lists"""

    timestamps = []
    simplex_runningTime_mean = []
    numberOfProducers = []
    simplex_reachedPrice_mean = []

    for timestamp, values in simplex_data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))
        #get mean of number of producers
        numberOfProducers.append(np.mean(values['numberOfProducers']))
        # get a list of the means of runningTimes
        simplex_runningTime_mean.append(np.mean(values['runningTime']))
        #get a list of the means of the reached price
        simplex_reachedPrice_mean.append(np.mean(values['averagePrice']))

    return timestamps, simplex_runningTime_mean, numberOfProducers, simplex_reachedPrice_mean


#---------------get result data of revised data ----------------------------------
def get_day_data_revised(file):
    """ function that gets all data of the revised simplex results
            :returns a python dictionary called revised_data"""
    timestamps = []
    revised_data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        revised_data[timestamp] = {}
        revised_data[timestamp]['totalTradedWatts'] = []
        revised_data[timestamp]['averagePrice'] = []
        revised_data[timestamp]['maximumPrice'] = []
        revised_data[timestamp]['minimumPrice'] = []
        revised_data[timestamp]['runningTime'] = []
        revised_data[timestamp]['numberOfProducers'] = []
        revised_data[timestamp]['numberOfConsumers'] = []
        revised_data[timestamp]['dataPrepTime'] = []
        revised_data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in revised_data.keys():
                if row['timestamp'] == timestamp:
                    revised_data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    revised_data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    revised_data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    revised_data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    revised_data[timestamp]['runningTime'].append(float(row['runningTime']))
                    revised_data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    revised_data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    revised_data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    revised_data[timestamp]['usedReductions'].append(row['usedReductions'])

    return revised_data


def get_allData_revised(revised_data):
    """ function that prepares all test data of the revised simplex algorithm
        for plotting the data
        :returns 3 lists"""

    timestamps = []
    revised_runningTime_mean = []
    numberOfProducers = []
    revised_reachedPrice_mean = []

    for timestamp, values in revised_data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))
        #get mean of number of producers
        numberOfProducers.append(np.mean(values['numberOfProducers']))
        # get a list of the means of runningTimes
        revised_runningTime_mean.append(np.mean(values['runningTime']))
        #get a list of the means of the reached price
        revised_reachedPrice_mean.append(np.mean(values['averagePrice']))

    return timestamps, revised_runningTime_mean, numberOfProducers, revised_reachedPrice_mean


#---------------get result data of revised data ----------------------------------
def get_day_data_interior(file):
    """ function that gets all data of the interior point method results
        :returns a python dictionary called interior_data"""
    timestamps = []
    interior_data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        interior_data[timestamp] = {}
        interior_data[timestamp]['totalTradedWatts'] = []
        interior_data[timestamp]['averagePrice'] = []
        interior_data[timestamp]['maximumPrice'] = []
        interior_data[timestamp]['minimumPrice'] = []
        interior_data[timestamp]['runningTime'] = []
        interior_data[timestamp]['numberOfProducers'] = []
        interior_data[timestamp]['numberOfConsumers'] = []
        interior_data[timestamp]['dataPrepTime'] = []
        interior_data[timestamp]['usedReductions'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in interior_data.keys():
                if row['timestamp'] == timestamp:
                    interior_data[timestamp]['totalTradedWatts'].append(float(row['totalTradedWatts']))
                    interior_data[timestamp]['averagePrice'].append(float(row['averagePrice']))
                    interior_data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    interior_data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    interior_data[timestamp]['runningTime'].append(float(row['runningTime']))
                    interior_data[timestamp]['dataPrepTime'].append(float(row['dataPrepTime']))
                    interior_data[timestamp]['numberOfProducers'].append(float(row['numberOfProducers']))
                    interior_data[timestamp]['numberOfConsumers'].append(float(row['numberOfConsumers']))
                    interior_data[timestamp]['usedReductions'].append(row['usedReductions'])

    return interior_data


def get_allData_interior(interior_data):
    """ function that prepares all test data of the interior point method
        for plotting the data
        :returns 3 lists"""

    timestamps = []
    interior_runningTime_mean = []
    numberOfProducers = []
    interior_reachedPrice_mean = []

    for timestamp, values in interior_data.items():
        # add timestamp to timestamp list
        timestamps.append(timestamp[11:16].replace('_', ':'))
        #get mean of number of producers
        numberOfProducers.append(np.mean(values['numberOfProducers']))
        # get a list of the means of runningTimes
        interior_runningTime_mean.append(np.mean(values['runningTime']))
        #get a list of the means of the reached price
        interior_reachedPrice_mean.append(np.mean(values['averagePrice']))

    return timestamps, interior_runningTime_mean, numberOfProducers, interior_reachedPrice_mean


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


def plot_runtimes(timestamps, numberOfProducers, network_runningTime_mean, kruskal_runningTime_mean, revised_runningTime_mean,
                  interior_runningTime_mean,simplex_runningTime_mean ):
    """ function that plots the runtime of all algorithms using matplotlib"""

    timeForTicker = pretty_ticker(timestamps)

    # setup plot
    fig1 = plt.figure(1, figsize=(10, 6))
    averageCommunityPrice = fig1.add_subplot()

    # create title
    #averageCommunityPrice.set_title('Laufzeiten 01. Juli 2020')
    averageCommunityPrice.set_ylim(0, 1)

    # set axes labels
    averageCommunityPrice.set_xlabel("Uhrzeit")
    averageCommunityPrice.set_ylabel("Laufzeit [s] ")

    # set tickers for x
    averageCommunityPrice.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    averageCommunityPrice.margins(x=0)

    plt.plot(timestamps, network_runningTime_mean, color='blue')
    #plt.plot(timestamps, runningTime_mean, color='red', label='mean')
    plt.plot(timestamps, kruskal_runningTime_mean, color = 'red')

    plt.plot(timestamps, revised_runningTime_mean, color = 'orange')
    plt.plot(timestamps, interior_runningTime_mean, color = 'black')
    plt.plot(timestamps, simplex_runningTime_mean, color = 'pink')

    # second axis
    par2 = averageCommunityPrice.twinx()
    par2.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    par2.set_ylabel("Anzahl an Producer-Haushalten", color='green')
    par2.set_ylim(0, 16)
    par2.plot(timestamps, numberOfProducers, color='green')

    # legende
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color='blue', label='Netzwerk-Simplex'),
                       Line2D([0], [0], color='red', label='modifiz. Kruskal'),
                       Line2D([0], [0], color='orange', label='revidierter Simplex'),
                       Line2D([0], [0], color='black', label='Innere-Punkte-Methode'),
                       Line2D([0], [0], color='pink', label='Simplex Algorithmus'),
                       Line2D([0], [0], color='green', label='Anzahl an Producer-Haushalten')
                       ]

    plt.legend(handles=legend_elements, loc='best')

    fig = plt.gcf()

    # saving as svg graphic
    fig.savefig("allRuntimes_scalable.pdf")
    fig.savefig("allRuntimes_scalable.svg")

    plt.show()

    return 0

def main():

    kruskal_data = get_day_data_kruskal('kruskal_01_07_nurReduzierung.csv')
    network_data = get_day_data_network('netzwerk_01_07_nurReduzierung.csv')
    simplex_data = get_day_data_simplex('simplex_01_07_nurReduzierung.csv')
    revised_data = get_day_data_revised('revised_01_07_nurReduzierung.csv')
    interior_data = get_day_data_interior('interior_01_07_nurReduzierung.csv')


    timestamps, network_runningTime_mean, numberOfProducers, network_reachedPrice_mean = get_allData_network(network_data)
    timestamps, kruskal_runningTime_mean, numberOfProducers, kruskal_reachedPrice_mean = get_allData_kruskal(kruskal_data)
    timestamps, simplex_runningTime_mean, numberOfProducers, simplex_reachedPrice_mean = get_allData_simplex(simplex_data)
    timestamps, revised_runningTime_mean, numberOfProducers, revised_reachedPrice_mean = get_allData_revised(revised_data)
    timestamps, interior_runningTime_mean, numberOfProducers, interior_reachedPrice_mean = get_allData_interior(interior_data)


    abbildung = plot_runtimes(timestamps, numberOfProducers, network_runningTime_mean, kruskal_runningTime_mean,
                              revised_runningTime_mean, interior_runningTime_mean, simplex_runningTime_mean)

    print(abbildung)

if __name__ == '__main__':
    main()