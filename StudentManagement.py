import math
from Student import StudentController


class StudentManagementController:
    list_student = []  # Khoi tao 1 list de luu tru sinh vien

    def number_of_student(self):
        return self.list_student.__len__()

    # Ham tao ID tu dong tang dan
    def generate_id(self):
        maxId = 1
        if self.number_of_student() > 0:
            maxId = self.number_of_student()[0]._id
            for x in self.list_student:
                if maxId < x._id:
                    maxId = x._id
            maxId = maxId + 1
        return maxId

    # Ham tinh diem trung binh cho sinh vien
    def calculate_gpa(self, stu: StudentController):
        gpa = (stu._math + stu._physic + stu._chemistry) / 3
        # sd ceil de lam tron so thap phan
        stu._gpa = math.ceil(gpa * 100) / 100

    # Ham xep loai hoc luc cho sinh vien
    def status_student(self, stu: StudentController):
        if stu._gpa >= 8:
            stu._status = "Gioi"
        elif stu._gpa >= 6.5:
              stu._status = "Kha"
        elif stu._gpa >= 5:
            stu._status = "Trung Binh"
        else:
            stu._status = "Yeu"

    # Ham nhap thong tin sinh vien
    def insert_student_information(self):
        id = self.generate_id()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        age = int(input("Nhap tuoi sinh vien: "))
        math = float(input("Nhap diem toan: "))
        physic = float(input("Nhap diem Ly: "))
        chemistry = float(input("Nhap diem Hoa: "))
        student = StudentController(id, name, sex, age, math, physic, chemistry)
        self.calculate_gpa(student)
        self.status_student(student)
        self.list_student.append(student)

    # Ham tim kiem thong tin sinh vien theo ID
    def find_by_id(self, ID):
        searchResult = None
        if self.number_of_student() > 0:
            for stu in self.list_student:
                if stu._id == ID:
                    searchResult = stu
        return searchResult

    # Ham cap nhap thong tin sinh vien
    def update_student_infor(self, ID):
        # Tim kiem sinh vien trong list da cho
        stu: StudentManagementController = self.find_by_id(ID)
        if stu is not None:
            # nhap lai thong tin
            name = input("Nhap ten sinh vien: ")
            gender = input("Nhap gioi tinh sinh vien: ")
            age = int(input("Nhap tuoi sinh vien: "))
            math = float(input("Nhap diem toan: "))
            physic = float(input("Nhap diem Ly: "))
            chemistry = float(input("Nhap diem Hoa: "))
            # cap nhap lai thong tin sinh vien
            stu._name = name
            stu._gender = gender
            stu._age = age
            stu._math = math
            stu._physic = physic
            stu._chemistry = chemistry
            self.calculate_gpa(stu)
            self.status_student(stu)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    # Ham sap xep danh sach sinh vien theo ID o dang tang dan
    def sort_by_id(self):
        self.list_student.sort(key=lambda x: x._id, reverse=False)

    # Ham sap xep danh sach sinh vien theo ten o dang tang dan
    def sort_by_name(self):
        self.list_student.sort(key=lambda x: x._name, reverse=False)

    # Ham sap xep danh sach sinh vien theo diem trung binh o dang tang dan
    def sort_by_gpa(self):
        self.list_student.sort(key=lambda x: x._diemTB, reverse=False)

    #  Ham tim kiem sinh vien theo ten va tra ve 1 danh sach sinh vien
    def find_by_name(self, keyword):
        list_stu = []
        if self.number_of_student() > 0:
            for stu in self.list_student:
                if keyword.upper() in stu._name.upper():
                    list_stu.append(stu)
        return list_stu

    # Ham xoa thong tin sinh vien theo ID
    def delete_student_infor(self, ID):
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        stu = self.find_by_id(ID)
        if stu is not None:
            self.list_student.remove(stu)
            isDeleted = True
        return isDeleted

    # Ham hien thi thong tin sinh vien
    def print_list_student(self, list_stu):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Gender", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        # hien thi danh sach sinh vien
        if list_stu.__len__() > 0:
            for stu in list_stu:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(stu._id, stu._name, stu._gender, stu._age, stu._math, stu._physic,
                              stu._chemistry, stu._gpa, stu._status))
        print("\n")

    # Ham tra ve danh sach sinh vien o hien tai
    def get_list_student(self):
        return self.list_student
