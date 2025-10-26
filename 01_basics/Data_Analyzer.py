students={
    "Mira": {"math": 88, "Science": 92, "english":85},
    "Aashish": {"math":99, "Science": 96, "english": 98},
    "Rina": {"math": 78, "Science":80, "english": 85}
}

# Find average marks of each students
for name, subjects in students.items():
    avg = sum(subjects.value())/ len(subjects)
    print(f"{name} - Average Marks: {avg:.2f}")

# Find the top scorer
top_student = max(students.items(), key=lambda item: sum(item[1].values()))
print(f"\nTop Student: {top_student[0]}")