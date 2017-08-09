a=int(input("num1"))
b=int(input("num2"))
c=int(input("num3"))
d=int(input("num4"))
e=int(input("num5"))
if(a>b and a>c):
    g=a
elif(b>c):
    g=b
else:
    g=c
if(g>d and g>e):
    print("the greatest number is",g)
elif(d>e):
    print("the greatest number is",d)
else:
    print("the greatest number is",e)
 
            
