[![PyPI](https://img.shields.io/pypi/v/english-words.svg)](https://pypi.org/project/english-words/)

# english-words-py

Contains sets of English words from
[svnweb.freebsd.org/csrg/share/dict/](https://svnweb.freebsd.org/csrg/share/dict/).
This is up to date with revision 61569 of their words list.

There are four sets in this package:

+ `english_words_set`: A set of English words containing both upper- and
    lower-case letters; with punctuation.
+ `english_words_lower_set`: A set of English words containing
    lower-case letters; with punctuation.
+ `english_words_alpha_set`: A set of English words containing both
    upper- and lower-case letters; with no punctuation.
+ `english_words_lower_alpha_set`: A set of English words containing
   lower-case letters; with no punctuation.

where the `lower` set is the same as the `english_words_set` with all
upper-case letters converted to lower-case letters, and where the
`alpha` set is the same as the `english_words_set` with all apostrophes
(`'`) removed. The `lower_alpha` set intuitively has both of the rules
from the `lower` set and the `alpha` set applied.

You can use use these like you would any Python set:

```
>>> from english_words import english_words_set
>>> 'ghost' in english_words_set
True
```

## Installation

Install this with pip with

```
pip install english-words
```
