class StudentController:
    def __init__(self, id, name, gender, age, math, physic, chemistry):
        self._id = id
        self._name = name
        self._gender = gender
        self._age = age
        self._math = math
        self._physic = physic
        self._chemistry = chemistry
        self._gpa = 0
        self._status = ""

