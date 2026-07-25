#!/usr/bin/env python3

import math
import os
import sys


rating_norm = float(
    os.environ.get(
        "RATING_NORM",
        "1"
    )
)

feature_mean_squared_sum = float(
    os.environ.get(
        "FEATURE_MEAN_SQUARED_SUM",
        "0"
    )
)


def extract_rating(document_id):

    file_name = document_id.split("/")[-1]

    rating_text = (
        file_name
        .split("_")[1]
        .split(".")[0]
    )

    return float(rating_text)


def print_document_statistics(
    document_id,
    sum_x_squared,
    sum_x_times_mean
):

    centred_norm_squared = (
        sum_x_squared
        - (2.0 * sum_x_times_mean)
        + feature_mean_squared_sum
    )

    centred_norm_squared = max(
        centred_norm_squared,
        0.0
    )

    centred_feature_norm = math.sqrt(
        centred_norm_squared
    )

    rating = extract_rating(
        document_id
    )

    if rating_norm > 0:

        normalised_rating = (
            rating
            / rating_norm
        )

    else:

        normalised_rating = 0.0


    if centred_feature_norm > 0:

        baseline_component = (
            normalised_rating
            / centred_feature_norm
        )

    else:

        baseline_component = 0.0


    print(
        document_id
        + "\t"
        + format(rating, ".6f")
        + "\t"
        + format(centred_feature_norm, ".10f")
        + "\t"
        + format(normalised_rating, ".10f")
        + "\t"
        + format(baseline_component, ".10f")
    )


current_document = None
current_sum_x_squared = 0.0
current_sum_x_times_mean = 0.0


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 4:
        continue

    document_id = fields[0]

    try:
        tfidf = float(fields[2])
        feature_mean = float(fields[3])

    except ValueError:
        continue

    if document_id == current_document:

        current_sum_x_squared += (
            tfidf * tfidf
        )

        current_sum_x_times_mean += (
            tfidf * feature_mean
        )

    else:

        if current_document is not None:

            print_document_statistics(
                current_document,
                current_sum_x_squared,
                current_sum_x_times_mean
            )

        current_document = document_id

        current_sum_x_squared = (
            tfidf * tfidf
        )

        current_sum_x_times_mean = (
            tfidf * feature_mean
        )


if current_document is not None:

    print_document_statistics(
        current_document,
        current_sum_x_squared,
        current_sum_x_times_mean
    )
