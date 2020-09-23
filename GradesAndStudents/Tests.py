import unittest
from Repository import StudentRepo#, GradeRepo
from Controller import StudentController#, GradeController
from Domain import Student, ValidateStudent#, Grade, ValidateGrade
from Exceptions import ValidError, RepoError


class MyTestCase(unittest.TestCase):
    def test_student(self):
        validateStudent = ValidateStudent()
        student = Student(1, 'Name', 'Group')

        validateStudent.validate(student)

        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, 'Name')
        self.assertEqual(student.group, 'Group')
        self.assertEqual(str(student), '1 Name Group')

        student1 = Student(2, 'Name', 'Group')

        self.assertEqual(student, student)
        self.assertFalse(student == student1, True)

        badStudent = Student('x', 100, '')
        try:
            validateStudent.validate(badStudent)
        except ValidError as ve:
            self.assertEqual(str(ve), 'Wrong ID!\nWrong name!\nWrong group!\n')

    def test_repoStudents(self):
        repoStudents = StudentRepo('studentstest', Student.write_student, Student.read_student)
        self.assertEqual(len(repoStudents.getAll()), 0)

        repoStudents.store(Student(1, 'Name', 'Group'))
        self.assertEqual(len(repoStudents.getAll()), 1)

        try:
            repoStudents.store(Student(1, 'Name', 'Group'))
        except RepoError as re:
            self.assertEqual(str(re), 'The object already exists!')
            self.assertEqual(len(repoStudents.getAll()), 1)

        repoStudents.delete(Student(1, None, None))
        self.assertEqual(len(repoStudents.getAll()), 0)

        try:
            repoStudents.delete(Student(1, None, None))
        except RepoError as re:
            self.assertEqual(str(re), 'The object does not exist!')
            self.assertEqual(len(repoStudents.getAll()), 0)

        try:
            repoStudents.find(Student(1, None, None))
        except RepoError as re:
            self.assertEqual(str(re), 'Could not find the object!')

        repoStudents.store(Student(1, 'Name', 'Group'))
        self.assertEqual(repoStudents.find(Student(1, None, None)) == Student(1, 'Name', 'Group'), True)

        repoStudents.saveToFile()
        with open('studentstest', 'r') as f:
            line = f.read()
            self.assertEqual(line, str(Student(1, 'Name', 'Group'))+'\n')

        repoStudents.delete(Student(1, None, None))

    def test_studetController(self):
        repoStudents = StudentRepo('studentstest', Student.write_student, Student.read_student)
        studentController = StudentController(repoStudents)

        studentController.create(1, 'Name', 'Group')
        self.assertEqual(studentController.repo.getAll()[0], Student(1, 'Name', 'Group'))

        studentController.remove(1)
        self.assertEqual(len(studentController.repo.getAll()), 0)


if __name__ == '__main__':
    unittest.main()
