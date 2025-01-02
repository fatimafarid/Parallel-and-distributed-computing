#CODE2
class StudentDatabase:
    def __init__(self):
        self.students = [
            ("Alice", 22, "Biology"),
            ("Bob", 23, "Mathematics"),
            ("Charlie", 21, "Physics"),
            ("David", 24, "Chemistry")
        ]
        self.student_dict = {}
        self.populate_student_dict()

    def populate_student_dict(self):
        for student in self.students:
            name, age, major = student
            self.student_dict[name] = {"age": age, "major": major}

    def add_student(self, name, age, major):
        self.students.append((name, age, major))
        self.student_dict[name] = {"age": age, "major": major}

    def search_student(self, name):
        if name in self.student_dict:
            return f"{name}: {self.student_dict[name]}"
        else:
            return f"{name} not found."

    def display_students(self):
        for student in self.students:
            print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

def main():
    db = StudentDatabase()
    print("Current Students:")
    db.display_students()

    search_name = input("Enter a student's name to search: ")
    result = db.search_student(search_name)
    print(result)

    add_more = input("Do you want to add a new student? (yes/no): ")
    if add_more.lower() == "yes":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        major = input("Enter the student's major: ")
        db.add_student(name, age, major)
        print(f"Student {name} added successfully!")

    print("\\nUpdated Students List:")
    db.display_students()

if __name__ == "__main__":
    main()
class StudentDatabase:
    def __init__(self):
        self.students = [
            ("Alice", 22, "Biology"),
            ("Bob", 23, "Mathematics"),
            ("Charlie", 21, "Physics"),
            ("David", 24, "Chemistry")
        ]
        self.student_dict = {}
        self.populate_student_dict()

    def populate_student_dict(self):
        for student in self.students:
            name, age, major = student
            self.student_dict[name] = {"age": age, "major": major}

    def add_student(self, name, age, major):
        self.students.append((name, age, major))
        self.student_dict[name] = {"age": age, "major": major}

    def search_student(self, name):
        if name in self.student_dict:
            return f"{name}: {self.student_dict[name]}"
        else:
            return f"{name} not found."

    def display_students(self):
        for student in self.students:
            print(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

def main():
    db = StudentDatabase()
    print("Current Students:")
    db.display_students()

    search_name = input("Enter a student's name to search: ")
    result = db.search_student(search_name)
    print(result)

    add_more = input("Do you want to add a new student? (yes/no): ")
    if add_more.lower() == "yes":
        name = input("Enter the student's name: ")
        age = int(input("Enter the student's age: "))
        major = input("Enter the student's major: ")
        db.add_student(name, age, major)
        print(f"Student {name} added successfully!")

    print("\\nUpdated Students List:")
    db.display_students()

if __name__ == "__main__":
    main()

