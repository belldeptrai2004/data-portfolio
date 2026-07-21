#!/usr/bin/env python3

import sys


# Read MapReduce Job 1 output one line at a time.
for line in sys.stdin:

    # Remove the line-break character.
    line = line.strip()

    # Ignore empty lines.
    if line == "":
        continue

    # Separate the four Job 1 fields.
    fields = line.split(
        "\t"
    )

    # Ignore an invalid record.
    if len(fields) != 4:
        continue

    document_id = fields[0]
    word = fields[1]
    word_count = fields[2]
    term_frequency = fields[3]

    # Use the word as the Hadoop key.
    print(
        word
        + "\t"
        + document_id
        + "\t"
        + word_count
        + "\t"
        + term_frequency
    )
