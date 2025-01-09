### int(), float(), round()

# x=int(input("What's x? "))
# y=int(input("What's y? "))

# x=float(input("What's x? "))
# y=float(input("What's y? "))

x=float(input("What's x? "))
y=float(input("What's y? "))
z=round(x+y)
# print(z)

# *** round(number[, ndigits]) , default: nearest int
# https://docs.python.org/3/library/functions.html#round

# z=round(x+y, 4)
print(z)

# *** format print(z) output, f-strings
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
variable = z
print(f"Variable: {variable}")
print(f"{z:,}")
print(f"{z:.3f}") # "print 3 digits of float"