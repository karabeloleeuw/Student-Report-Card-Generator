import matplotlib.pyplot as plt

def input_student_data():
    student={}
    student['name']=input("Enter student's name:")
    student['id']=input("Enter student ID:")
    subjects=['Math','English','science','Digital Literacy','History']
    
    grades[]
    print("\nEnter marks out of 100 for the following subjects:")
    for subjects in subjects:
        while True:
            try:
                mark=float(input(f"{subject}:"))
                if 0<= mark <= 100:grades.append(mark) 
                break
                else:prnt("Mark must be between 0 and 100.")
                except valueError:
                    print("Please enter a valid number.")
                    studet['grades']=dict(zip(subjects,grades))
                    return student

def calculate_report(student):
    grades=list(student['grades'].values())
    avg=sum(grades)/len(grades)
    if avg>= 90:
        grade= 'A'
    elif avg>= 80:
        grade= 'B'
    elif avg>= 70
         grade= 'C'
    elif avg>= 60:
        grade= 'D'
    elf avg>= 50:
        grade= 'E'
    else:
        grade= 'F' 
    student['average']= round(avg,2)
    student['final_grade']= grade
    return student                                       

def display_report(student):
    print("\n===Report Card 2025===")
    print(f"Name: {student['name']}")
    print(f"ID: {student['id']}")
    for subject,mark in student['grades'].items():
        print(f"{subject}:{mark}")
        print(f"Average: {student['average']}")
        print(f"Final Grade: {student['final_grade']}")

def visualize_grades(student):
    subjects= list(student['grades'].keys())
    marks= list(student['grades'].values())

    plt.fiugure(figsize=(8,5))
    plt.bar(subjects, marks, color='skyblue')
    plt.title(f"{student['name']}'s Report Card")
    plt.xlabel("Marks")
    plt.ylim(0,100)
    plt.axhline(student['average'], color='red', linestyle='--', label=f"Average:
    {student['average']}")
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Student Report Card Generator")
    print("=" * 50)
    print("Let's get started!\n")
    student = input_student_data()
    student = calculate_report(student)
    display_report(student)
    visualize_grades(student)

if__name__ == "__main__":
main()       