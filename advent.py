#!/usr/bin/env python3

import optparse
import os.path
import requests
import sys
import time

import session_id

def get_input(n):
    inpath = 'input/%02d' % ((int(n) - 1)// 2 + 1)

    # If we already have the input, read it.
    if os.path.exists(inpath):
        with open(inpath) as f:
            return f.read()

    # Otherwise, download the input for problem n from adventofcode.com and
    # write it to disk.
    uri = 'http://adventofcode.com/2019/day/%d/input' % n
    response = requests.get(uri,  cookies={'session': session_id.SESSION_ID})
    response.raise_for_status()

    with open(inpath, 'w') as f:
        f.write(response.text)
    return response.text


def invoke(n):
    # import the function advent# and time its execution
    # if it does not exist, exit gracefully
    file_name = "advent%02d" % n
    function_name = "advent%02d" % n
    try:
        module = __import__(file_name)
    except ImportError:
        if not do_all:
            print('Could not import %s, has that problem been solved yet?' % \
                file_name)
        return 1
    target_function = getattr(module, function_name)
    if not callable(target_function):
        if not do_all: print('%s does not exist' % function_name)
        return 1

    input = get_input(n)
    start = time.time()
    try:
        print(target_function(input))
    except:
        print('Error during %s: %s' % (function_name, sys.exc_info()[0]))
        raise
    end = time.time()
    print('%s took %0.0f ms' % (function_name, (end - start) * 1000.9))


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)

    settings, args = parser.parse_args(argv)

    if not args:
        print('usage: advent problem_number')
        return 1

    return invoke(int(args[0]))

if __name__ == "__main__":
    status = main()
    sys.exit(status)
