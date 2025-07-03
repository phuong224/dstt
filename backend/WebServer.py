from DataAccess import Factory
from AccountManager import AccountManager
from DataManager import DataManager
from flask import Flask, jsonify, session, request
from flask_cors import CORS
import os 

class AccountError(Exception):
    def __init__ (self, s):
        self.message = "account error: " + s


class WebServer:
    def __init__ (self):
        self.data_mag = DataManager()
        self.acc_mag = AccountManager()
        

    def run(self, host='127.0.0.1', port=5000):
        app = Flask(__name__)
        CORS(app)
        self.set_routes(app)
        app.secret_key = 'nhom_5'
        app.run(host=host, port=port, debug=True)
    
    def console_test(self):
        cmd = 10
        while (cmd != 0):
            os.system('cls')
            print ("Bảng mệnh lệnh: ")
            print ("0. Thoát.")
            print ("1. đăng nhập.")
            print ("2. đăng xuất.")
            print ("3. Danh sách sản phẩm.")
            print ("4. Danh sách sản phẩm đã mua.")
            print ("5. Danh sách sản phẩm đề xuất.")
            print ("6. Mua hàng.")
            print ("7. Hủy đơn hàng.")

            cmd = int(input("vui lòng nhập mã lệnh: "))

            try:
                match cmd:
                    case 0: 
                        break
                    case 1:
                        self.login(
                            email = input("Vui lòng nhập email: "),
                            pw = input("Vui lòng nhập mật khẩu: ")
                        )
                    case 2:
                        self.logout()
                    case 3:
                        print ("Danh sách vật phẩm: ")
                        for prod in self.getproducts():
                            print (prod)
                    case 4:
                        print ("Danh sách vật phẩm đã mua: ")
                        for prod in self.getPreviousProduct():
                            print (prod)
                    case 5:
                        print ("Danh sách vật phẩm đề xuất: ")
                        for prod in self.getProposeProduct(5):
                            print (prod)
                    case 6: 
                        self.buy(
                            id = input("Nhập mã hàng: "),
                            quantity = int(input("Nhập số lượng: "))
                        )
                    case 7: 
                        self.drop (
                            id = input ("Nhập mã đơn bạn muốn hủy: ")
                        )
            except Exception as err:
                print (f"Error: {err}")
            input("enter....")
        
    def getproducts(self):
        return self.data_mag.getProductData()
    
    def login(self, email, pw):
        for cus in self.data_mag.getCustomData():
            if cus['email'] == email and cus['pw'] == pw:
                self.acc_mag.setAccount(cus['id'])
        
        if self.acc_mag.id is None:
            raise AccountError("Wrong email or password.")

    def logout(self):
        if self.acc_mag.id is None:
            raise AccountError("You are not logged in.")
        else:
            self.acc_mag.setDefault()
            
        
    def drop(self, id):
        if self.acc_mag.id is None:
            raise AccountError("You are not logged in.")
        elif self.data_mag.getPurById(id) is None:
            raise ValueError("Cannot find purchase!")
        else:
            self.data_mag.removePurchaseData(id)
            
    
    def buy(self, id, quantity):
        if self.acc_mag.id is None:
            raise AccountError("You are not logged in.")
        elif self.data_mag.getProdById(id) is None:
            raise ValueError("Cannot find product!")
        elif quantity < 0 or quantity > 50:
            raise ValueError("abnormal quantity.")
        else:
            self.data_mag.addPurchaseData(self.acc_mag.id, id, quantity)
                
    
    def getPreviousProduct(self):
        if self.acc_mag.id is None:
            raise AccountError('You are not logged in.')

        return self.acc_mag.getPreviousProduct(
            self.data_mag.getProductData(), 
            self.data_mag.getPurchaseData()
        )
    
    def getProposeProduct(self, k):
        if self.acc_mag.id is None:
            raise AccountError('You are not logged in')
        
        return self.acc_mag.getProposeProduct(
            self.data_mag.getCustomData(),
            self.data_mag.getProductData(),
            self.data_mag.getPurchaseData(),
            k
        )

    def getUserInfo(self):
        user = self.data_mag.getCusById(self.acc_mag.id)
        if user is None:
            raise AccountError("Cannot find user")
        else:
            return user


    def set_routes(self, app):
        @app.route("/danh-sach-san-pham")
        def danh_sach_san_pham():
            return self.getproducts()
        
        @app.route("/danh-sach-san-pham-da-mua")
        def danh_sach_san_pham_da_mua():
            return self.getPreviousProduct()
        
        @app.route("/danh-sach-san-pham-goi-y")
        def danh_sach_san_pham_goi_y():
            return self.getProposeProduct(5)
        
        from flask import request, session, jsonify

        @app.route("/dang-nhap", methods=["POST"])
        def dang_nhap():
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")

            try:
                self.login(email, password)
                user = next((c for c in self.data_mag.getCustomData() if c["id"] == self.acc_mag.id), None)
                return jsonify({"success": True, "user": user})
            except AccountError as err:
                return jsonify({"success": False, "message": str(err)}), 401
            
        @app.route("/dang-xuat", methods=["POST"])
        def dang_xuat():
            session.clear()
            try:
                self.logout()
                return jsonify({"status": True, "message": "Đăng xuất thành công"})
            except AccountError as err:
                return jsonify({"status": False, "message": str(err)})
            
        @app.route("/nguoi-dung", methods=["GET"])
        def thong_tin_nguoi_dung():
            try:
                user = self.getUserInfo()
                return jsonify({"status": True, "user": user})
            except AccountError as err:
                return jsonify({"status": False, "message": str(err)})

