#!/usr/bin/env python3

import sys


def print_document_results(
    document_id,
    word_counts,
    total_words
):
    """
    Print the word count and term frequency
    for every word in one review.
    """

    # Sort the words to keep the output consistent.
    words = sorted(
        word_counts.keys()
    )

    for word in words:

        word_count = word_counts[word]

        term_frequency = (
            word_count
            / total_words
        )

        print(
            document_id
            + "\t"
            + word
            + "\t"
            + str(word_count)
            + "\t"
            + format(term_frequency, ".6f")
        )


# Store the review currently being processed.
current_document = None

# Store word counts for the current review.
current_word_counts = {}

# Store the total number of words in the current review.
current_total_words = 0


# Read the sorted mapper output.
for line in sys.stdin:

    line = line.strip()

    # Ignore empty lines.
    if line == "":
        continue

    # Separate the document ID and word.
    document_id, word = line.split(
        "\t",
        1
    )

    # Continue processing the same review.
    if document_id == current_document:

        current_total_words = (
            current_total_words + 1
        )

        if word in current_word_counts:

            current_word_counts[word] = (
                current_word_counts[word] + 1
            )

        else:

            current_word_counts[word] = 1

    else:

        # Print the completed previous review.
        if current_document is not None:

            print_document_results(
                current_document,
                current_word_counts,
                current_total_words
            )

        # Begin processing a new review.
        current_document = document_id
        current_word_counts = {
            word: 1
        }
        current_total_words = 1


# Print the final review after the loop finishes.
if current_document is not None:

    print_document_results(
        current_document,
        current_word_counts,
        current_total_words
    )
