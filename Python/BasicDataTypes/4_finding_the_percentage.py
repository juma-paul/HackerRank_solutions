def record_student_marks(num):
    """
    Record student marks in a dictionary with their names as keys and list of scores as values.

    Args:
        num (int): The number of students to record marks for.

    Returns:
        dict: A dictionary of student marks.
    """

    student_marks = {}
    for _ in range(num):
        name, *lyst = input().split()
        scores = list(map(float, lyst))
        student_marks[name] = scores
    return student_marks

def calculate_average(marks):
    """
    Calculate the average of a list of student marks.

    Args:
        marks (list): A list of student marks.

    Returns:
        float: The average of the student's marks.
    """

    return sum(marks) / len(marks) if marks else 0

def main():
    """
    Main method to execute the logic for recording students' marks and calculating the average of a queried student.
    """
    
    n = int(input('Enter number of students to record marks: '))
    student_marks = record_student_marks(n)
    query_name = input('Enter name of student to query: ')

    if query_name in student_marks:
        avg_marks = calculate_average(student_marks[query_name])
        print(f'{avg_marks:.2f}')
    else:
        print("Student's name not found")

if __name__ == '__main__':
    main()
