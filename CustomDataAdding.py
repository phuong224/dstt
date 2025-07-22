import sys 
sys.path.append("./backend/")
from DataManager import DataManager

def main():
    data_mag = DataManager()

    data_mag.addCustomData(
        "Nguyễn Nam Phương",
        "123456",
        "phuong.nguyen@gmail.com"
    )

    data_mag.addCustomData(
        "Lưu Chí Vỹ",
        "123456",
        "vy.luu@gmail.com"
    )

    data_mag.addCustomData(
        "Trần Khả Vy",
        "123456",
        "vy.tran@gmail.com"
    )

    data_mag.addCustomData(
        "Võ Trúc Mai",
        "123456",
        "mai.vo@gmail.com"
    )

    data_mag.addCustomData(
        "Trần Ngọc Bình",
        "123456",
        "binh.tran@gmail.com"
    )

    data_mag.addCustomData(
        "Trương Ngọc Phát",
        "123456",
        "phat.truong@gmail.com"
    )

    data_mag.addCustomData(
        "Nguyễn Thanh Tâm",
        "123456",
        "tam.nguyen@gmail.com"
    )

    data_mag.addCustomData(
        "Nguyễn Quang Minh",
        "123456",
        "quang.nguyen@gmail.com"
    )

    data_mag.addCustomData(
        "Trương Triều Trường",
        "123456",
        "truong.truong@gmail.com"
    )

    data_mag.addCustomData(
        "Đậu Ngọc Vương",
        "123456",
        "vuong.dau@gmail.com"
    )

    data_mag.addCustomData(
        "Nguyễn Ngọc Thiện",
        "123456",
        "thien.nguyen@gmail.com"
    )

    data_mag.addCustomData(
        "Vũ Đăng Khôi",
        "123456",
        "khoi.vu@gmail.com"
    )

    data_mag.addCustomData(
        "Nguyễn Phương Thảo",
        "123456",
        "thao.nguyen@gmail.com"
    )

    data_mag.addCustomData(
        "Phạm Thị Hồng Nhung",
        "123456",
        "nhung.pham@gmail.com"
    )

    data_mag.addCustomData(
        "Lê Minh Tuấn",
        "123456",
        "tuan.le@gmail.com"
    )

    data_mag.addCustomData(
        "Hoàng Gia Bảo",
        "123456",
        "bao.hoang@gmail.com"
    )

    data_mag.addCustomData(
        "Đặng Thị Kim Ngân",
        "123456",
        "ngan.dang@gmail.com"
    )


if __name__ == "__main__":
    main()