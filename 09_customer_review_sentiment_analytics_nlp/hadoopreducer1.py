#!/usr/bin/env python3

import sys


def print_word_count(combined_key, total_count):
    """
    Print the final count for one document-word pair.

    Example input key:
    train/pos/0_9.txt|good

    Example output:
    train/pos/0_9.txt    good    2
    """

    # Separate the document ID and word
    document_id, word = combined_key.split(
        "|",
        1
    )

    # Output three tab-separated fields
    print(
        document_id
        + "\t"
        + word
        + "\t"
        + str(total_count)
    )


# Store the key currently being counted
current_key = None

# Store the total count for the current key
current_count = 0


# Hadoop sends sorted mapper output one line at a time
for line in sys.stdin:

    # Remove the line-break character and extra spaces
    line = line.strip()

    # Ignore empty lines
    if line == "":
        continue

    # Separate the key and value
    combined_key, count_text = line.split(
        "\t",
        1
    )

    # Convert the count from text into an integer
    count = int(count_text)

    # The current line belongs to the same key
    if combined_key == current_key:

        current_count = current_count + count

    else:

        # Print the completed previous key
        if current_key is not None:

            print_word_count(
                current_key,
                current_count
            )

        # Start counting a new key
        current_key = combined_key
        current_count = count


# Print the final key after the loop ends
if current_key is not None:

    print_word_count(
        current_key,
        current_count
    )
