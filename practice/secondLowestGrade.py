list = []
grade = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    list.append([name, score])
    grade.append(score)
secondGrade = sorted(set(grade))[1]
orderName = []

for iterate in list:
    if (iterate[1] == secondGrade):
        orderName.append(iterate[0])

orderName = sorted(orderName)

for n in orderName:
    print(n)