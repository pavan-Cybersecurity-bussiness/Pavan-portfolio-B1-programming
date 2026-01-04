score = int(input("Please Enter your score (0-100): "))
if score >= 90:
 grade = "A"
 print("Excellent work!")
elif score >= 80:
 grade = "B"
 print("Good job")
elif score >= 70:
 grade = "C"
elif score >= 60:
  grade= "D"
else:
 grade = "F"

print(f"Your grade is: {grade}")

