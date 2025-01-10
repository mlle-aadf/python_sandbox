def main():
    score = int(input("Enter score: "))
    print(grade(score))

def grade(score):
    if score >= 90:
        return "Grade: A" 
    elif score >= 80:
        return "Grade: B"
    elif score >= 70:
        return "Grade: C"
    elif score >= 60:
        return "Grade: D"
    else:
        return "Grade: F"
    
main()