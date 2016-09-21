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

    args = parser.parse_args()
    return args


def main(arg):
    pass

if __name__ == '__main__':
    main()
