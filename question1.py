a = 1.0
b = "1"
c ="1.1"
print(a + float(b))
print(float(b) + float(c))
print(a + int(1.1))
print(a + int(float(c)))
print(int(a) + int(float(c)))
print(2.0*int(b))