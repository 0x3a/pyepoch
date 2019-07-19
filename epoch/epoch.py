#!/usr/bin/env python3

import sys
import datetime
import argparse

from dateutil import parser as du_parser


# Taken from: https://mail.python.org/pipermail/tutor/2003-November/026645.html
class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


# Remove buffering, processing large datasets eats memory otherwise
sys.stdout = Unbuffered(sys.stdout)

def to_iso_datetime(val, in_seconds):
    if not in_seconds:
        val /= 1000

    return datetime.datetime.utcfromtimestamp(val).isoformat()

def to_epoch(val, in_seconds):
    dt = du_parser.parse(val)
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * (1 if in_seconds else 1000))


# Ghetto type check & conversion is ghetto
def convert_value(val):
    try:
        return float(val)
    except:
        try:
            return int(val)
        except:
            return None


def convert(val, in_seconds):
    pval = convert_value(val)
    if pval is not None:
        return to_iso_datetime(pval, in_seconds)
    else:
        return to_epoch(val, in_seconds)

def parse_args():
    parser = argparse.ArgumentParser(prog="epoch")
    parser.add_argument('value', nargs='?', type=str, default=None, help="Value to convert (can also be supplied on stdin)")

    parser.add_argument('-s', '--seconds', action="store_true",
                        help="For input epochs, assume second notations, for input datestamps conver to epochs in seconds."
                        )

    return parser.parse_args()

def main():
    args = parse_args()

    if args.value:
        print(convert(args.value, in_seconds=args.seconds))
    else:
        for line in sys.stdin:
            line = line.rstrip()
            print(convert(line, in_seconds=args.seconds))
