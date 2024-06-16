def main():
    # Get student's records
    num_students = int(input('How many students are in the class? '))

    records = []
    for _ in range(num_students):
        name = input('Enter student\'s name: ')
        score = float(input('What is the score? '))
        records.append([name, score])

    # Find second lowest score
    scores = sorted(set([record[1] for record in records]))

    if len(scores) < 2:
        print('Scores are not enough to determine second-lowest.')
    
    second_lowest_score = scores[1]

    # Find names of students with second-lowest score
    name_with_second_lowest_score = sorted(record[0] for record in records if record[1] == second_lowest_score)

    # Print names in ascending order
    for name in name_with_second_lowest_score:
        print(name)
    
    

if __name__ == '__main__':
    main()
