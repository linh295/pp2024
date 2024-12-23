import math
import numpy as np
import curses

class Student:
    def __init__(self):
        self.__id = input("Enter the student's id: ")
        self.__name = input("Enter the student's name: ")
        self.__dob = input("Enter the student's dob: ")
        self.__scores = []  # List of tuples (course_id, score, credit)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_score(self, course_id, score, credit):
        # Round score down to one decimal place
        score = math.floor(score * 10) / 10
        self.__scores.append((course_id, score, credit))

    def calculate_gpa(self):
        if not self.__scores:
            return 0
        scores_array = np.array([s[1] for s in self.__scores])
        credits_array = np.array([s[2] for s in self.__scores])
        weighted_sum = np.sum(scores_array * credits_array)
        total_credits = np.sum(credits_array)
        return round(weighted_sum / total_credits, 2) if total_credits > 0 else 0

    def get_scores(self):
        return self.__scores

class Course:
    def __init__(self):
        self.__id = input("Enter the course's id: ")
        self.__name = input("Enter the course's name: ")
        self.__credits = int(input("Enter the course's credits: "))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits

class Utils:
    @staticmethod
    def input_something(args):
        while True:
            try:
                value = int(input(f"Enter the number of {args}: "))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def show(items):
        if not items:
            print("No items available.")
            return
        for i, item in enumerate(items):
            if isinstance(item, Student):
                print(f"{i + 1}. {item.get_id()} - {item.get_name()} - GPA: {item.calculate_gpa()}")
            elif isinstance(item, Course):
                print(f"{i + 1}. {item.get_id()} - {item.get_name()} - Credits: {item.get_credits()}")

class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def set_num_students(self):
        self.__num_students = Utils.input_something("students")

    def set_num_courses(self):
        self.__num_courses = Utils.input_something("courses")

    def set_students(self):
        if self.__num_students == 0:
            print("Please set the number of students first.")
            return
        self.__students.clear()
        for _ in range(self.__num_students):
            self.__students.append(Student())

    def set_courses(self):
        if self.__num_courses == 0:
            print("Please set the number of courses first.")
            return
        self.__courses.clear()
        for _ in range(self.__num_courses):
            self.__courses.append(Course())

    def add_scores(self):
        if not self.__students or not self.__courses:
            print("Please ensure students and courses are set up first.")
            return

        for student in self.__students:
            print(f"Adding scores for {student.get_name()} ({student.get_id()})")
            for course in self.__courses:
                score = float(input(f"Enter score for {course.get_name()} ({course.get_id()}): "))
                student.add_score(course.get_id(), score, course.get_credits())

    def list_students(self):
        if not self.__students:
            print("No students available.")
            return
        print("Student list:")
        Utils.show(self.__students)

    def list_courses(self):
        if not self.__courses:
            print("No courses available.")
            return
        print("Course list:")
        Utils.show(self.__courses)

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda s: s.calculate_gpa(), reverse=True)

# UI with curses

def curses_main(stdscr):
    univ = University()

    while True:
        stdscr.clear()
        stdscr.addstr("Options:\n")
        stdscr.addstr("0. Exit\n")
        stdscr.addstr("1. Input number of students\n")
        stdscr.addstr("2. Input number of courses\n")
        stdscr.addstr("3. Input student details\n")
        stdscr.addstr("4. Input course details\n")
        stdscr.addstr("5. Add student scores\n")
        stdscr.addstr("6. List students\n")
        stdscr.addstr("7. List courses\n")
        stdscr.addstr("8. Sort students by GPA\n")
        stdscr.addstr("Your choice: ")
        stdscr.refresh()

        try:
            option = int(stdscr.getkey())
        except ValueError:
            continue

        if option == 0:
            break
        elif option == 1:
            univ.set_num_students()
        elif option == 2:
            univ.set_num_courses()
        elif option == 3:
            univ.set_students()
        elif option == 4:
            univ.set_courses()
        elif option == 5:
            univ.add_scores()
        elif option == 6:
            univ.list_students()
        elif option == 7:
            univ.list_courses()
        elif option == 8:
            univ.sort_students_by_gpa()
        else:
            stdscr.addstr("Invalid input. Please try again!\n")

        stdscr.addstr("Press any key to continue...\n")
        stdscr.refresh()
        stdscr.getkey()

if _name_ == "_main_":
    curses.wrapper(curses_main)