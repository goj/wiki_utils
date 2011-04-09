#!/usr/bin/env python3

import csv, pipes

__all__ = ['dump_reader']

CSV_OPTIONS = {'delimiter': ',',
               'escapechar': '\\',
               'quotechar': "'"}

def dump_reader(sql_dump_name):
    pipe = pipes.Template()
    pipe.append(r'zcat $IN', 'f-')
    pipe.append(r'grep INSERT', '--')
    pipe.append(r"sed -e 's/^.*VALUES //'"
                r"    -e 's/;$//'"
                r"    -e 's/),(/)\n(/g'",
                '--')
    pipe.append(r"sed -e 's/^(//'"
                r"    -e 's/)$//'",
                '--')
    return csv.reader(pipe.open(sql_dump_name, 'r'),
                      **CSV_OPTIONS)
