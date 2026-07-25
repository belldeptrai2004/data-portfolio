#!/usr/bin/env python3

import sys


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

    # Only training TF-IDF values contribute to the mean.
    if document_id.startswith("train/"):

        print(
            word
            + "\t"
            + str(tfidf)
        )

    else:

        # Preserve test-only vocabulary items.
        print(
            word
            + "\t"
            + "0"
        )
