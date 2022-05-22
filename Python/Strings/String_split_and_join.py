# String split and join

# In Python, a string can be split on a delimiter

# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Function description
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# - string line: a string of space-separated words

# Returns
# - string: the resulting string

# Input format
# The one line contains a string consisting of space separated words.

# Solution using replace method
def split_and_join1(line):
    return line.replace(' ', '-')


# Solution using split and join method
def split_and_join2(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


if __name__ == '__main__':
    inp = input()
    print(split_and_join1(inp))
    print(split_and_join2(inp))
