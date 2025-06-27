import random
print("nhập số từ 1-10:")

        
choice = input("Nhập lựa chọn của bạn: ")

if choice == '1':
    my_list=[1,2,3,4,5,6,7,8,9,10]
    my_list.append(11)
    my_list.insert(0, 0)
    my_list.remove(5)
    print(my_list)
elif choice == '2':
    num=[]
    for i in range(5):
        so_nguyen=int(input("nhập 5 số nguyên bất kì :"))
        num.append(so_nguyen)
    tong=sum(num)
    giaitri_max=max(num)
    giatri_min=min(num)
    print("tông : ",tong)
    print("giá trị lớn nhất: ",giaitri_max)
    print("giá trị nhỏ nhất: ",giatri_min)
elif choice == '3':
    chuoi=input("nhập 1 chuỗi bất kỳ:")
    tach_chuoi=chuoi.split()
    sotu=len(tach_chuoi)
    sap_xep=sorted(tach_chuoi)
    print("Số từ:", sotu)
    print("sắp xếp:", sap_xep)
elif choice == '4':
    sochan=[]
    for i in range(21):
        if i%2 ==0 :
            sochan.append(i)
    tong=sum(sochan)
    sochia=len(sochan)
    trung_binh=tong/sochia
    print("list:",sochan)
    print("TB: " , trung_binh)
elif choice == '5':
    danh_sach=["minh","quang","linh","tú","hải"]
    name_can_kiem_tra=input("nhập tên học sinh cần kiểm tra:")
    if name_can_kiem_tra in danh_sach:
        print("có trong lớp ")
    else:
        print("ko có trong lớp")
elif choice == '6':
    list=[]
    for i in range(10):
        so=random.randint(10,100)
        list.append(so)
    print(list)
    list.sort()
    print(list)
elif choice == '7':
    so=[]
    sole=[]
    tong=0
    while True:
        nhap_so=int(input("nhập số: "))
        if nhap_so==0:
            break
        so.append(nhap_so)
    for chiaba in so :
        if chiaba%3==0:
            tong+=chiaba
    for so_le in so:
        if so_le%2==0:
            sole.append(so_le)
    print("tổng:",tong)
    print("danh sách số lẻ: ",sole)
elif choice == '8':
    list1=[]
    list2=[]
    while True:
        nhap_so_nguyen=int(input("nhập số lít 1 (1010 để thoát): "))
        if nhap_so_nguyen==1010:
            break
        list1.append(nhap_so_nguyen)
    while True:
        nhap_so_nguyen=int(input("nhập số lít 2 (1010 để thoát): "))
        if nhap_so_nguyen==1010:
            break
        list2.append(nhap_so_nguyen)
    list_gop = list1 + list2
    list_khong_trung = []
    for so in list_gop:
        if so not in list_khong_trung:
            list_khong_trung.append(so)
    list_khong_trung.sort()
    print("kết quả:", list_khong_trung)
#elif choice == '9':
elif choice == '10':
    ds_so = []

    while True:
        nhap = input("Nhập một số thực (hoặc 'x' để kết thúc): ")
        if nhap.lower() == 'x':
            break
        else:
            so = float(nhap)
            ds_so.append(so)

    if len(ds_so) > 0:
        tong = 0
        for so in ds_so:
            tong += so
        tbc = tong / len(ds_so)

        print("Tổng các số:", tong)
        print("Trung bình cộng:", tbc)

        print("Các số lớn hơn trung bình cộng:")
        for so in ds_so:
            if so > tbc:
                print(so)
