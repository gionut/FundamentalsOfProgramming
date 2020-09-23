from Domain import Student, ValidateStudent, Grades, ValidateGrade, StudentDTO
from Exceptions import ValidError
import copy


class StudentController():
    def __init__(self, repoStudents):
        self.repo = repoStudents
        self.undorepo = repoStudents
        self.__validateStudent = ValidateStudent()

    def create(self, id, name, group):
        student = Student(id, name, group)
        self.__validateStudent.validate(student)
        self.undorepo = copy.deepcopy(self.repo)
        self.repo.store(student)



    def remove(self, studentId):
        student = Student(studentId, None, None)
        self.repo.delete(student)

    def getAll(self):
        list = self.repo.getAll()
        students = []
        for obj in list:
            students.append(str(obj))
        return students



class GradeController:
    def __init__(self, gradeRepo, studentRepo):
        self.gradeRepo = gradeRepo
        self.studentRepo = studentRepo
        self.__validateGrades = ValidateGrade()

    def assignLab(self, studentId, labNo, labProblemNo):
        student = Student(studentId, None, None)
        if student not in self.studentRepo.getAll():
            raise ValidError('The student does not exist!')
        lab = Grades(studentId, labNo, labProblemNo, 0)
        self.gradeRepo.store(lab)

    def assign_to_group(self, group, labNo):
        count = 1
        for student in self.studentRepo.getAll():
            if student.group == group:
                grade = Grades(student.id, labNo, None, None)
                if grade not in self.gradeRepo.getAll(student.id):
                    lab = Grades(student.id, labNo, count, 0)
                    count += 1
                    self.gradeRepo.store(lab)

    def grade(self, studentId, laboratoryNo, val):
        grade = Grades(None, None, None, val)
        self.__validateGrades.validate(grade)
        student = Student(studentId, None, None)
        if student not in self.studentRepo.getAll():
            raise ValidError('The student does not exist!')
        for grade in self.gradeRepo.getAll(studentId):
            if grade.labNo == laboratoryNo:
                grade.value = val
                self.gradeRepo.update()

    def rank(self, group):
        students = []
        for student in self.studentRepo.getAll():
            if student.group == group:
                students.append(self.calc_average(student))

        students.sort(key=lambda x: x.average , reverse=True)
        list = []
        for student in students:
            list.append(str(student))
        return list

    def calc_average(self, student):
        average = 0.00
        count = 0
        for grade in self.gradeRepo.getAll(student.id):
            count += 1
            average += grade.value
        if count == 0:
            count = 1
        average = average / count
        student = StudentDTO(student, average)
        return student

    def failing(self):
        students = []
        for student in self.studentRepo.getAll():
            s = self.calc_average(student)
            if s.average < 5 and s. average != 0:
                students.append(s)
        return students





