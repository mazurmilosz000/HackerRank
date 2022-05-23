# Text Wrap

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# - string string: a long string
# - ont max_width: the width to wrap to


# Returns

# - string: a single string with newline characters ('\n') where the breaks should be

# Input format
#  the first line contains a string, 'string'.
# The second line contains the width, 'maxwidth'

# Constraints:
# 0 < len(string) < 1000
# 0 < maxwidth < len(string)

import textwrap


def wrap(s, m_w):
    return textwrap.fill(s, m_w)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
