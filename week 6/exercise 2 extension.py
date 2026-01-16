
# part A data collection
student_records = []

for i in range(6):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))

    score_dict = {"score": score}

    student_tuple = (name, score_dict)

    student_records.append(student_tuple)

#Part b
scores = []

for name, data in student_records:
    scores.append(data["score"])
#using a dictionary for easier refrence
stats = {
    "highest": max(scores),
    "lowest": min(scores),
    "average": sum(scores) / len(scores)
}

print("Statistics:")
print("Highest:", stats["highest"])
print("Lowest:", stats["lowest"])
print("Average:", stats["average"])

# unique grades
unique_scores = set(scores)
unique_scores = sorted(unique_scores) # ordering the scores

print("Unique scores:", unique_scores)


# part d Grade distrubutiona
grade_distribution = {}
# checking unique scores and appending them in a dictionary
for score in scores:
    if score in grade_distribution:
        grade_distribution[score] += 1
    else:
        grade_distribution[score] = 1

print("Grade Distribution:")
for score, count in grade_distribution.items():
    print(score, ":", count, "student(s)")

"""Extension"""

# assign letter grades to each student
for i, (name, data) in enumerate(student_records): # enumerate adds index
    score = data["score"]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # add letter grade to the dictionary
    student_records[i] = (name, {"score": score, "grade": grade})

print("\nStudents with letter grades:")
for name, data in student_records:
    print(f"{name}: {data['score']} → {data['grade']}")
# median
sorted_scores = sorted(scores)
n = len(sorted_scores)

if n % 2 == 1:  # odd number of scores
    median = sorted_scores[n // 2]
else:           # even number of scores
    median = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2

print("\nMedian score:", median)

# Identify Students Above/Below Average
above_avg = []
below_avg = []

for name, data in student_records:
    if data["score"] > stats["average"]:
        above_avg.append(name)
    else:
        below_avg.append(name)

print("\nStudents above average:", above_avg)
print("Students below average:", below_avg)

#Save Results to JSON File
import json

results = {
    "students": student_records,
    "statistics": stats,
    "unique_scores": unique_scores,
    "grade_distribution": grade_distribution
}

with open("student_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nResults saved to student_results.json")
