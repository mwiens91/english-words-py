"""Contains the main function to generate word sets.

The package readme provides documentation for this package and the main
function.
"""

from collections.abc import Iterable
import os
import pickle
from english_words.constants import PROCESSED_DATA_DIR, ALPHA, LOWER
from english_words.util import get_data_file_path


def get_english_words_set(
    sources: Iterable[str], alpha: bool = False, lower: bool = False
) -> set[str]:
    # Ensure sources is non-empty
    if not sources:
        raise ValueError("No word list sources were provided")

    # Set up a list to dump all the sets in
    sets_list = []

    # Put the options into a tuple. These *critically* need to be in
    # alphabetic order
    options = []

    if alpha:
        options.append(ALPHA)

    if lower:
        options.append(LOWER)

    # Get sets to combine
    for source in sources:
        data_path = get_data_file_path(source, options)

        try:
            with open(data_path, "rb") as f:
                sets_list.append(pickle.load(f))
        except FileNotFoundError as e:
            raise ValueError(
                f"{source} is not a valid word list identifier"
            ) from e

    # Combine the sets and return the results
    return set.union(*sets_list)
