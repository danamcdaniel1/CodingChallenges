from collections import OrderedDict


def unique_char_counts(string):
    """
    Count all of the unique characters in a string.  Sorts the chars before counting.
    it assumes the input string is alphabetical only.

    :param str: This is the string to be compressed.  e.g. 'aaabbbc'
    :return: string in format ([letter][number])*.  e.g. 'a3b3c'
    """

    unique = sorted(string)
    compressed = ""

    dict = OrderedDict.fromkeys(unique, 0)
    for ch in string:
        dict[ch] += 1

    for key, value in dict.items():
        compressed = compressed + key + str(dict[key])
    return compressed


def run_length_encoding(string):
    """
    Perform char-sized Run Length Encoding to compress a string into a smaller size.
    Returns the original string if the original string is smaller.

    e.g. 'AAAABBBBBBDAAA' --> A4B6D1A3
    e.g. 'bookkeeper' --> bookkeeper  (not b1o2k2e2p1e1r1)

    :param str: This is the string to be compressed.  e.g. 'aaabbbaaa'
    :return: string in format ([letter][number])*.  e.g. 'a3b3a3
    """


    compressed = ''
    count = 1
    prev = string[0]
    for i in string[1:]:
        if i == prev:
            count += 1
        else:
            compressed = compressed + prev + str(count)
            count = 1
            prev = i

    # for loop doesn't hit last letter
    compressed = compressed + prev + str(count)

    # return string if it's too short
    if len(compressed) <= len(string):
        return compressed
    else:
        return string
