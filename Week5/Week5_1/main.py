from database import create_table
from user_manager import add_user, view_users, search_user, delete_user,getUserIDByName
from course_manager import add_course,searchCourseByUserAndCourse,getCourseIDByCourseName,enrollUserInCourse
def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Search User by Name and ID")
    print("7. Add Course")
    print("8. Enroll Student for Course")
    print("9. Search Course by User and Course ID")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-8): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            name = input("Enter name: ")
            result = getUserIDByName(name)
            for user in result:
                print(user)
            break
        elif choice == '7':
            name = input("Enter course name: ")
            unit = int(input("Enter number of units: "))
            add_course(name, unit)
        elif choice == '8':
            course_name = input("Enter course name: ")
            course_ids = getCourseIDByCourseName(course_name)
            user_name = input("Enter user name:")
            user_ids = getUserIDByName(user_name)
            enrollUserInCourse(user_ids[0],course_ids[0])
        elif choice == '9':
            course_name = input("Enter course name: ")
            course_ids = getCourseIDByCourseName(course_name)
            user_name = input("Enter user name:")
            user_ids = getUserIDByName(user_name)
            searchCourseByUserAndCourse(course_ids[0],user_ids[0])
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
