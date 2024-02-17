nterm = int(input("enter a number"))
n1 =0
n2=1
c=0
if nterm<=0:
    print("please positive no")
elif nterm==1:
    print(nterm)
    print(n1)
else:
    print("the fibonaci sequence ")
    while(c<nterm):
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        c+=1

# # Program to display the Fibonacci sequence up to n-th term
# nterms = int(input("How many terms? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1