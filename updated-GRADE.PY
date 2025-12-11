

def get_grade(score):
    if score >= 95: return 'A+'
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

def get_grade_description(grade):
    descriptions = {
        'A+': 'Excellent - Outstanding performance',
        'A': 'Excellent - Very Good performance',
        'B': 'Good - Above average performance',
        'C': 'Average - Satisfactory performance',
        'D': 'Below Average - Passing performance',
        'F': 'Fail - Needs improvement'
    }
    return descriptions.get(grade, 'Unknown grade')

def show_grade_scale():
    print("\nGRADING SCALE:")
    print("A+ (95-100): Excellent - Outstanding performance")
    print("A  (90-94):  Excellent - Very Good performance")
    print("B  (80-89):  Good - Above average performance")
    print("C  (70-79):  Average - Satisfactory performance")
    print("D  (60-69):  Below Average - Passing performance")
    print("F  (0-59):   Fail - Needs improvement\n")

def main():
    while True:
        print("\n1. Check grade for a student\n2. View grade scale\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Goodbye!")
            break
        elif choice == '1':
            try:
                score = float(input("Enter student score (0-100): "))
                if 0 <= score <= 100:
                    grade = get_grade(score)
                    print(f"Grade: {grade}, Description: {get_grade_description(grade)}")
                else:
                    print("Invalid score! Enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == '2':
            show_grade_scale()
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()