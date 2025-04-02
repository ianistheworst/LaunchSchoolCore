def get_grade(score_1, score_2, score_3):
    mean = ((score_1 + score_2 + score_3) / 3)
    if 90 <= mean <= 100:
        return 'A'
    elif 80 <= mean < 90:
        return 'B'
    elif 70 <= mean < 80:
        return "C"
    elif 60 <= mean < 70:
        return 'D'
    elif 0 <= mean < 60:
        return 'F'
    
print(get_grade(95, 90, 93))
print(get_grade(50, 50, 95))