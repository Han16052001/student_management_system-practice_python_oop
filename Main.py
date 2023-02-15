from StudentManagement import StudentManagementController

student_management = StudentManagementController()

waiting_input = True

time_trial_left = 0


def print_menu():
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("=========================MENU==========================")
    print("==  1. Them sinh vien.                               ==")
    print("==  2. Cap nhat thong tin sinh vien boi ID.          ==")
    print("==  3. Xoa sinh vien boi ID.                         ==")
    print("==  4. Tim kiem sinh vien theo ten.                  ==")
    print("==  5. Sap xep sinh vien theo diem trung binh (GPA). ==")
    print("==  6. Sap xep sinh vien theo ten.                   ==")
    print("==  7. Sap xep sinh vien theo ID.                    ==")
    print("==  8. Hien thi danh sach sinh vien.                 ==")
    print("==  0. Thoat                                         ==")
    print("=======================================================")


while waiting_input and time_trial_left < 5:
    print_menu()
    option_number = int(input("Moi ban chon: "))

    match option_number:
        case 1:
            print("1.Them sinh vien")
            student_management.insert_student_information()
            print("Them sinh vien thanh cong !!!")
        case 2:
            if student_management.number_of_student() > 0:
                print("2.Cap nhap thong tin sinh vien")
                ID = int(input("Moi ban nhap ID sinh vien: "))
                student_management.update_student_infor(ID)
            else:
                print("Danh sach sinh vien trong")
        case 3:
            if student_management.number_of_student() > 0:
                print("3.Xoa thong tinh sinh vien")
                ID = int(input("Moi ban nhap ID sinh vien: "))
                if student_management.delete_student_infor():
                    print(f"Sinh vien co {ID} nay da duoc xoa thong tin")
                else:
                    print(f"Khong tim thay sinh vien co so {ID} nay")
            else:
                print("Danh sach sinh vien trong")
        case 4:
            if student_management.number_of_student() > 0:
                print("4.Tim kiem sinh vien theo ten")
                name = str(input("Nhap ten sinh vien can tim: "))
                result = student_management.find_by_name(name)
                student_management.print_list_student(result)
            else:
                print("Danh sach sinh vien trong")
        case 5:
            if student_management.number_of_student() > 0:
                print("5. Sap xep sinh vien theo diem trung binh (GPA)")
                student_management.sort_by_gpa()
                student_management.print_list_student(student_management.get_list_student())
            else:
                print("Danh sach sinh vien trong")
        case 6:
            if student_management.number_of_student() > 0:
                print("6. Sap xep sinh vien theo ten")
                student_management.sort_by_name()
                student_management.print_list_student(student_management.get_list_student())
            else:
                print("Danh sach sinh vien trong")
        case 7:
            if student_management.number_of_student() > 0:
                print("7. Sap xep sinh vien theo ID.")
                student_management.sort_by_id()
                student_management.print_list_student(student_management.get_list_student())
            else:
                print("Danh sach sinh vien trong")
        case 8:
            if student_management.number_of_student() > 0:
                print("8. Hien thi danh sach sinh vien.")
                student_management.print_list_student(student_management.get_list_student())
            else:
                print("Danh sach sinh vien trong")
        case 0:
            print("Ban da thoat khoi chuong trinh")
            waiting_input = False
        case _:
            time_trial_left += 1
            print("Chuc nang nay khong ton tai, moi ban chon lai !!!")
            print(f"Ban con {5-time_trial_left} thu")