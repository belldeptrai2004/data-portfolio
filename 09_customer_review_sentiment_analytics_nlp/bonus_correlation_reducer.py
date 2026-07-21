#!/usr/bin/env python3

import os
import sys


baseline_sum = float(
    os.environ.get(
        "BASELINE_SUM",
        "0"
    )
)


# Load the MapReduce feature means.
feature_means = {}

with open(
    "bonus_feature_means.tsv",
    "r",
    encoding="utf-8"
) as mean_file:

    for line in mean_file:

        fields = line.strip().split("\t")

        if len(fields) != 2:
            continue

        feature_means[fields[0]] = float(
            fields[1]
        )


def print_correlation(
    word,
    contribution_sum,
    training_document_frequency
):

    feature_mean = feature_means.get(
        word,
        0.0
    )

    correlation = (
        contribution_sum
        - (
            feature_mean
            * baseline_sum
        )
    )

    print(
        word
        + "\t"
        + str(training_document_frequency)
        + "\t"
        + format(feature_mean, ".10f")
        + "\t"
        + format(correlation, ".10f")
    )


current_word = None
current_contribution_sum = 0.0
current_training_frequency = 0


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 3:
        continue

    word = fields[0]
    record_type = fields[1]

    try:
        contribution = float(fields[2])

    except ValueError:
        continue

    if word == current_word:

        if record_type == "DATA":

            current_contribution_sum += contribution
            current_training_frequency += 1

    else:

        if current_word is not None:

            print_correlation(
                current_word,
                current_contribution_sum,
                current_training_frequency
            )

        current_word = word
        current_contribution_sum = 0.0
        current_training_frequency = 0

        if record_type == "DATA":

            current_contribution_sum = contribution
            current_training_frequency = 1


if current_word is not None:

    print_correlation(
        current_word,
        current_contribution_sum,
        current_training_frequency
    )
