#plaindrome number
num =101
rev = 0
temp=num

while num!=0:
    rem = num%10
    rev =rev*10+(rem)
    num//=10
if(temp==rev):
        print("plaindrome no")
else:
        print("not plaindrome ")

#plaindrome string 

str="hih"
if (str==str[::-1]):
       print("the string is plaindrome")
else:
       print("not plaindrome")       
