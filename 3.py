def calculate_average(numbers):
    total = 0
    for number in numbers:
        total+= number
    average = total / len(numbers)
        return average

def classify_average(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"    
    else:
        return "F"

students_scores = [95, 88, 72, 65, 79]
average_scores = calculate_average(students_scores)
letter_grade = classify_average(average_score)
print("Average Scores:", average_score)
print("Letter_Grade", letter_grades)
