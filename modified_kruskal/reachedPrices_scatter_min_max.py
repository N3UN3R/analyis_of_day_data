import csv
import ast
import json
from matplotlib import pyplot as plt
import numpy as np


def get_day_data(file):
    timestamps = []
    data = {}

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['timestamp'] not in timestamps:
                timestamps.append(row['timestamp'])

    for timestamp in timestamps:
        data[timestamp] = {}
        data[timestamp]['tradedAmounts'] = []
        data[timestamp]['maximumPrice'] = []
        data[timestamp]['minimumPrice'] = []
        data[timestamp]['averagePrice'] = []

    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            for timestamp in data.keys():
                if row['timestamp'] == timestamp:
                    data[timestamp]['tradedAmounts'].append(row['tradedAmounts'])
                    data[timestamp]['maximumPrice'].append(float(row['maximumPrice']))
                    data[timestamp]['minimumPrice'].append(float(row['minimumPrice']))
                    data[timestamp]['averagePrice'].append(float(row['averagePrice']))

    return data


def new_try(data):

    with open('new_tradingCost_prosumers_to_all_households_tuples.json', 'r') as f:
        temp = json.load(f)
        tradingCosts = ast.literal_eval(temp)

    timestamp_dict = {}

    for timestamp, intervallData in data.items():
        if timestamp not in timestamp_dict.keys():
            key = timestamp[11:16].replace('_', ':')
            timestamp_dict[key] = {}
           # timestamp_dict[key][reachedPrice_mean] = []
            timestamp_dict[key]['max_reachedPrice'] = []
            timestamp_dict[key]['min_reachedPrice'] = []
           # timestamp_dict[key]['trading_prices'] = []
            timestamp_dict[key]['reachedPrice_mean'] = []

            """min und max price sind done"""
            timestamp_dict[key]['max_reachedPrice'].append(intervallData['maximumPrice'][0])
            timestamp_dict[key]['min_reachedPrice'].append(intervallData['minimumPrice'][0])
            timestamp_dict[key]['reachedPrice_mean'].append(intervallData['averagePrice'][0])

            tradingPairs = ast.literal_eval(intervallData['tradedAmounts'][0])

            trading_prices = []
            for matchedhouseholds in tradingPairs.keys():
                trading_prices.append(tradingCosts[matchedhouseholds])

            timestamp_dict[key]['trading_prices'] = trading_prices


    return timestamp_dict


def prep_for_plotting(timestamp_dict):
    timestamps = list(timestamp_dict.keys())

    sorted_trading_prices = []
    sorted_max_reachedPrice = []
    sorted_min_reachedPrice = []
    sorted_reachedPrice_mean = []
    plotting_timestamps = []


    for key,value in timestamp_dict.items():
        sorted_max_reachedPrice.extend(timestamp_dict[key]['max_reachedPrice'])
        sorted_min_reachedPrice.extend(timestamp_dict[key]['min_reachedPrice'])
        sorted_reachedPrice_mean.extend(timestamp_dict[key]['reachedPrice_mean'])

        sorted_trading_prices.extend(timestamp_dict[key]['trading_prices'])

        for _ in timestamp_dict[key]['trading_prices']:
            plotting_timestamps.append(key)

    return timestamps, sorted_trading_prices, sorted_max_reachedPrice, sorted_min_reachedPrice, sorted_reachedPrice_mean, plotting_timestamps


def pretty_ticker(timestamps):
    """ create good time intervalls on x-axis"""
    timeForTicker = []
    for ts in timestamps:
        if ts[3:5] == str('00'):
            timeForTicker.append(ts)
        else:
            timeForTicker.append(None)

    return timeForTicker



# ----------------plot the data--------------------------------------

def plot_runtime_scatter(timestamps,timeForTicker, sorted_trading_prices, sorted_max_reachedPrice, sorted_min_reachedPrice,
                         sorted_reachedPrice_mean, plotting_timestamps):



    timestamps = np.array(timestamps)
    tradingPrices = np.array(sorted_trading_prices)
    max_reachedPrice = np.array(sorted_max_reachedPrice)
    min_reachedPrice = np.array(sorted_min_reachedPrice)
    reachedPrice_mean = np.array(sorted_reachedPrice_mean)
    plotting_timestamps = np.array(plotting_timestamps)

    print(timestamps.shape)
    print(tradingPrices.shape)
    print(max_reachedPrice.shape)
    print(min_reachedPrice.shape)
    print(reachedPrice_mean.shape)
    print(plotting_timestamps.shape)


    # setup plot
    fig1= plt.figure(1, figsize=(10, 6))
    averageCommunityPrice = fig1.add_subplot()

    # create title
    averageCommunityPrice.set_title('mod. Kruskal: Preisverteilung 01. Juli 2020')
    averageCommunityPrice.set_ylim(18, 27)

    # set axes labels
    averageCommunityPrice.set_xlabel("Uhrzeit")
    averageCommunityPrice.set_ylabel("Erreichter Strompreis [ct]")

    # set tickers for x
    averageCommunityPrice.set_xticklabels(timeForTicker, fontsize=10, rotation=45)
    averageCommunityPrice.margins(x=0)





    #plt.plot(timestamps, tradingPrices, ".", color='blue', alpha=0.08)
    plt.scatter(plotting_timestamps, tradingPrices, marker='.',color='blue',alpha=0.08, edgecolors=None,
                rasterized=True)
    plt.plot(timestamps, min_reachedPrice,'r-', color = 'green', alpha = 0.8)
    plt.plot(timestamps, max_reachedPrice,'r-', color = 'black', alpha = 0.8)
    plt.plot(timestamps, reachedPrice_mean,'r-', color = 'red', alpha = 0.8)

    # legende
   # from matplotlib.lines import Line2D
   # legend_elements = [Line2D([0], [0], color='black', label='highest price'),
     #                  Line2D([0], [0], color='green', label='lowest price'),
    #                   Line2D([0], [0], color='red', label='average price'),
      #                 Line2D([0], [0], marker='o', color='blue', label='data points',
       #                       markerfacecolor='blue', markersize=5)]

    #plt.legend(handles=legend_elements, loc='best')

    fig = plt.gcf()
    fig.set_size_inches(10, 6)

    # saving as svg graphic
#    fig.savefig("kruskal_runtime_deviation.svg")
    fig.savefig("falsch_01_07kruskal_runtime_deviation.pdf")

    plt.show()

    return 0



def main():


    file = 'falsch_01_07.csv'

    data = get_day_data(file)

    timestamp_dict = new_try(data)

    timestamps, sorted_trading_prices, sorted_max_reachedPrice, sorted_min_reachedPrice, sorted_reachedPrice_mean, plotting_timestamps = prep_for_plotting(timestamp_dict)

    timeForTicker = pretty_ticker(timestamps)


    abbildung = plot_runtime_scatter(timestamps,timeForTicker, sorted_trading_prices, sorted_max_reachedPrice, sorted_min_reachedPrice,
                         sorted_reachedPrice_mean, plotting_timestamps)

    print(abbildung)



if __name__ == '__main__':
    main()

