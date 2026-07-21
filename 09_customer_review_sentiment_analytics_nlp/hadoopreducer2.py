#!/usr/bin/env python3

import math
import os
import sys


# Read the total number of documents from Hadoop.
total_documents_text = os.environ.get(
    "TOTAL_DOCUMENTS"
)

# Use 60 as a safe default for the tiny dataset.
if total_documents_text is None:
    total_documents = 60
else:
    total_documents = int(
        total_documents_text
    )


def print_tfidf_results(
    word,
    document_records
):
    """
    Calculate and print TF-IDF results for one word.
    """

    # One record represents one document containing the word.
    document_frequency = len(
        document_records
    )

    # Calculate smoothed IDF.
    inverse_document_frequency = math.log(
        (total_documents + 1)
        / (document_frequency + 1)
    ) + 1

    # Sort records by document ID for consistent output.
    document_records = sorted(
        document_records
    )

    # Calculate TF-IDF for each document.
    for record in document_records:

        document_id = record[0]
        word_count = record[1]
        term_frequency = record[2]

        tfidf = (
            term_frequency
            * inverse_document_frequency
        )

        print(
            document_id
            + "\t"
            + word
            + "\t"
            + str(word_count)
            + "\t"
            + format(term_frequency, ".6f")
            + "\t"
            + str(document_frequency)
            + "\t"
            + format(
                inverse_document_frequency,
                ".6f"
            )
            + "\t"
            + format(tfidf, ".6f")
        )


# Store the word currently being processed.
current_word = None

# Store all document records for the current word.
current_document_records = []


# Read sorted mapper output.
for line in sys.stdin:

    line = line.strip()

    # Ignore empty lines.
    if line == "":
        continue

    # Separate the mapper output fields.
    fields = line.split(
        "\t"
    )

    # Ignore an invalid record.
    if len(fields) != 4:
        continue

    word = fields[0]
    document_id = fields[1]
    word_count = int(
        fields[2]
    )
    term_frequency = float(
        fields[3]
    )

    # Store the current document information.
    document_record = (
        document_id,
        word_count,
        term_frequency
    )

    # Continue collecting records for the same word.
    if word == current_word:

        current_document_records.append(
            document_record
        )

    else:

        # Print the completed previous word.
        if current_word is not None:

            print_tfidf_results(
                current_word,
                current_document_records
            )

        # Begin collecting a new word.
        current_word = word
        current_document_records = [
            document_record
        ]


# Print the final word after the loop ends.
if current_word is not None:

    print_tfidf_results(
        current_word,
        current_document_records
    )
