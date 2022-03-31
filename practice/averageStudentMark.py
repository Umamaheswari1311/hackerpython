n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum = 0
count = 0
for marks in student_marks[query_name]:
    sum += marks
    count += 1
average = "{:.2f}".format(sum / count)
print(average)



