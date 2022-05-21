# sWAP cASE

# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# Function Description

# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# - string s: the string to modify

# Returns
# - string: the modified string

# Input Format
# A single line containing a string s.

# Constraints
# 0 <len(s) <= 1000

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    inp = input()
    result = swap_case(inp)
    print(result)
