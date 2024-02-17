n = int(input('enter a number'))
reverse_num =0

while n!=0:
    rem = n%10
    reverse_num = reverse_num*10+rem
    n//=10 

print("reverse_num"+str(reverse_num))

# num = str(input('enter a string: '))
# # num =123456
# print(str(num)[::-1])