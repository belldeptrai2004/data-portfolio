#!/usr/bin/env python3

import sys


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 2:
        continue

    document_id = fields[0]

    try:
        rating = float(fields[1])

    except ValueError:
        continue

    rating_squared = rating * rating

    print(
        "stats"
        + "\t"
        + "1"
        + "\t"
        + str(rating)
        + "\t"
        + str(rating_squared)
    )
