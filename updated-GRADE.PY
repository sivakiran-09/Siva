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