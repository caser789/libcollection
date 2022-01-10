def sort(students):
    max_section = 0
    for name, section in students:
        if section > max_section:
            max_section = section

    counter = [0 for _ in range(max_section+2)]
    for name, section in students:
        counter[section+1] += 1

    for i in range(max_section+1):
        counter[i+1] += counter[i]

    n = len(students)
    aux = [None for _ in range(n)]
    for i in range(n):
        section = students[i][1]
        j = counter[section]
        aux[j] = students[i]
        counter[section] += 1

    for i in range(n):
        students[i] = aux[i]


if __name__ == '__main__':
    students = [
        ("Anderson", 2),
        ("Brown", 3),
        ("Davis", 3),
        ("Garcia", 4),
        ("Harris", 1),
        ("Jackson", 3),
        ("Johnson", 4),
        ("Jones", 3),
        ("Martin", 1),
        ("Martinez", 2),
        ("Miller", 2),
        ("Moore", 1),
        ("Robinson", 2),
        ("Smith", 4),
        ("Taylor", 3),
        ("Thomas", 4),
        ("Thompson", 4),
        ("White", 2),
        ("Williams", 3),
        ("Wilson", 4),
    ]

    students2 = students[:]
    assert students2 == students

    sort(students)
    assert students2 != students

    assert sorted(students2, key=lambda x:x[1]) == students
