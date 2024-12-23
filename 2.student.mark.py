class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"


class Mark:
    def __init__(self):
        self.data = {}

    def add_mark(self, course_id, student_id, mark):
        if course_id not in self.data:
            self.data[course_id] = {}
        self.data[course_id][student_id] = mark

    def get_marks(self, course_id):
        return self.data.get(course_id, {})


class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def input_number(self, prompt):
        while True:
            try:
                number = int(input(prompt))
                if number > 0:
                    return number
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def input_students(self):
        num_students = self.input_number("Enter the number of students: ")
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB (YYYY-MM-DD): ")
            self.students.append(Student(student_id, name, dob))

    def input_courses(self):
        num_courses = self.input_number("Enter the number of courses: ")
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        self.list_courses()
        course_id = input("Select a course ID to input marks: ")
        if any(course.course_id == course_id for course in self.courses):
            print(f"Entering marks for course: {course_id}")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
                        if 0 <= mark <= 100:
                            self.marks.add_mark(course_id, student.student_id, mark)
                            break
                        else:
                            print("Marks should be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid course ID.")

    def list_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("\nStudents:")
        for student in self.students:
            print(student)

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        course_marks = self.marks.get_marks(course_id)
        if course_marks:
            print(f"\nMarks for course {course_id}:")
            for student_id, mark in course_marks.items():
                student_name = next((s.name for s in self.students if s.student_id == student_id), "Unknown")
                print(f"Student ID: {student_id}, Name: {student_name}, Mark: {mark}")
        else:
            print("No marks recorded for this course.")

    def menu(self):
        while True:
            print("\nOptions:")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. List courses")
            print("5. List students")
            print("6. Show marks for a course")
            print("7. Exit")

            option = input("Select an option: ")

            if option == '1':
                self.input_students()
            elif option == '2':
                self.input_courses()
            elif option == '3':
                self.input_marks()
            elif option == '4':
                self.list_courses()
            elif option == '5':
                self.list_students()
            elif option == '6':
                self.show_marks()
            elif option == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    smms = StudentMarkManagementSystem()
    smms.menu()
