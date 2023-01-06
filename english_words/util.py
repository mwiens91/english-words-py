"""Stores utility functions for the main function."""

import os
import typing
from english_words.constants import PROCESSED_DATA_DIR


def get_data_file_path(identifier: str, options: typing.Iterable[str]) -> str:
    # This is basically repeated code taken from the script used to
    # process data
    data_file_name = (
        identifier
        + ("_" if len(options) > 0 else "")
        + "_".join(options)
        + ".pickle"
    )

    data_file_path = os.path.join(PROCESSED_DATA_DIR, data_file_name)

    return data_file_path
