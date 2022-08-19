# -*- coding: utf-8 -*-
import argparse
import csv

# Create the parser
parser = argparse.ArgumentParser(description='Command line Help')

# Add the arguments
parser.add_argument(dest='file_path', metavar='path', type=str, help='path to source file')
parser.add_argument('revs', type=str.lower, nargs='+', help='category')
parser.add_argument('-l', dest='flag', action='store_true',  help='add header')
args = parser.parse_args()

# print (args)

# Parse arguments
file_path = args.file_path
flag = args.flag
revs = args.revs

with open(file_path, 'r') as csvfile:
    term_reader = csv.reader(csvfile, delimiter=':')
    
    header_row = next(term_reader)
    new_header_row = [item.lower() for item in header_row]
    
    difference = set(revs) - set(new_header_row)
    if difference:
        print ("Fields " + ', '.join("'" + item + "'" for item in difference) + " do(es) not exist in the data file.")

    headers = []
    for item in revs:
        if item in new_header_row:
            headers.append (new_header_row.index(item))
    
    if flag == True:
        print (' '.join(''.join(header_row[index]) for index in headers))

    for row in term_reader:
        print(' '.join(row[index] for index in headers))