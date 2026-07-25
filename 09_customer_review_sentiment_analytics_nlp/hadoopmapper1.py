#!/usr/bin/env python3

import os
import re
import sys


def get_document_id():
    """
    Get the ID of the review currently being processed.

    Example Hadoop path:
    /users/hadoop/COMP3002/imdb_tiny/train/pos/0_9.txt

    Returned ID:
    train/pos/0_9.txt
    """

    # Get the input file path from Hadoop.
    input_file_path = os.environ.get(
        "mapreduce_map_input_file"
    )

    # Some Hadoop versions use this older variable name.
    if input_file_path is None:
        input_file_path = os.environ.get(
            "map_input_file"
        )

    # Use a safe value if the path is unavailable.
    if input_file_path is None:
        return "unknown_file"

    # Use forward slashes consistently.
    input_file_path = input_file_path.replace(
        "\\",
        "/"
    )

    # Break the path into separate parts.
    path_parts = input_file_path.split("/")

    # Keep the split, sentiment folder and file name.
    document_id = "/".join(
        path_parts[-3:]
    )

    return document_id


def extract_words(review_text):
    """
    Convert review text into lowercase English words.
    """

    # Convert all letters to lowercase.
    review_text = review_text.lower()

    # Remove the common HTML line-break marker.
    review_text = review_text.replace(
        "<br />",
        " "
    )

    # Extract sequences containing letters from a to z.
    words = re.findall(
        r"[a-z]+",
        review_text
    )

    return words


# Identify the review being processed.
document_id = get_document_id()


# Hadoop sends the review text one line at a time.
for line in sys.stdin:

    words = extract_words(
        line
    )

    # Emit one record for every word occurrence.
    for word in words:

        print(
            document_id
            + "\t"
            + word
        )
