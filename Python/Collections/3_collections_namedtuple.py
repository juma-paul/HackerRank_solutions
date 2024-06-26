from collections import namedtuple
from typing import List

def calculate_average(N: int, columns: List[str], student_data: List[str]) -> float:
    """
    Calculate the average marks of students.

    Args:
        N (int): Number of students.
        columns (List[str]): List of column names.
        student_data (List[str]): List of student data as strings.

    Returns:
        float: The average marks of the students.
    """

    Marks = namedtuple('Marks', columns)

    total_marks = 0

    for data in student_data:
        elements = data.split()
        student = Marks(*elements)
        total_marks += int(student.MARKS)
    
    average_marks = total_marks / N
    return average_marks

def main():
    """
    Main function to read input, calculate, and print the average marks.
    """

    N = int(input('Enter the number of students: '))
    columns_names = input('Enter the column names (ID, MARKS, CLASS, NAME) in any order, separated by space: ').upper().split()
    students_data = [input(f'Enter data for student {i+1} (ID, MARKS, CLASS, NAME) separated by space: ').strip() for i in range(N)]
    
    average_marks = calculate_average(N, columns_names, students_data)
    
    print(f'\nThe average marks of the students is: {average_marks:.2f}')

if __name__ == '__main__':
    main()
