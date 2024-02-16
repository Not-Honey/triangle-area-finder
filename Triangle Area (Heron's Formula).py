import math
a = int(input("Please enter side a:"))
b = int(input("Please enter side b:"))
c = int(input("Please enter side c:"))
p = a + b + c
s = p/2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#Triangle Specifications
print("-------TRIANGLE SPECIFICATIONS-------")
print("Side a of triangle is:",a)
print()
print("Side b of triangle is:",b)
print()
print("Side c of triangle is:",c)
print()
print("Perimeter of triangle is:",p)
print()
print("Semi-Perimeter of triangle is:",s)
print()
print("Area of triangle is:",area)
print()
print("THANK YOU")
print("Made By Not_Honey, A.K.A Ghost")