#大於 0、整數、找出4和3的公倍數、小於 n，請輸出所有可能的數字。
#輸入為一個整數 n
n = int(input())
for i in range(1,n):
    if n % 3 == 0 and n % 4 == 0:
        continue
    else:
        print(i)