"""Stores utility functions for the main function."""


def get_data_file_name(identifier: str, options: list[str]) -> str:
    """Get the name of a data file in the processed data directory.

    Args:
        identifier: A word list identifier.
        options: A list of options the word list is processed with.

    Returns:
        The data file name which contains the word list processed with
        the given options.
    """
    return (
        identifier
        + ("_" if len(options) > 0 else "")
        + "_".join(options)
        + ".pickle"
    )
