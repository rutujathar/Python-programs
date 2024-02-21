# n = int(input("enter the rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end ="")
#     print(" ")

n = int(input("enter the roy"))
num = 1
for i in range(0, n):
        num= 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")