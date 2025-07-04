﻿# 🛠️ Backend - Hệ Thống Đề Xuất Sản Phẩm

Đây là **phần backend** của hệ thống web đề xuất sản phẩm. Ứng dụng sử dụng Python (Flask) làm server, giao tiếp với frontend qua REST API, quản lý người dùng, phiên đăng nhập và dữ liệu sản phẩm trong MySQL.

---

## 🧱 Kiến trúc backend

Ảnh dưới đây minh họa kiến trúc backend, gồm các lớp:
- API Flask
- Module xử lý người dùng, dữ liệu sản phẩm
- Kết nối cơ sở dữ liệu MySQL

![Sơ đồ hệ thống backend](images/Diagram.png)

---

## 🗄️ Mô hình dữ liệu quan hệ

Sơ đồ CSDL mô tả mối quan hệ giữa các bảng:
- Người dùng
- Sản phẩm
- Đơn hàng
- Loại sản phẩm

![Mô hình dữ liệu](images/Relational_Schema.png)

---

## 🔌 API chính

| Phương thức | Đường dẫn                      | Mô tả                                 |
|------------|--------------------------------|---------------------------------------|
| POST       | `/dang-nhap`                  | Đăng nhập người dùng                  |
| POST       | `/dang-xuat`                  | Đăng xuất người dùng                  |
| GET        | `/nguoi-dung`                 | Lấy thông tin người dùng hiện tại     |
| GET        | `/danh-sach-san-pham`         | Trả về toàn bộ sản phẩm               |
| GET        | `/danh-sach-san-pham-goi-y`   | Trả về sản phẩm gợi ý cho người dùng  |
| GET        | `/danh-sach-san-pham-da-mua`           | Trả về danh sách sản phẩm đã mua của người dùng |

---

## ⚙️ Công nghệ sử dụng

- Python 3.x
- Flask
- Flask-CORS
- Flask-Session
- MySQL Connector

---

## 📁 Cấu trúc thư mục backend

```plaintext
dstt/
├── run.py                    # file test
├── backend/
    ├── AccountManager.py     # quản lý đăng nhập
    ├── DataAccess.py         # giao tiếp trực tiếp với database
    ├── DataManager.py        # lấy dữ liệu từ DataAccess
    ├── Utils.py              # các hàm tính toán SVD để gợi ý sản phẩm
    └── WebServer.py          # server chạy API và console test
```

---

## 📌 Lưu ý

- Backend sử dụng session để lưu thông tin đăng nhập → cần bật `credentials: 'include'` phía frontend.
- Các API đều trả về dữ liệu JSON.

---

## ✍️ Tác giả

- Nguyễn Nam Phương – [@phuong224](https://github.com/phuong224)
