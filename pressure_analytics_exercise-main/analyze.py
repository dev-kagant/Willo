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
    # FIXME
    pressure_monitor = 95
    contraction_counter = 0
    for row in pressure_data:
        if row[1] == 'pressure': continue
        if float(row[1]) > float(pressure_monitor):
            if pressure_monitor == 85:
                pressure_monitor = 95
                contraction_counter += 1
            continue
        if float(row[1]) < pressure_monitor:
            if pressure_monitor == 95:
                pressure_monitor = 85
            continue
        else: continue

    return contraction_counter


def contractions_per_sec(pressure_data, totalContractions):
    """
    Calculate the mean contractions / secs for a pressure curve
    :param pressure_data: a list of pressure points
    :return: The mean frequency of contraction / secs
    """
    # FIXME
    total_seconds = pressure_data[len(pressure_data)-1]
    return round(totalContractions/int(int(total_seconds[0])/1000), 2)



def main():
    pressure_file = sys.argv[1]
    with open(sys.argv[1]) as pressure_file:   #opening and reading csv files
        csv_reader = csv.reader(pressure_file, delimiter=",")
        data = [row for row in csv_reader]
        n = count_contractions(data) # 0 FIXME
        f = contractions_per_sec(data, n) # 0 FIXME
        print("---")
        print("For {}:".format(pressure_file.name))
        print("* Number of contraction = {}".format(n))
        print("* Contraction / s = {}".format(f))

    return 0

if __name__ == '__main__':
    sys.exit(main())
