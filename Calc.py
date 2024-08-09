print ("menu:")
print("jam=1")
print("menha=2")
print("zarb=3")
print("taghsim=4")
z=int(input("enter your num"))
x=float(input("enter num 1:"))
y=float(input("enter num 2:"))
if z==1 :
    print(x+y)
elif z==2 :
    if x>y :
      print(x-z)
    elif y>x :
      print(y-x)
elif z==3 :
    print (x*y)
elif z==4 :
if x>y :
    print(x/y)
elif y>x :
    print(y/x)
