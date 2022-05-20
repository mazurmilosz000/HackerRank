# Consider a list (list = []). You can perform the following commands:

# 1.insert i e: Insert integer e at position i.
# 2.print: Print the list.
# 3.remove e: Delete the first occurrence of integer e.
# 4.append e: Insert integer e at the end of the list.
# 5.sort: Sort the list.
# 6.pop: Pop the last element from the list.
# 7.reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# Input Format

# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints

# - The elements added to the list must be integers.

# Output Format

# For each command of type print, print the list on a new line.

if __name__ == '__main__':
    N = int(input())
    output = []
    # basic version
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            output.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(output)
        elif cmd[0] == 'remove':
            output.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            output.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            output.sort()
        elif cmd[0] == 'pop':
            output.pop(-1)
        elif cmd[0] == 'reverse':
            output.reverse()
        else:
            raise ValueError

        # fancy version
        # for _ in range(N):
        #     inp = input(). split()
        #     cmd = inp[0]
        #     args = inp[1:]
        #     if cmd == 'print':
        #         print(output)
        #     else:
        #         cmd += '(' + ','.join(args) + ')'
        #         eval('output.' + cmd)
