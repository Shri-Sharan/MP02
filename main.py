import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Database connection
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admmin@%%*',
            database='EduSchema'
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Course Management Functions
def add_course(conn, course_name, description, start_date, end_date):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Courses (CourseName, Description, StartDate, EndDate)
            VALUES (%s, %s, %s, %s)
        """, (course_name, description, start_date, end_date))
        conn.commit()
        messagebox.showinfo("Success", "Course added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def update_course(conn, course_id, course_name, description, start_date, end_date):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Courses
            SET CourseName = %s, Description = %s, StartDate = %s, EndDate = %s
            WHERE CourseID = %s
        """, (course_name, description, start_date, end_date, course_id))
        conn.commit()
        messagebox.showinfo("Success", "Course updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def remove_course(conn, course_id):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Courses WHERE CourseID = %s", (course_id,))
        conn.commit()
        messagebox.showinfo("Success", "Course removed successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def search_courses(conn, keyword):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT * FROM Courses
            WHERE CourseName LIKE %s OR Description LIKE %s
        """, (f"%{keyword}%", f"%{keyword}%"))
        courses = cursor.fetchall()
        return courses
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()

def sort_courses(conn, column):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(f"SELECT * FROM Courses ORDER BY {column}")
        courses = cursor.fetchall()
        return courses
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()

# Instructor Management Functions
def add_instructor(conn, first_name, last_name, email, phone_number):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Instructors (FirstName, LastName, Email, PhoneNumber)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, email, phone_number))
        conn.commit()
        messagebox.showinfo("Success", "Instructor added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def update_instructor(conn, instructor_id, first_name, last_name, email, phone_number):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE Instructors
            SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s
            WHERE InstructorID = %s
        """, (first_name, last_name, email, phone_number, instructor_id))
        conn.commit()
        messagebox.showinfo("Success", "Instructor updated successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def remove_instructor(conn, instructor_id):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Instructors WHERE InstructorID = %s", (instructor_id,))
        conn.commit()
        messagebox.showinfo("Success", "Instructor removed successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def assign_instructor_to_course(conn, course_id, instructor_id):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO CourseInstructors (CourseID, InstructorID)
            VALUES (%s, %s)
        """, (course_id, instructor_id))
        conn.commit()
        messagebox.showinfo("Success", "Instructor assigned to course successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

# Student Enrollment Functions
def enroll_student(conn, student_name, course_id):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Students (StudentName, CourseID)
            VALUES (%s, %s)
        """, (student_name, course_id))
        conn.commit()
        messagebox.showinfo("Success", "Student enrolled successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def track_student_progress(conn, student_id):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT * FROM StudentProgress
            WHERE StudentID = %s
        """, (student_id,))
        progress = cursor.fetchall()
        return progress
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()

# Assessment and Grades Functions
def add_assessment(conn, course_id, assessment_name, max_score):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Assessments (CourseID, AssessmentName, MaxScore)
            VALUES (%s, %s, %s)
        """, (course_id, assessment_name, max_score))
        conn.commit()
        messagebox.showinfo("Success", "Assessment added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def add_grade(conn, student_id, assessment_id, score):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Grades (StudentID, AssessmentID, Score)
            VALUES (%s, %s, %s)
        """, (student_id, assessment_id, score))
        conn.commit()
        messagebox.showinfo("Success", "Grade added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()

def view_grades(conn, student_id):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT * FROM Grades
            WHERE StudentID = %s
        """, (student_id,))
        grades = cursor.fetchall()
        return grades
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
        return []
    finally:
        cursor.close()

# GUI Functions
def main():
    conn = connect_to_db()
    if conn is None:
        return

    root = Tk()
    root.title("EduSchema Management System")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Course Management Tab
    course_frame = Frame(notebook)
    notebook.add(course_frame, text="Course Management")

    Label(course_frame, text="Course Management", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    Label(course_frame, text="Course Name:").grid(row=1, column=0, padx=10, pady=5)
    course_name_entry = Entry(course_frame, width=30)
    course_name_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(course_frame, text="Description:").grid(row=2, column=0, padx=10, pady=5)
    description_entry = Entry(course_frame, width=30)
    description_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(course_frame, text="Start Date (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
    start_date_entry = Entry(course_frame, width=30)
    start_date_entry.grid(row=3, column=1, padx=10, pady=5)

    Label(course_frame, text="End Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    end_date_entry = Entry(course_frame, width=30)
    end_date_entry.grid(row=4, column=1, padx=10, pady=5)

    Label(course_frame, text="Course ID (for update/remove):").grid(row=5, column=0, padx=10, pady=5)
    course_id_entry = Entry(course_frame, width=30)
    course_id_entry.grid(row=5, column=1, padx=10, pady=5)

    def add_course_command():
        add_course(conn, course_name_entry.get(), description_entry.get(), start_date_entry.get(), end_date_entry.get())

    def update_course_command():
        update_course(conn, course_id_entry.get(), course_name_entry.get(), description_entry.get(), start_date_entry.get(), end_date_entry.get())

    def remove_course_command():
        remove_course(conn, course_id_entry.get())

    def search_courses_command():
        courses = search_courses(conn, course_name_entry.get())
        search_results_text.config(state=NORMAL)
        search_results_text.delete(1.0, END)
        for course in courses:
            search_results_text.insert(END, f"{course['CourseID']} | {course['CourseName']} | {course['Description']} | {course['StartDate']} | {course['EndDate']}\n")
        search_results_text.config(state=DISABLED)

    def sort_courses_command():
        courses = sort_courses(conn, sort_by_combobox.get())
        search_results_text.config(state=NORMAL)
        search_results_text.delete(1.0, END)
        for course in courses:
            search_results_text.insert(END, f"{course['CourseID']} | {course['CourseName']} | {course['Description']} | {course['StartDate']} | {course['EndDate']}\n")
        search_results_text.config(state=DISABLED)

    Button(course_frame, text="Add Course", width=15, command=add_course_command).grid(row=6, column=0, pady=10)
    Button(course_frame, text="Update Course", width=15, command=update_course_command).grid(row=6, column=1, pady=10)
    Button(course_frame, text="Remove Course", width=15, command=remove_course_command).grid(row=6, column=2, pady=10)
    Button(course_frame, text="Search Courses", width=15, command=search_courses_command).grid(row=5, column=2, padx=10, pady=5)

    sort_by_combobox = ttk.Combobox(course_frame, values=['CourseID', 'CourseName', 'StartDate', 'EndDate'], width=15)
    sort_by_combobox.grid(row=6, column=3, padx=10, pady=5)
    sort_by_combobox.current(0)
    sort_button = Button(course_frame, text="Sort Courses", width=15, command=sort_courses_command)
    sort_button.grid(row=6, column=4, padx=10, pady=5)

    search_results_text = Text(course_frame, height=10, width=80)
    search_results_text.grid(row=7, column=0, columnspan=5, padx=10, pady=10)
    search_results_text.config(state=DISABLED)

    # Instructor Management Tab
    instructor_frame = Frame(notebook)
    notebook.add(instructor_frame, text="Instructor Management")

    Label(instructor_frame, text="Instructor Management", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    Label(instructor_frame, text="First Name:").grid(row=1, column=0, padx=10, pady=5)
    first_name_entry = Entry(instructor_frame, width=30)
    first_name_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(instructor_frame, text="Last Name:").grid(row=2, column=0, padx=10, pady=5)
    last_name_entry = Entry(instructor_frame, width=30)
    last_name_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(instructor_frame, text="Email:").grid(row=3, column=0, padx=10, pady=5)
    email_entry = Entry(instructor_frame, width=30)
    email_entry.grid(row=3, column=1, padx=10, pady=5)

    Label(instructor_frame, text="Phone Number:").grid(row=4, column=0, padx=10, pady=5)
    phone_number_entry = Entry(instructor_frame, width=30)
    phone_number_entry.grid(row=4, column=1, padx=10, pady=5)

    Label(instructor_frame, text="Instructor ID (for update/remove):").grid(row=5, column=0, padx=10, pady=5)
    instructor_id_entry = Entry(instructor_frame, width=30)
    instructor_id_entry.grid(row=5, column=1, padx=10, pady=5)

    def add_instructor_command():
        add_instructor(conn, first_name_entry.get(), last_name_entry.get(), email_entry.get(), phone_number_entry.get())

    def update_instructor_command():
        update_instructor(conn, instructor_id_entry.get(), first_name_entry.get(), last_name_entry.get(), email_entry.get(), phone_number_entry.get())

    def remove_instructor_command():
        remove_instructor(conn, instructor_id_entry.get())

    Button(instructor_frame, text="Add Instructor", width=15, command=add_instructor_command).grid(row=6, column=0, pady=10)
    Button(instructor_frame, text="Update Instructor", width=15, command=update_instructor_command).grid(row=6, column=1, pady=10)
    Button(instructor_frame, text="Remove Instructor", width=15, command=remove_instructor_command).grid(row=6, column=2, pady=10)

    # Student Enrollment Tab
    student_frame = Frame(notebook)
    notebook.add(student_frame, text="Student Enrollment")

    Label(student_frame, text="Student Enrollment", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    Label(student_frame, text="Student Name:").grid(row=1, column=0, padx=10, pady=5)
    student_name_entry = Entry(student_frame, width=30)
    student_name_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(student_frame, text="Course ID:").grid(row=2, column=0, padx=10, pady=5)
    student_course_id_entry = Entry(student_frame, width=30)
    student_course_id_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(student_frame, text="Student ID (for tracking progress):").grid(row=3, column=0, padx=10, pady=5)
    track_student_id_entry = Entry(student_frame, width=30)
    track_student_id_entry.grid(row=3, column=1, padx=10, pady=5)

    def enroll_student_command():
        enroll_student(conn, student_name_entry.get(), student_course_id_entry.get())

    def track_progress_command():
        progress = track_student_progress(conn, track_student_id_entry.get())
        progress_text.config(state=NORMAL)
        progress_text.delete(1.0, END)
        for p in progress:
            progress_text.insert(END, f"{p['StudentID']} | {p['CourseID']} | {p['Progress']}\n")
        progress_text.config(state=DISABLED)

    Button(student_frame, text="Enroll Student", width=15, command=enroll_student_command).grid(row=4, column=0, pady=10)
    Button(student_frame, text="Track Progress", width=15, command=track_progress_command).grid(row=4, column=1, pady=10)

    progress_text = Text(student_frame, height=10, width=80)
    progress_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    progress_text.config(state=DISABLED)

    # Assessment and Grades Tab
    assessment_frame = Frame(notebook)
    notebook.add(assessment_frame, text="Assessment and Grades")

    Label(assessment_frame, text="Assessment and Grades", font=("Arial", 18)).grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    Label(assessment_frame, text="Course ID:").grid(row=1, column=0, padx=10, pady=5)
    assessment_course_id_entry = Entry(assessment_frame, width=30)
    assessment_course_id_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(assessment_frame, text="Assessment Name:").grid(row=2, column=0, padx=10, pady=5)
    assessment_name_entry = Entry(assessment_frame, width=30)
    assessment_name_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(assessment_frame, text="Max Score:").grid(row=3, column=0, padx=10, pady=5)
    max_score_entry = Entry(assessment_frame, width=30)
    max_score_entry.grid(row=3, column=1, padx=10, pady=5)

    Label(assessment_frame, text="Student ID (for adding/viewing grades):").grid(row=4, column=0, padx=10, pady=5)
    grade_student_id_entry = Entry(assessment_frame, width=30)
    grade_student_id_entry.grid(row=4, column=1, padx=10, pady=5)

    Label(assessment_frame, text="Assessment ID:").grid(row=5, column=0, padx=10, pady=5)
    grade_assessment_id_entry = Entry(assessment_frame, width=30)
    grade_assessment_id_entry.grid(row=5, column=1, padx=10, pady=5)

    Label(assessment_frame, text="Score:").grid(row=6, column=0, padx=10, pady=5)
    score_entry = Entry(assessment_frame, width=30)
    score_entry.grid(row=6, column=1, padx=10, pady=5)

    def add_assessment_command():
        add_assessment(conn, assessment_course_id_entry.get(), assessment_name_entry.get(), max_score_entry.get())

    def add_grade_command():
        add_grade(conn, grade_student_id_entry.get(), grade_assessment_id_entry.get(), score_entry.get())

    def view_grades_command():
        grades = view_grades(conn, grade_student_id_entry.get())
        grades_text.config(state=NORMAL)
        grades_text.delete(1.0, END)
        for grade in grades:
            grades_text.insert(END, f"{grade['GradeID']} | {grade['StudentID']} | {grade['AssessmentID']} | {grade['Score']}\n")
        grades_text.config(state=DISABLED)

    Button(assessment_frame, text="Add Assessment", width=15, command=add_assessment_command).grid(row=7, column=0, pady=10)
    Button(assessment_frame, text="Add Grade", width=15, command=add_grade_command).grid(row=7, column=1, pady=10)
    Button(assessment_frame, text="View Grades", width=15, command=view_grades_command).grid(row=7, column=2, pady=10)

    grades_text = Text(assessment_frame, height=10, width=80)
    grades_text.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
    grades_text.config(state=DISABLED)

    root.mainloop()

if __name__ == "__main__":
    main()
