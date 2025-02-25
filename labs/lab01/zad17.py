x = 1
y = 2
z = 3

max = 2.2250738585072014e-308

if x > max:
    max = x
if y > max:
    max = y
if z > max:
    max = z

print(max)