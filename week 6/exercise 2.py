
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
