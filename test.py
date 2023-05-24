#!/usr/bin/env python3

import itertools
import re
import unittest
from english_words import get_english_words_set


# Constants
GCIDE_ID = "gcide"
WEB2_ID = "web2"

# Function to get all possible word sets
def get_all_possible_word_sets():
    # All permutation of option arguments
    num_options = 2
    options_permutations = itertools.permutations([True, False], num_options)

    # All 1 to max length combinations of word list IDs
    word_list_ids = (GCIDE_ID, WEB2_ID)
    word_list_ids_combos = []

    for n in range(1, len(word_list_ids) + 1):
        for word_list_ids_combo in itertools.combinations(word_list_ids, n):
            word_list_ids_combos.append(tuple(word_list_ids_combo))

    # All word sets
    word_sets = []

    for options in options_permutations:
        for word_list_combo in word_list_ids_combos:
            word_sets.append(get_english_words_set(word_list_combo, *options))

    return word_sets


class TestBasic(unittest.TestCase):
    """Contains a few basic tests."""

    def test_alpha_standalone_option(self):
        """Test to see if alpha option is working on target strings."""
        # Note that web2 doesn't have any non-alphanumeric characters so
        # this test doesn't apply to it
        gcide_nonalpha_word = "3-hitter"

        for word_list_id, test_nonalpha_word in zip(
            (GCIDE_ID,),
            (gcide_nonalpha_word,),
        ):
            # Get word sets
            word_set = get_english_words_set([word_list_id])
            word_alpha_set = get_english_words_set([word_list_id], alpha=True)

            # Use test strings to assert membership
            self.assertIn(test_nonalpha_word, word_set)
            self.assertIn(
                re.sub("[^A-Za-z0-9]", "", test_nonalpha_word), word_alpha_set
            )

    def test_lower_standalone_option(self):
        """Test to see if lower option is working on target strings."""
        gcide_capitalized_word = "Zounds"
        web2_capitalized_word = "Abasgi"

        for word_list_id, test_capitalized_word in zip(
            (GCIDE_ID, WEB2_ID),
            (gcide_capitalized_word, web2_capitalized_word),
        ):
            # Get word sets
            word_set = get_english_words_set([word_list_id])
            word_lower_set = get_english_words_set([word_list_id], lower=True)

            # Use test strings to assert membership
            self.assertIn(test_capitalized_word, word_set)
            self.assertIn(test_capitalized_word.lower(), word_lower_set)

    def test_no_empty_string(self):
        """Test to make sure no word sets contain an empty string."""
        # Get all possible word sets
        word_sets = get_all_possible_word_sets()

        # Ensure they are non-empty
        for word_set in word_sets:
            self.assertFalse("" in word_set)

    def test_non_empty_sets(self):
        """Test to make sure all word sets non-empty."""
        # Get all possible word sets
        word_sets = get_all_possible_word_sets()

        # Ensure they are non-empty
        for word_set in word_sets:
            self.assertTrue(len(word_set) > 0)


if __name__ == "__main__":
    unittest.main()
