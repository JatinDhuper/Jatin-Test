# Task 1:-
#Problem 1:
numbers = [1,2,2,3,3,3,4,4,4,4]
freq = {}

# Counting how many times each number appears
for i in numbers:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

# Convert dictionary into a list of number--count pairs
freq_list = []

for key in freq:
    freq_list.append((key, freq[key]))

# Sort the list based on frequency (largest first)
freq_list.sort(key=lambda x: x[1], reverse=True)

# Print the top 3 most frequent numbers
print("Top 3 most frequent numbers:")

for i in range(3):
    number = freq_list[i][0]
    count = freq_list[i][1]
    print(number, "--", count, "times")

#------------------------------------------------------------------------

#Problem 2:
data = {
    "Aman": [85, 90, 78],
    "Eakam": [92, 88, 95],
    "Kiran": [70, 75, 80]
}

averages = {}  

for student in data:
    scores = data[student]   
    total = 0

    # Add all the scores
    for mark in scores:
        total = total + mark

    # Calculate average
    avg = total / len(scores)

    # Store the average in another dictionary
    averages[student] = avg

# Print the averages
for student in averages:
    print(student + ":", round(averages[student], 1))

# Now find the student with the highest average
top_student = ""
highest_avg = 0

for student in averages:
    if averages[student] > highest_avg:
        highest_avg = averages[student]
        top_student = student

print("Top Student:", top_student)

