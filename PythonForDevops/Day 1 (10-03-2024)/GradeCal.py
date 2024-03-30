def grade_score(score):

    if score >= 80:

        return "A++"

    elif score >= 70:

        return "A"

    elif score >= 60:

        return "B"

    elif score >= 50:

        return "C"

    else:

        return "F"

score = float(input("Enter the score: "))

grade = grade_score(score)

print("Grade:", grade)