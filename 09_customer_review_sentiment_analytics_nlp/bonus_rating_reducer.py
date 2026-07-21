#!/usr/bin/env python3

import math
import sys


number_of_documents = 0
sum_of_ratings = 0.0
sum_of_squared_ratings = 0.0


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 4:
        continue

    number_of_documents += int(fields[1])
    sum_of_ratings += float(fields[2])
    sum_of_squared_ratings += float(fields[3])


if number_of_documents > 0:

    # Keep the mean for descriptive reporting.
    mean_rating = (
        sum_of_ratings
        / number_of_documents
    )

    # Calculate the L2 norm required by the assignment.
    # The rating vector is not centred.
    rating_norm = math.sqrt(
        sum_of_squared_ratings
    )

    print(
        "stats"
        + "\t"
        + str(number_of_documents)
        + "\t"
        + format(sum_of_ratings, ".6f")
        + "\t"
        + format(sum_of_squared_ratings, ".6f")
        + "\t"
        + format(mean_rating, ".6f")
        + "\t"
        + format(rating_norm, ".6f")
    )
