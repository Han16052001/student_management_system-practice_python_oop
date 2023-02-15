"""
Đề bài: Viết chương trình quản lý sinh viên trong Python.
Mỗi đối tượng sinh viên có các thuộc tính sau: id, tên, giới tính, tuổi, điểm toán, điểm lý, điểm hóa, điểm trung bình
và học lực.

- Id là mã sinh viên tự động tăng.

- Điểm trung bình là giá trị trung bình của 3 môn toán, lý và hóa.

- Học lực được tính như sau:
+ Giỏi: nếu điểm trung bình lớn hơn hoặc bằng 8.
+ Khá: nếu điểm trung bình nhỏ hơn 8 và lớn hơn hoặc bằng 6.5.
+ Trung Bình: nếu điểm trung bình nhỏ hơn 6.5 và lớn hơn hoặc bằng 5.
+ Yếu: nếu điểm trung bình nhỏ hơn 5.

Yêu cầu: tạo ra một menu với các chức năng sau:
1. Thêm sinh viên.
2. Cập nhật thông tin sinh viên bởi ID.
3. Xóa sinh viên bởi ID.
4. Tìm kiếm sinh viên theo tên.
5. Sắp xếp sinh viên theo điểm trung bình (GPA).
6. Sắp xếp sinh viên theo tên.
6. Sắp xếp sinh viên theo ID.
8. Hiển thị danh sách sinh viên.

optional: Khong duoc cho phep nguoi dung nhap sai gia tri da quy dinh trong menu qua 5 lan
"""