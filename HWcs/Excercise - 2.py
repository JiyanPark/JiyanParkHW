score = input("Enter the score (between 0 and 100): ")

try:
    score = float(score)
    if 0 <= score <= 100:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        else:
            print("Grade: F")
    else:
        print("Error: The score should be between 0 and 100.")
except ValueError:
    print("Error: Please enter a valid numeric value for the score.")
