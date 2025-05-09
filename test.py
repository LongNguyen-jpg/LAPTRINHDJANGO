chon = 0
socauhoi = 7
while chon != socauhoi+1:
# Chương trình menu ghi các bài toán
    chon = int(input("Nhập lựa chọn của bạn (1-8): "))
 
    if  chon == 1:
        chuoi=input("nhập 1 chuỗi bất kì: ")
        chuoidao=""
        for i in range(len(chuoi)-1,-1,-1):
            chuoidao+=chuoi[i]
        print("Chuỗi đảo ngược là:", chuoidao)
 
    elif chon == 2:
        print("điều kiên a < b")
        soa=int(input("mời nhập số nguyên a: "))
        sob=int(input("mời nhập số nguyên b: "))
        if soa >= sob :
            print("mời bạ chọn lại")
        elif soa <= sob:
            tong=0
            for i in range(soa+1,sob):
                if i % 2 ==0:
                    tong +=i
            print("tổng của các số chẵn từ",soa,"đến",sob,"là",tong)
    
    elif chon==3:
        demsoam = 0

        while True:
            number = int(input("Nhập một số nguyên âm (nhập 0 để kết thúc): "))
            if number == 0:
                break
            elif number < 0:
                demsoam += 1

        print("Số lượng số âm là:", demsoam)
    
    elif chon==4:
        tong = 0
        sochia=0
        trungbinh=0

        while True:
            number = float(input("Nhập một số thực (nhập số âm để kết thúc): "))
            if number <0:
                break
            
            tong+=number
            sochia+=1
            trungbinh=tong/number

        print("trung bình các số bạn nhập là là:", trungbinh)

    elif chon==5:
        nam=int(input("nhập 1 năm bất kỳ: "))
        if nam%4==0:
            if nam % 100 !=0 or nam % 400== 0:
                print("năm đó là năm nhuận")
    elif chon==6:
        n = int(input("Nhập số nguyên n: "))
        tong = 0

        while n > 0:
            chu_so = n % 10  
            tong += chu_so      
            n = n // 10        

        print("Tổng các chữ số là:", tong)

    elif chon==7:
        chuoi=input("nhập 1 chuỗi bất kỳ : ")
        kytu=input("nhập ký tự cần đếm")
        dem=0
        for i in chuoi:
            if kytu==i:
                dem+=1
        print('Số lần xuất hiện của ký tự ',kytu, 'trong chuỗi là',dem)
    
    elif chon==8:
        soa=int(input("số kWh mà bạn tiêu thụ là :"))

    elif chon == socauhoi+1:
        print("\nCảm ơn bạn đã sử dụng chương trình!\n")
 
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn lại.\n")