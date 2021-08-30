# Create a script that has:

#a function accept a list of grades (i.e. [99, 88, 77])

#and returns a grading report for that list.

# Data 
# List of Integers

# blank_list = []
# grades = [99, 75, 89, 45, 68, 94, 87, 86, 80]

# Conditional logic
# A >= 90
# B < 90 and B >= 80
# C < 80 and C >= 70
# D < 70 and D >= 60
# F < 60


#grade = grades[0]
## do logic
#grade = grades[1]
## do logic

# until no more grades left
#ind = 0
#while ind < len(grades):
#    grade = grades[ind]
#    # do logic
#    ind += 1

# def scorer(scores: list):
# accepts a list of scores
# def func_name(param1, param2,...):
def scorer(scores):
    class_scores = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in scores:
        if grade >= 90:
            print(f"{grade} is an A!")
            print(str(grade) + " is an A!")
            # class_scores["A"] = class_scores["A"] + 1
            class_scores["A"] += 1
        elif grade >= 80:
            print(f"{grade} is a B!")
            class_scores["B"] += 1
        elif grade >= 70:
            print(f"{grade} is a C!")
            class_scores["C"] += 1
        elif grade >= 60:
            print(f"{grade} is a D!")
            class_scores["D"] += 1
        else:
            print(f"{grade} is a FAILURE!!!")
            class_scores["F"] += 1
    
    print(class_scores)



grades = [99, 75, 89, 45, 68, 94, 87, 86, 80]
scorer(grades)

print("mrs_ts_grades")

mrs_ts_grades = [101, 22, 55, 77, 88, 99]
scorer(mrs_ts_grades)

print("mr_s_grades")

mr_s_grades = [99, 76, 56, 65]
scorer(mr_s_grades)
# Expected Output
# print out number of A's, B's, etc..

# OR

# dictionary output { "A": 2, "B": 4 ...}


