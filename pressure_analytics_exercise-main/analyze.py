#! /usr/bin/env python3

import json
import sys
import csv

def count_contractions(pressure_data):
    """
    Count the number of contractions for a pressure curve
    :param pressure_data: a list of pressure points
    :return: The total number of contractions
    """
    pressure_monitor = 95
    contraction_counter = 0
    for row in pressure_data:
        if row[1] == 'pressure': continue
        if float(row[1]) < pressure_monitor:
            if pressure_monitor == 85:
                pressure_monitor = 95
            continue
        elif float(row[1]) > pressure_monitor:
            if pressure_monitor == 95:
                pressure_monitor = 85
                contraction_counter += 1
            continue
        else: continue

    return contraction_counter-1


def contractions_per_sec(pressure_data, totalContractions):
    """
    Calculate the mean contractions / secs for a pressure curve
    :param pressure_data: a list of pressure points
    :return: The mean frequency of contraction / secs
    """
    total_seconds = pressure_data[len(pressure_data)-1]
    return round(totalContractions/int(int(total_seconds[0])/1000), 2)



def main():
    pressure_file = sys.argv[1]
    results = {}
    with open(sys.argv[1]) as pressure_file:
        csv_reader = csv.reader(pressure_file, delimiter=",")
        data = [row for row in csv_reader]
        results = {
        "pressure_data":[{"ms": d[0], "pressure": d[1]} for d in data if d[0] != "ms"],
        "count_contractions": count_contractions(data),
        "contraction_per_sec": contractions_per_sec(data, count_contractions(data)),
        }
    with open(f'pressure_{pressure_file.name[9]}.json', 'w') as outfile:
        json.dump(results, outfile)

if __name__ == '__main__':
    sys.exit(main())
