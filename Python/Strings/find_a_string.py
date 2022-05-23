# Find a string

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Constraints
# 1 <= len(string) <= 200
# Each character in string is an ascii character.

# Output format
# Output  the integer number indicating the total number of occurrences of thw substring in the original string.

def count_substring(string, substring):
    count = 0
    while substring in string:
        count += 1
        string = string[string.find(substring)+1:]

    return count


if __name__ == '__main__':

    print(count_substring('ABCDCDC', 'CDC'))
