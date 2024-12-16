# 1.student.mark.py

def input_students():
    students = []
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (DD-MM-YYYY): ")
        students.append((student_id, name, dob))
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(students, courses):
    marks = {}
    for course in courses:
        course_id, course_name = course
        marks[course_id] = {}
        print(f"\nEntering marks for course: {course_name}")
        for student in students:
            student_id, student_name, student_dob = student
            mark = float(input(f"Enter marks for {student_name} (Student ID: {student_id}): "))
            marks[course_id][student_id] = mark
    return marks

def list_courses(courses):
    print("\nList of courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}")

def list_students(students):
    print("\nList of students:")
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

def show_student_marks(marks, students, course_id):
    if course_id in marks:
        print(f"\nMarks for Course ID: {course_id}:")
        for student in students:
            student_id, student_name, _ = student
            if student_id in marks[course_id]:
                mark = marks[course_id][student_id]
                print(f"{student_name}: {mark}")
    else:
        print("Invalid course ID.")

def main():
    # Input student and course information
    students = input_students()
    courses = input_courses()

    # Input marks for each course and student
    marks = input_marks(students, courses)

    # Provide menu options to list courses, students, or show student marks for a given course
    while True:
        print("\nChoose an option:")
        print("1. List Courses")
        print("2. List Students")
        print("3. Show Student Marks for a Course")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            course_id = input("Enter course ID to see student marks: ")
            show_student_marks(marks, students, course_id)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
