#!/usr/bin/env python3

import sys
import os.path
import csv
from decimal import Decimal
from statistics import mean

SEARCH_KEYWORD = 0
IMPRESSIONS = 1
CTR = 2
COST = 3
POSITION = 4
COMPANY = 5
REVENUE = 6

HEADER = [
    'Search keyword',
    'Impressions',
    'CTR',
    'Cost',
    'Position',
    'Company',
    'Revenue'
]


def calculate_SEMP_per_keyword(kw):
    return ((kw['impressions'] * kw['cost'] * kw['position']) /
            (kw['ctr'] * kw['revenue']))


def calculate_SEMP_per_company(kw_list):
    return mean([calculate_SEMP_per_keyword(kw) for kw in kw_list])


def main(argv):
    help_msg = "Usage: measure_semp.py /path/to/data.csv"

    if len(argv) != 1:
        print(help_msg)
        sys.exit(2)

    data_path = argv[0]
    if not os.path.isfile(data_path):
        msg = '{} is not a file'.format(data_path)
        print(msg)
        sys.exit(2)

    with open(data_path) as f:
        reader = csv.reader(f)

        header = next(reader)
        if header != HEADER:
            msg = '{} is not a valid data file'.format(data_path)
            print(msg)
            sys.exit(2)

        # Group data by company
        data = {}

        for row in reader:
            company = row[COMPANY]

            if company not in data:
                data[company] = []

            data[company].append({
                'impressions': int(row[IMPRESSIONS]),
                'ctr': Decimal(row[CTR]),
                'cost': Decimal(row[COST]),
                'position': int(row[POSITION]),
                'revenue': Decimal(row[REVENUE])
            })

        result = []
        for company, kw_list in data.items():
            result.append({
                'company': company,
                'SEMP': calculate_SEMP_per_company(kw_list)
            })

        result = sorted(result, key=lambda item: item['SEMP'])

        for item in result:
            print('{}: {}'.format(item['company'], item['SEMP']))


if __name__ == "__main__":
    main(sys.argv[1:])
