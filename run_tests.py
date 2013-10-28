#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import subprocess
import sys


def run():
    data = open('tests.json').read()

    try:
        data = json.loads(data)
    except ValueError:
        print "[x] Failed to parse tests.json! Exiting."
        print "[.] You should report this issue."
        return

    if len(sys.argv) == 1:
        print "[x] You need to specify the location of the program"
        _help()
        return

    if len(sys.argv[1]) == '-h':
        _help()
        return

    program = sys.argv[1]
    failed_cases = []
    for name, item in data.get('tests', {}).iteritems():
        ret = run_test(program, name, item)
        if not ret:
            print "[/] Passed %s [%s]" % (name, item.get('email', 'No Email'))
        else:
            print "[x] Failed %s [%s]" % (name, item.get('email', 'No Email'))
            failed_cases.append(ret)

    if not failed_cases:
        print "[/] Passed ALL tests"
        return

    print "You failed the following %d cases:" % len(failed_cases)
    for item in failed_cases:
        print "[.] %s: %s" % (item['reason'], item['cmd'])
        print item['details']
        print


def run_test(program, name, item):
    if 'test' not in item:
        print "[x] Skipping %s - no flags. Please report this" % name
        return

    cmd = "%s %s" % (program, item['test'])

    print "[.] Running %s (%s)" % (name, cmd)

    try:
        devnull = open('/dev/null', 'w')
        ret = subprocess.check_output(cmd, shell=True, stderr=devnull)
    except subprocess.CalledProcessError as e:
        return {
            'error': True,
            'reason': 'Program Crashed',
            'details': e,
            'email': item.get('email', 'No Email'),
            'cmd': cmd
        }

    if 'output' not in item:
        print "[x] No output for test %s. Please report this" % name
        return

    actual_output = open(item['output']).read().strip().split('\n')
    output = ret.strip().split('\n')

    greater = len(actual_output)
    if len(actual_output) != len(output):
        if len(actual_output) > len(output):
            greater = len(actual_output)
        else:
            greater = len(output)

    i = 0
    while (i < greater - 1):
        if not actual_output[i] == output[i]:
            return {
                'error': True,
                'reason': 'Output Difference',
                'details': 'Line difference on line %s. \nActual Output: %s\nYour Output: %s' % (i, actual_output[i], output[i]),
                'email': item.get('email', 'No Email'),
                'cmd': cmd
            }

        i = i + 1


def _help():
    print "EECS 281 Community Grader"
    print "python run_tests path/to/your/program"
    print "Example: python run_tests.py ../proj2/MineEscape"
    print
    print "-h Prints this messasge"


if __name__ == "__main__":
    run()
