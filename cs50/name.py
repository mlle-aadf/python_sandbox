## https://docs.python.org/3/library/sys.html#module-sys
import sys


## ARGV

if len(sys.argv) < 2:
    sys.exit("too few arguments")
# slice of argv[start, end]
for arg in sys.argv[1:]:
    print("hello, my name is", arg)
# negative index
for arg in sys.argv[1:-1]: 
    print("hello, my name is", arg)
for arg in sys.argv[-2:]: # negative index
    print("hello, my name is", arg)



# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("too many arguments")

# print("hello, my name is", sys.argv[1])


# try:
#     print("hello, my name is", sys.argv[1])

# except IndexError:
#     print("i don't know your name")

# print("hello, my name is", sys.argv[1])
# print("you are running", sys.argv[0])
