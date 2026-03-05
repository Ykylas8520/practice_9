import json

# Example 1: Python to JSON
a = {"name": "Ali", "age": 20}
b = json.dumps(a)
print(b)

# Example 2: JSON to Python
c = json.loads(b)
print(c["name"])

# Example 3: Write JSON file
with open("data.json", "w") as f:
    json.dump(a, f)

# Example 4: Read JSON file
with open("data.json", "r") as f:
    d = json.load(f)
    print(d)

# Example 5: List inside JSON
e = {
    "students": ["Ali", "Sara", "John"],
    "year": 2025
}

with open("students.json", "w") as f:
    json.dump(e, f)

with open("students.json", "r") as f:
    x = json.load(f)
    print(x["students"])
