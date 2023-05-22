#!/usr/bin/env python3

"""Processes raw words lists.

The raw word lists are the text files found in the raw_data directory at
the root of the repository. The identifier for each word list is taken
to be the name of the text file (i.e., the * in *.txt). Currently,
processing is done even for word lists that have been previously
processed; if the speed of this script becomes an issue at some point,
previously processed word lists should be identified and skipped.

Binary representations of word list sets are produced using the pickle
module for every combination of options.
"""

import glob
import itertools
import os
import pickle
import re


# Directories
REPOSITORY_BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
RAW_DATA_DIR = os.path.join(REPOSITORY_BASE_DIR, "raw_data")
PROCESSED_DATA_DIR = os.path.join(REPOSITORY_BASE_DIR, "english_words", "data")

# Option constants
ALPHA = "alpha"
LOWER = "lower"
OPTIONS = (ALPHA, LOWER)

# Process each word list
for raw_data_path in glob.glob(os.path.join(RAW_DATA_DIR, "*.txt")):
    identifier = os.path.splitext(os.path.basename(raw_data_path))[0]

    # Get the lines
    with open(raw_data_path, "r", encoding="utf8") as f:
        lines = [l.rstrip() for l in f.readlines()]

    # Process each combination of options. The below method is a little
    # overkill with few options, but scales decently if more options are
    # included. This loop can be made more efficient by reusing the
    # N - 1 length option combination results when processing the N
    # length option combination word lists; but this optimization isn't
    # implemented here.
    for n in range(len(OPTIONS) + 1):
        for current_options in itertools.combinations(OPTIONS, n):
            # Copy the data lines when we process them here
            lines_copy = lines.copy()

            # Now consume each option and perform the required
            # operations
            for option in current_options:
                if option == ALPHA:
                    new_lines_copy = []

                    for l in lines_copy:
                        new_l = re.sub("[^A-Za-z0-9]", "", l)

                        if new_l:
                            new_lines_copy.append(new_l)

                    lines_copy = new_lines_copy
                elif option == LOWER:
                    lines_copy = [l.lower() for l in lines_copy]

            # Encode the options used into the destination file name
            dest_file_name = (
                identifier
                + ("_" if len(current_options) > 0 else "")
                + "_".join(current_options)
                + ".pickle"
            )
            dest_file_path = os.path.join(PROCESSED_DATA_DIR, dest_file_name)

            # Turn the list into a set and write the object to a file
            data_set = set(lines_copy)

            with open(dest_file_path, "wb") as f:
                pickle.dump(data_set, f, protocol=pickle.HIGHEST_PROTOCOL)
