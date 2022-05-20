# Nested Lists

# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names
# alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students.
# The 2 N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints
# - 2 <= N <= 5
# - There will always be one or more students having the second lowest grade.

# Output Format

# Print the name(s) of any student(s) having the second lowest grade in.
# If there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        python_students.append([name, score])

    grades = sorted(set(([x[1] for x in python_students])))
    second_lowest = grades[1]
    second_students = []
    for x in python_students:
        if second_lowest == x[1]:
            second_students.append(x[0])

    for student in sorted(second_students):
        print(student)