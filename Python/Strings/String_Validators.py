# String Validators

# Python has built-in string validation methods for basic data.
# It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# Task
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters,
# digits, lowercase and uppercase characters.

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) < 1000

# Output Format

# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':

    string = input()
    print(any(letter.isalnum() for letter in string))
    print(any(letter.isalpha() for letter in string))
    print(any(letter.isdigit() for letter in string))
    print(any(letter.islower() for letter in string))
    print(any(letter.isupper() for letter in string))
