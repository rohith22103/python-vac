m1=int(input("enter c mark:"))
m2=int(input("enter py mark:"))
m3=int(input("enter java mark:"))
m4=int(input("enter c# mark:"))
m5=int(input("enter c++ mark:"))
sum=m1+m2+m3+m4+m5
avg=sum/5
if(m1>=45 and m2>=45 and m3>=45 and m4>=45 and m5>=45):
    r="pass"
if(avg>90):
    g='a+'
elif(avg>80):
    g='b'
elif(avg>70):
    g='c'
elif(avg>=45):
    g='d'
else:
    r="fail"
    g="no grade"
print("result:",r)
print("total:",sum)
print("average:",avg)
print("grade:",g)
