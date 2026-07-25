#!/usr/bin/env python3

import os
import re
import sys


def get_document_id():
    """
    Get the ID of the review currently being processed.

    Example input path:
    /users/bigdata/Hadoop/imdb/tinyversion/train/pos/0_9.txt

    Returned document ID:
    train/pos/0_9.txt
    """

    # Get the current input file path from Hadoop
    input_file_path = os.environ.get(
        "mapreduce_map_input_file"
    )

    # Some Hadoop versions use a different variable name
    if input_file_path is None:
        input_file_path = os.environ.get(
            "map_input_file"
        )

    # Use a safe name if Hadoop does not provide the path
    if input_file_path is None:
        return "unknown_file"

    # Replace Windows separators with standard separators
    input_file_path = input_file_path.replace(
        "\\",
        "/"
    )

    # Split the path into individual parts
    path_parts = input_file_path.split("/")

    # Keep the final three parts:
    # train/pos/0_9.txt
    document_id = "/".join(
        path_parts[-3:]
    )

    return document_id


def extract_words(review_text):
    """
    Convert review text into lowercase English words.

    Example:
    'A GREAT movie!' becomes ['a', 'great', 'movie']
    """

    # Convert all letters to lowercase
    review_text = review_text.lower()

    # Remove the common HTML line-break marker
    review_text = review_text.replace(
        "<br />",
        " "
    )

    # Extract sequences containing letters from a to z
    words = re.findall(
        r"[a-z]+",
        review_text
    )

    return words


# Identify the review currently being processed
document_id = get_document_id()


# Hadoop sends review text one line at a time
for line in sys.stdin:

    # Convert the current line into words
    words = extract_words(line)

    # Emit one record for each word occurrence
    for word in words:

        combined_key = document_id + "|" + word

        # Output format:
        # document_id|word    1
        print(
            combined_key + "\t1"
        )
