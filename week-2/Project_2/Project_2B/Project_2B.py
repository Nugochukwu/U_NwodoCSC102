a = int(input("What is A"))
b = int(input("What is B"))
c = int(input("What is c"))
qroot1 = ((0 - b) + ((b ** 2) - (4 * a * c)) ** (1/2))/(2 * a)
qroot2 = ((0 - b) - ((b ** 2) - (4 * a * c)) ** (1/2))/(2 * a)

print(f"1st root ={qroot1}")
print(f"2nd root ={qroot2}")
