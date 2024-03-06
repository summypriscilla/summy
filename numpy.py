import numpy or np
t= np arrange (0,1,0.01)
x=np sin(2* np pi*s*t)
#write data
f= open('sine.txt','w')
f.write(str(x))
f.close()
# read data
f=open(sine.txt,'r')
y=f.read()
print(y)
f.close()

