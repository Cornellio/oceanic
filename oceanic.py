#!/usr/bin/python

'''
A Dashing job for graphing ocean temperatures of dive sites.
Lookup current temperate from NOAA, store results to local file,
then read historical values from file and post to a Dashing graph.
'''

import sys
import time
import argparse
import urllib2
import httplib


def get_temperature():
    pass


def store_temperature():
    pass


def tail_temperature_history():
    pass


def construct_graph_points():
    pass


def transmit_graph_points(arg):
    pass


def parse_args():
    '''Parse arguments'''

    parser = argparse.ArgumentParser(description='Graph ocean temperatures.')

    parser.add_argument('-a', help='Dashing authentication token',
                        required=True, dest='authtoken')

    parser.add_argument('--host', help='Dashing host to send data to',
                        required=True, dest='dashing_host')

    parser.add_argument('-w', help='Widget to send data to',
                        required=True, dest='widget')

    parser.add_argument('-n', help='Number of data points to\
                        plot on x-axis of graph',
                        required=False, type=int, dest='num_recs', default=12)

    parser.add_argument('-i', help='Interval. This is the number of values\
                        to skip when plotting data points',
                        required=False, type=int,
                        dest='interval', default=1)

    parser.add_argument('-x', '--skip_lookup', help='Do not lookup\
                        current value, just graph historical\
                        values', dest='skip_lookup', required=False,
                        action='store_true')

    parser.add_argument('-f', help='File to store values in. Defaults to the\
                        name of the script, excluding the .py extension',
                        required=False, dest='historyfile',
                        default=sys.argv[0].strip('py') + "history")

    return parser.parse_args()


def main():
    args = parse_args()
    print args

if __name__ == '__main__':
    main()
