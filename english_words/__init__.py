"""
Contains sets of English words from obtained from https://svnweb.freebsd.org/csrg/share/dict/.

There are eight sets in this module:

english_words_set: A set of English words containing both upper- and
    lower-case letters; with punctuation.
english_words_lower_set: A set of English words containing lower-case
    letters; with punctuation.
english_words_upper_set:  A set of English words containing upper-case
    letters; with punctuation.
english_words_captialized_set: A set of English words containing captitalized words; with punctuation.

english_words_alpha_set: A set of English words containing both upper-
    and lower-case letters; with no punctuation.
english_words_lower_alpha_set: A set of English words containing
    lower-case letters; with no punctuation.
english_words_upper_alpha_set: A set of English words containing
    upper-case letters; with no punctuation.
english_words_captialized_alpha_set: A set of English words containing captitalized words; with no punctuation.
"""

import os
from pathlib import Path
import gzip

BASE_DIR = Path(__file__).resolve().parent

with gzip.open(BASE_DIR / os.path.join('data', 'web2.txt.gz'), "rt", encoding="utf-8") as f:
    web2_words: list = [x.strip() for x in f]

web2_lower = list(map(lambda x: x.lower(), web2_words))

web2_words_set: set = set(web2_words)
web2_lower_set: set = set(web2_lower)

with gzip.open(BASE_DIR / os.path.join('data', 'english_words_set.txt.gz'), "rt", encoding="utf-8") as f:
    english_words_set : set = {x.strip() for x in f}

with gzip.open(BASE_DIR / os.path.join('data', 'english_words_lower_set.txt.gz'), "rt", encoding="utf-8") as f:
    english_words_lower_set : set = {x.strip() for x in f}
    english_words_upper_set: set = {x.strip().upper() for x in f}
    english_words_captialized_set: set = {x.strip().capitalize() for x in f}

with gzip.open(BASE_DIR / os.path.join('data', 'english_words_alpha_set.txt.gz'), "rt", encoding="utf-8") as f:
    english_words_alpha_set : set = {x.strip() for x in f}

with gzip.open(BASE_DIR / os.path.join('data', 'english_words_lower_alpha_set.txt.gz'), "rt", encoding="utf-8") as f:
    english_words_lower_alpha_set : set = {x.strip() for x in f}
    english_words_upper_alpha_set: set = {x.strip().upper() for x in f}
    english_words_captialized_alpha_set: set = {x.strip().capitalize() for x in f}
