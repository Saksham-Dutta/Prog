
student_db = []

def display_menu():
    print("\n" + "="*30)
    print(" STUDENT RECORD SYSTEM ")
    print("="*30)
    print("1. Add Student Record")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Record")
    print("5. Delete Student Record")
    print("6. Exit")
    print("="*30)

def add_student():
    print("\n--- Add Student Record ---")
    student_id = input("Enter Student ID: ").strip()
    
 
    for student in student_db:
        if student['id'] == student_id:
            print("❌ Error: A student with this ID already exists!")
            return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    grade = input("Enter Grade: ").strip()
 
    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'course': course,
        'grade': grade
    }
    
    student_db.append(student)
    print(" Student record added successfully!")

def view_students():
    print("\n--- View All Students ---")
    if not student_db:
        print("No records found.")
        return
 
    print(f"{'ID':<10} {'Name':<20} {'Age':<6} {'Course':<15} {'Grade':<6}")
    print("-" * 60)
    for student in student_db:
        print(f"{student['id']:<10} {student['name']:<20} {student['age']:<6} {student['course']:<15} {student['grade']:<6}")

def search_student():
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID to search: ").strip()
    
    for student in student_db:
        if student['id'] == student_id:
            print("\n Record Found:")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Grade: {student['grade']}")
            return
            
    print("❌ Student record not found.")

def update_student():
    print("\n--- Update Student Record ---")
    student_id = input("Enter Student ID to update: ").strip()
    
    for student in student_db:
        if student['id'] == student_id:
            print(f"Found record for {student['name']}. Leave blank to keep current value.")
            
            new_name = input(f"Enter new Name ({student['name']}): ").strip()
            new_age = input(f"Enter new Age ({student['age']}): ").strip()
            new_course = input(f"Enter new Course ({student['course']}): ").strip()
            new_grade = input(f"Enter new Grade ({student['grade']}): ").strip()
            
          
            if new_name: student['name'] = new_name
            if new_age: student['age'] = new_age
            if new_course: student['course'] = new_course
            if new_grade: student['grade'] = new_grade
            
            print(" Student record updated successfully!")
            return
            
    print(" Student record not found.")

def delete_student():
    print("\n--- Delete Student Record ---")
    student_id = input("Enter Student ID to delete: ").strip()
    
    for student in student_db:
        if student['id'] == student_id:
            student_db.remove(student)
            print("Student record deleted successfully!")
            return
            
    print(" Student record not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("\nThank you for using the Student Record System. Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()