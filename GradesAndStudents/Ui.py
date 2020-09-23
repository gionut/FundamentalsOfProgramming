from Exceptions import RepoError, ValidError


class Console:
    def __ui_add_student(self, params):
        if len(params) != 3:
            raise ValueError('add_student function requiers exactly 3 parameters!')

        id = params[0]
        name = params[1]
        group = params[2]

        self.__studentController.create(int(id), name, group)

    def __ui_print_students(self, params):
        if len(params) != 0:
            raise ValueError('pirnt_students function requiers no parameters!')

        list = self.__studentController.getAll()
        for obj in list:
            print(obj)

    def __ui_delete_student(self, params):
        if len(params) != 1:
            raise ValueError('delete_student function requiers exactly one parameter!')
        id = params[0]
        self.__studentController.remove(int(id))

    def __ui_assign_lab(self, params):
        if len(params) != 3:
            raise ValueError('assign_lab function requiers exactly three parameters!')
        studentId = params[0]
        labNo = params[1]
        labPbNo = params[2]
        self.__gradeController.assignLab(int(studentId), int(labNo), int(labPbNo))

    def __ui_assign_to_group(self, params):
        if len(params) != 2:
            raise ValueError('assign_to_group function requiers exactly 2 parameters!')
        group = params[0]
        labNo = params[1]
        self.__gradeController.assign_to_group(group, int(labNo))

    def __ui_grade(self, params):
        if len(params) != 3:
            raise ValueError('grade function requiers exactly 3 parameters!')
        studentId = params[0]
        labNo = params[1]
        grade = params[2]
        self.__gradeController.grade(int(studentId), int(labNo), int(grade))

    def __ui_rank(self, params):
        if len(params) != 1:
            raise ValueError('rank function requiers exactly 1 parameter!')
        group = params[0]
        students = self.__gradeController.rank(group)
        for student in students:
            print(student)

    def __ui_failing(self, params):
        list = self.__gradeController.failing()
        for student in list:
            print(student)

    def __ui_undo(self, params):
        self.

    def __ui_redo(self, params):

    def __init__(self, studentController, gradeController):
        self.__studentController = studentController
        self.__gradeController = gradeController
        self.__commands = {
            'add_student' : self.__ui_add_student,
            'print_students' : self.__ui_print_students,
            'delete_student' : self.__ui_delete_student,
            'assign_lab' : self.__ui_assign_lab,
            'assign_to_group' : self.__ui_assign_to_group,
            'grade' : self.__ui_grade,
            'rank' : self.__ui_rank,
            'failing' : self.__ui_failing,
            'undo' : self.__ui_undo,
            'redo' : self.__ui_redo
        }

    def run(self):
        while True:
            cmd = input('>>>')
            if cmd == 'exit':
                return
            if cmd == '':
                continue
            parts = cmd.split()
            command = parts[0]
            params = parts[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](params)
                except ValueError as ve:
                    print("Ui Error!\n" + str(ve))
                except RepoError as re:
                    print("Infrastructure Error!\n" + str(re))
                except ValidError as vi:
                    print('Business Error!\n' + str(vi))
            else:
                print("Invalid command!")
