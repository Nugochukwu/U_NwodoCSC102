a = int(input("What is A  "))
b = int(input("What is B  "))
c = int(input("What is C  "))
d = int(input("What is D  "))

Q = ((3*b)-(a**2))/9
R = ((9*a*b)-(27*c)-(2*(a**3)))/54
S = (R+((Q**3)+(R**2))**(1/2))**(1/3)
T = (R-((Q**3)+(R**2))**(1/3))**(1/3)
qroot1 = S + T - (1/3)*a
qroot2 = (-1 * (1/2))*(S+T)-((1/3)*a)+ (1/2)*(3**(1/3))*(S-T)
qroot3 = (-(1/2)*(S+T))-((1/3)*a)-((1/2)*(3**(1/2))*(S-T))
print(f"1st root ={qroot1}")
print(f"2nd root ={qroot2}")
print(f"3rd root ={qroot3}")
