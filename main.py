import pandas as pd
import numpy as np

data = pd.read_csv("students.csv")
print(data)

print("\nColumn Names:")
print(data.columns)

print("\nNumber of Students:")
print(len(data))

print("\nBasic Information:")
data.info()

data["Total"] = data["Python"] + data["Maths"] + data["English"] + data["Physics"] + data["Chemistry"] + data["Biology"]

data["Average"] = data["Total"] / 6
data["Average"] = data["Average"].round(2)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


grades = []

for average in data["Average"]:
    grade = calculate_grade(average)
    grades.append(grade)

data["Grade"] = grades


def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


results = []

for average in data["Average"]:
    result = check_result(average)
    results.append(result)

data["Result"] = results


print("\nStudent Performance:")
print(data)


marks = np.array(data["Average"])

highest_average = np.max(marks)
lowest_average = np.min(marks)
class_average = np.mean(marks)


python_average = np.mean(data["Python"])
maths_average = np.mean(data["Maths"])
english_average = np.mean(data["English"])
physics_average = np.mean(data["Physics"])
chemistry_average = np.mean(data["Chemistry"])
biology_average = np.mean(data["Biology"])

subject_averages = {
    "Python": python_average,
    "Maths": maths_average,
    "English": english_average,
    "Physics": physics_average,
    "Chemistry": chemistry_average,
    "Biology": biology_average
}

best_subject = max(subject_averages, key=subject_averages.get)


print("\nClass Analysis:")
print("Highest Average:", highest_average)
print("Lowest Average:", lowest_average)
print("Class Average:", round(class_average, 2))


print("\nSubject-wise Average:")
print("Python:", round(python_average, 2))
print("Maths:", round(maths_average, 2))
print("English:", round(english_average, 2))
print("Physics:", round(physics_average, 2))
print("Chemistry:", round(chemistry_average, 2))
print("Biology:", round(biology_average, 2))

print("Best Subject:", best_subject)


passed_students = (data["Result"] == "Pass").sum()
failed_students = (data["Result"] == "Fail").sum()

print("\nResult:")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)


top_students = data.sort_values("Average", ascending=False).head(3)

print("\nTop 3 Students:")
print(top_students[["Name", "Average", "Grade"]])