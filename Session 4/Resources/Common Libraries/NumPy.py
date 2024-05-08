import numpy as np

# Student grades (out of 100)
grades = [85, 90, 88, 72, 95, 84, 91, 78, 80, 87]

# Convert grades list to a NumPy array
grades_array = np.array(grades)

# Statistical Analysis
mean_grade = np.mean(grades_array)
median_grade = np.median(grades_array)
max_grade = np.max(grades_array)
min_grade = np.min(grades_array)
std_deviation = np.std(grades_array)

# Output
print("Mean Grade:", mean_grade)
print("Median Grade:", median_grade)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Standard Deviation:", std_deviation)
