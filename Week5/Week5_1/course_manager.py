from database import create_connection
import sqlite3

def add_course(name, unit):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (name, unit) VALUES (?, ?)", (name, unit))
        conn.commit()
        print(" course added successfully.")
    except sqlite3.IntegrityError:
        print(" unit must be unique.")
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_course(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")

def getCourseIDByCourseName(name):
    conn = create_connection()  # Open connection
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM courses WHERE name = ?", (name,))
    row = cursor.fetchone()
    
    if row:  # Check if a user was found
        id = row[0]
        cursor.execute("SELECT * FROM courses WHERE name = ? AND id = ?", (name, id))
        rows = cursor.fetchall()
    else:
        rows = []  # No rows found

    conn.close()  # Close the connection after all operations
    return rows

def searchCourseByUserAndCourse(course_id, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT users.name, users.email, courses.name, courses.unit
        FROM user_courses
        JOIN users ON user_courses.user_id = users.id
        JOIN courses ON user_courses.course_id = courses.id
        WHERE users.id = ? AND courses.id = ?
    ''', (user_id, course_id))
    result = cursor.fetchall()
    conn.close()

    
    print("🎯 Enrolled Course Details:")
    for row in result:
        print(f"User: {row[0]} | Email: {row[1]} | Course: {row[2]} | Unit: {row[3]}")


def enrollUserInCourse(user_id,course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_courses (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
    conn.commit()
    conn.close()

