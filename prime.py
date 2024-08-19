x=int(input("enter the number"))
flag=False
if x==1:
   print(x,"number is not prime")
elif x>2:
   for i in range(2,x) :
      if x%i==0:
         flag=True
         break
if flag:
   print("not a prime")
else:
   print("prime")         
      
            