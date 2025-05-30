password=123456789
so_du=10000000 
so_lan_nhap=0
max_lan_nhap=3
thanh_cong=False

while so_lan_nhap<max_lan_nhap:
    nhap_pass=int(input("nhập mã Pin: "))
    if nhap_pass==password:
        thanh_cong=True
        print("đăng nhập thành công !")
        break
    else :
        so_lan_nhap +=1
        so_lan_da_nhap=max_lan_nhap-so_lan_nhap
        print("nhập sai mật khẩu!")
        print("bạn còn",so_lan_da_nhap,"lần nhập")
if thanh_cong==False:
    print("bạn đã nhập mk quá 3 lần thẻ của bạn đã bị khóa")
else:
    while True:
        print("--- MENU ATM ---")
        print("1.Kiểm tra số dư")
        print("2.Rút tiền")
        print("3.Nạp tiền")
        print("4.Thoát")

        select=int(input("Chọn một chức năng (1-4): "))

        if select == 1:
            print("Số dư hiện tại của bạn là:",so_du,"vnđ")
            print("cảm ơn bạn đã sử dụng dịch vụ")
        elif select == 2:
            so_tien = float(input("Nhập số tiền muốn rút: "))
            if so_tien < 0:
                print("Số tiền không hợp lệ.")
            elif so_tien > so_du:
                print("Số dư không đủ.")
            else:
                so_du -= so_tien
                print("Bạn đã rút", so_tien ,"vnđ. Số dư còn lại:",so_du,"vnđ")
            print("cảm ơn bạn đã sử dụng dịch vụ")
        elif select == 3:
            so_tien = float(input("Nhập số tiền muốn nạp: "))
            if so_tien < 0:
                print("Số tiền không hợp lệ.")
            else:
                so_du += so_tien
                print("Bạn đã nạp",so_tien,"vnđ. Số dư mới:",so_du,"vnđ")
            print("cảm ơn bạn đã sử dụng dịch vụ")
        elif select == 4:
            print("Cảm ơn bạn đã sử dụng hệ thống atm của chúng tôi")
            break
        else:
            print("Vui lòng chọn số từ 1 đến 4.")