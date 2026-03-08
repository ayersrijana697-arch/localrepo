marks = []

print("Enter marks of 6 students")

for i in range(6):
    m = int(input("Enter marks: "))
    marks.append(m)

marks.sort()

print("Sorted marks:", marks)
