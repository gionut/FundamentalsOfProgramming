from Exceptions import ValidError


class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group


    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __eq__(self, other):
        return self.__id == other.id

    def __str__(self):
        return str(self.__id) + ' ' + self.__name + ' ' + self.__group

    @staticmethod
    def read_student(line):
        line = line.split()
        return Student(int(line[0].strip()), line[1].strip(), line[2].strip())

    @staticmethod
    def write_student(object):
        return str(object)


class ValidateStudent:
    def __init__(self):
        pass

    def validate(self, student):
        errors = ''
        if type(student.id) != int:
            errors += 'Wrong ID!\n'
        if type(student.name) != str or student.name == '':
            errors += 'Wrong name!\n'
        if type(student.group) != str or student.group == '':
            errors += 'Wrong group!\n'
        if errors != '':
            raise ValidError(errors)

class Grades:
    def __init__(self, studentId, laboratoryNo, laboratoryProblem, value):
        self.__studentId = studentId
        self.__laboratoryNo = laboratoryNo
        self.__laboratoryProblem = laboratoryProblem
        self.__value = value

    @property
    def studentId(self):
        return self.__studentId

    @property
    def labNo(self):
        return self.__laboratoryNo

    @property
    def labPb(self):
        return self.__laboratoryProblem

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):
        self.__value = x

    def __eq__(self, other):
        return self.__studentId == other.studentId and self.__laboratoryNo == other.labNo

    def __str__(self):
        return str(self.__studentId) + ' ' + str(self.__laboratoryNo) + ' ' \
               + str(self.__laboratoryProblem) + ' ' + str(self.__value)

    @staticmethod
    def  read_grades(line):
        line = line.split()
        if line[3].strip() == 'None':
            line[3] = 0
        return Grades(int(line[0].strip()), int(line[1].strip()), int(line[2].strip()), int(line[3]))

    @staticmethod
    def write_grades(grade):
        return str(grade)

class ValidateGrade:
    def __init__(self):
        pass

    def  validate(self, grade):
        errors = ''
        if grade.value < 0 or grade.value > 10:
            errors += 'Invalid grade!\n'
        if errors != '':
            raise ValidError(errors)

class StudentDTO:
    def __init__(self, student, average):
        self.__student = student
        self.__average = average

    @property
    def average(self):
        return self.__average

    def __str__(self):
        return str(self.__student) + ' ' + str(self.__average)