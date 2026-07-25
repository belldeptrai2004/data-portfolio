#!/usr/bin/env python3

import sys


# Load MapReduce document statistics.
document_statistics = {}

with open(
    "bonus_document_stats.tsv",
    "r",
    encoding="utf-8"
) as document_file:

    for line in document_file:

        fields = line.strip().split("\t")

        if len(fields) != 5:
            continue

        document_id = fields[0]

        centred_feature_norm = float(
            fields[2]
        )

        normalised_rating = float(
            fields[3]
        )

        document_statistics[document_id] = (
            centred_feature_norm,
            normalised_rating
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

    try:
        tfidf = float(fields[6])

    except ValueError:
        continue

    if document_id.startswith("train/"):

        statistics = document_statistics.get(
            document_id
        )

        if statistics is None:
            continue

        centred_feature_norm = statistics[0]
        normalised_rating = statistics[1]

        if centred_feature_norm > 0:

            contribution = (
                normalised_rating
                * tfidf
                / centred_feature_norm
            )

        else:

            contribution = 0.0

        print(
            word
            + "\t"
            + "DATA"
            + "\t"
            + str(contribution)
        )

    else:

        # Preserve words appearing only in the test set.
        print(
            word
            + "\t"
            + "MARKER"
            + "\t"
            + "0"
        )
