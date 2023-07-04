time = int(input("請輸入停車分鐘數："))

hr = time//60 #取整數 (小時) 
mi = time % 60 #取餘數 (分鐘)

if mi>=1:  #如果分鐘 大於或等於1分鐘加收20
  pay=(hr*40+20)
else: #其他沒有分鐘就算小時收費
  pay=(hr*40)


if pay>300:
  pay=300
print(f"要繳交{pay}元")