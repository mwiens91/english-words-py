"""Stores utility functions for the main function."""

from collections.abc import Iterable


def get_data_file_path(identifier: str, options: Iterable[str]) -> str:
    # This is basically repeated code taken from the script used to
    # process data
    data_file_name = (
        identifier
        + ("_" if len(options) > 0 else "")
        + "_".join(options)
        + ".pickle"
    )
    return data_file_name
