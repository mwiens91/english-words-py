[![PyPI](https://img.shields.io/pypi/v/english-words.svg)](https://pypi.org/project/english-words/)

# english-words-py

Returns sets of English words created by combining different words
lists together. Example usage: to get a set of English words from the
"web2" word list, including only lower-case letters, you write the
following:

```python3
>>> from english_words import get_english_words_set
>>> web2lowerset = get_english_words_set(['web2'], lower=True)
```

## Usage

From the main package, import `get_english_words_set` as demonstrated
above. This function takes a number of arguments; the first is a list of
word list identifiers for the word lists to combine and the rest are
flags. These arguments are described here (in the following order):

- `sources` is an iterable containing strings
corresponding to word list identifiers (see "Word lists" subsection
below)
- `alpha` (default `False`) is a flag specifying that all
  non-alphanumeric characters (e.g.: `-`, `'`) should be stripped
- `lower` (default `False` ) is a flag specifying that all upper-case
  letters should be converted to lower-case

Each word list is pre-processed to handle the above flags, so using any
combination of options will not cause the function to run slower.

Note that some care needs to be used when combining word lists. For
example, only proper nouns in the `web2` word list are capitalized, but
every word in the `gcide` word list is capitalized.

### Word lists

| Name/URL | Identifier | Notes |
| :--- | :--- | :--- |
| [GCIDE 0.53 index](https://ftp.gnu.org/gnu/gcide/) | `gcide` | Words found in GNU Collaborative International Dictionary of English 0.53. All words capitalized, and like a dictionary.<br/><br/>Unicode characters are currently unprocessed; for example `<ae/` is present in the dictionary instead of `æ`. Ideally, these should all be converted. |
| [web2 revision 326913](https://svnweb.freebsd.org/base/head/share/dict/web2?view=markup&pathrev=326913) | `web2` | |

## Adding additional word lists

To add a word list, say with identifier `x`, put the word list (one word
per line), into a plain text file `x.txt` in the [`raw_data`](raw_data)
directory at the root of the repository. Then, to process the word list
(and all others in the directory) run the script
[`process_raw_data.py`](scripts/process_raw_data.py).

## Installation

Install this with pip with

```
pip install english-words
```

This package is unfortunately rather large (~20MB), and will run into
scaling issues if more word lists or (especially) options are added.
When that bridge is crossed, word lists should possibly be chosen by the
user instead of simply including all of them; word lists could also be
preprocessed on the client side instead of being included in the
package.
