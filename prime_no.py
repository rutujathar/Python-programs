#prime number using while loop
n = int(input("enter the number:"))

# count = 0
# i =1

# while i<=n:
#    if(i%n==0):
#        count = count+1
#    i = i+1
# if(count ==2):
#     print(" yes ",n,"prime no")
# else:
     
#     print("no is not prime no")



# prime number using range()
if n==1:
    print(n,"is not prime no")
elif n>1:
    #check for factors
    for i in range(2,n):
        if(n%i==0):
            print(n, "is not a prime")
             
    else:
        
           print(n,"is prime no")
      


