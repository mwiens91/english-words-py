"""Stores utility functions for the main function."""


def get_data_file_name(identifier: str, options: list[str]) -> str:
    # This is basically repeated code taken from the script used to
    # process data
    return (
        identifier
        + ("_" if len(options) > 0 else "")
        + "_".join(options)
        + ".pickle"
    )
