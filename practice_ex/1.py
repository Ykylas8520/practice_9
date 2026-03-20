from functools import reduce

students = [
    ("Aidos", 95),
    ("Olzhas", 90),
    ("Nurasyl", 82),
]

scores = [x[1] for x in students]

total = len(students)

total_score = sum(scores)

max = max(scores)
min = min(scores)

avg = total_score / total

plus5 = list(map(lambda x: x+5, scores))

top = list(filter(lambda x: x[1] > 85, students))

prod = reduce(lambda x,y: x*y, scores)

print("Enumerate:")
for i, (n,s) in enumerate(students, 1):
    print(i, n, s)

names = [x[0] for x in students]
z = list(zip(names, scores))
print("Zip:", z)

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted:")
for n,s in sorted_students:
    print(n, s)

with open("report.txt", "w") as f:
    f.write(f"Total students: {total}\n")
    f.write(f"Average score: {avg}\n")
    f.write(f"Highest score: {max}\n")
    f.write(f"Lowest score: {min}\n\n")

    f.write("Top students:\n")
    for n,s in top:
        f.write(f"{n} {s}\n")