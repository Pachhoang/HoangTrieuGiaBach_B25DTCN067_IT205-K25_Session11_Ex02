# Phân tích:
# - Dictionary employee gồm các key:
#   employee_id, full_name, department, status
# - Dictionary truy cập dữ liệu bằng key, không dùng index như list
# - employee[0] gây lỗi KeyError vì key 0 không tồn tại
# - Muốn lấy mã nhân viên phải dùng employee["employee_id"]
# - employee["name"] gây lỗi vì dictionary không có key "name"
# - Key đúng để lấy họ tên là "full_name"
# - employee["employee_status"] = "official" tạo thêm key mới,
#   không cập nhật giá trị của key "status"
# - Muốn cập nhật trạng thái phải dùng key "status"
# - Dictionary không có phương thức append()
# - Muốn thêm lương cơ bản chỉ cần gán:
#   employee["base_salary"] = 15000000
# - del employee["team"] gây lỗi vì key "team" không tồn tại
# - Muốn xóa thông tin phòng ban phải dùng key "department"

employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]

employee["status"] = "official"

employee["base_salary"] = 15000000

del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)