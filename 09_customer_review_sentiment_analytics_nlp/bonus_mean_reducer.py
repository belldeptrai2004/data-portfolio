#!/usr/bin/env python3

import os
import sys


total_documents_text = os.environ.get(
    "TOTAL_TRAINING_DOCUMENTS"
)

if total_documents_text is None:
    total_documents = 40

else:
    total_documents = int(
        total_documents_text
    )


current_word = None
current_sum = 0.0


def print_mean(word, feature_sum):

    feature_mean = (
        feature_sum
        / total_documents
    )

    print(
        word
        + "\t"
        + format(feature_mean, ".10f")
    )


for line in sys.stdin:

    line = line.strip()

    if line == "":
        continue

    fields = line.split("\t")

    if len(fields) != 2:
        continue

    word = fields[0]

    try:
        tfidf = float(fields[1])

    except ValueError:
        continue

    if word == current_word:

        current_sum += tfidf

    else:

        if current_word is not None:

            print_mean(
                current_word,
                current_sum
            )

        current_word = word
        current_sum = tfidf


if current_word is not None:

    print_mean(
        current_word,
        current_sum
    )
