#!/usr/bin/env python3

import sys
import datetime

from dateutil import parser


def to_iso_datetime(val):
    return datetime.datetime.utcfromtimestamp(val).isoformat()


def to_epoch(val):
    dt = parser.parse(val)
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000.0)


# Ghetto type checking is ghetto
def conv_number(val):
    try:
        return float(val)
    except:
        try:
            return int(val)
        except:
            return None


def main():
    if len(sys.argv) < 2:
        print('Usage: {a} <epoch|timestamp>'.format(a=sys.argv[0]))

    val = sys.argv[1]
    pval = conv_number(val)
    if pval is not None:
        print(to_iso_datetime(pval))
    else:
        print(to_epoch(val))
