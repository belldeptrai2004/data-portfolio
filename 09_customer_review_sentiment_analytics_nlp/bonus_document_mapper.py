#!/usr/bin/env python3

import sys


# Load the feature means distributed by Hadoop.
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


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 7:
        continue

    document_id = fields[0]
    word = fields[1]

    # The bonus uses training data only.
    if not document_id.startswith("train/"):
        continue

    try:
        tfidf = float(fields[6])

    except ValueError:
        continue

    feature_mean = feature_means.get(
        word,
        0.0
    )

    print(
        document_id
        + "\t"
        + word
        + "\t"
        + str(tfidf)
        + "\t"
        + str(feature_mean)
    )
