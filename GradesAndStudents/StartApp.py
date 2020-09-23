from Domain import Student, Grades
from Repository import StudentRepo, GradeRepo
from Controller import StudentController, GradeController
from Ui import Console


# Create the repositories
studentRepo = StudentRepo('students', Student.write_student, Student.read_student)
gradeRepo = GradeRepo('grades', Grades.write_grades, Grades.read_grades)


# Create the controllers
studenController = StudentController(studentRepo)
gradeController = GradeController(gradeRepo, studentRepo)


# Create the console
console = Console(studenController, gradeController)

console.run()

