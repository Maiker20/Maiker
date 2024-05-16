import math

s=input("escribes un número:\n")
s1 =float(s)
s2=math. radians(s1)


x =math. radians(9)
y =math.radians(10)
z =math. radians (3)

print (math.sin(s2))
f=open("resultado.txt", "w")
f.write(f"el seno es: {x}")
f.close()

print(f"el seno es: {math. sin(x)}")
print(f" el coseno es :  {math.cos(y)}")
print(f"el tangente es : {math.tan(z)}")



a=int(input("número 2: "))
b=int(input("número 3: "))
s=a+b
r=a-b
d=a/b
m=a*b
print(f"la suma es :  ,{s} ")
print("la resta es :   ,{r}")
print("la división es:,{d}")
print("la multiplicación es: ,{m}")   






    