#!/usr/bin/env python
# Name: Meike Kortleve
# Student number: 10773576
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

# Global dictionary for the data
data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}

with open(INPUT_CSV, newline='') as csvfile:
    reader = csv.reader(csvfile)
    total_2008 = 0
    total_2009 = 0
    total_2010 = 0
    total_2011 = 0
    total_2012 = 0
    total_2013 = 0
    total_2014 = 0
    total_2015 = 0
    total_2016 = 0
    total_2017 = 0

    count_2008 = 0
    count_2009 = 0
    count_2010 = 0
    count_2011 = 0
    count_2012 = 0
    count_2013 = 0
    count_2014 = 0
    count_2015 = 0
    count_2016 = 0
    count_2017 = 0

    # read in the csv file
    for row in reader:
        if row[2] == '2008':
            total_2008 = (total_2008 + float(row[1]))
            count_2008 = count_2008 + 1
        elif row[2] == '2009':
             total_2009 = total_2009 + float(row[1])
             count_2009 = count_2009 + 1
        elif row[2] == '2010':
            total_2010 = total_2010 + float(row[1])
            count_2010 = count_2010 + 1
        elif row[2] == '2011':
            total_2011 = total_2011 + float(row[1])
            count_2011 = count_2011 + 1
        elif row[2] == '2012':
            total_2012 = total_2012 + float(row[1])
            count_2012 = count_2012 + 1
        elif row[2] == '2013':
            total_2013 = total_2013 + float(row[1])
            count_2013 = count_2013 + 1
        elif row[2] == '2014':
            total_2014 = total_2014 + float(row[1])
            count_2014 = count_2014 + 1
        elif row[2] == '2015':
            total_2015 = total_2015 + float(row[1])
            count_2015 = count_2015 + 1
        elif row[2] == '2016':
            total_2016 = total_2016 + float(row[1])
            count_2016 = count_2016 + 1
        elif row[2] == '2017':
            total_2017 = total_2017 + float(row[1])
            count_2017 += 1

    # calculate mean
    data_dict['2008'] = total_2008/count_2008
    data_dict['2009'] = total_2009/count_2009
    data_dict['2010'] = total_2010/count_2010
    data_dict['2011'] = total_2011/count_2011
    data_dict['2012'] = total_2012/count_2012
    data_dict['2013'] = total_2013/count_2013
    data_dict['2014'] = total_2014/count_2014
    data_dict['2015'] = total_2015/count_2015
    data_dict['2016'] = total_2016/count_2016
    data_dict['2017'] = total_2017/count_2017

if __name__ == "__main__":
    #plot graph
    plt.bar(data_dict.keys(),data_dict.values())
    plt.suptitle('IMDb ratings per year')
    plt.xlabel('Year of release')
    plt.ylabel('Mean rating')
    plt.show()
