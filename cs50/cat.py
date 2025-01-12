def main():
    number=get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("What's n?  "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


# prompting user for a positive integer n
# def meow():
#     while True:
#         n=int(input("What's n?  "))
#         if n>0:
#             break
#     for _ in range(n):
#         print("meow")

# using multiplication
# def meow():
    # print("meow \n" *3, end="")
         

# for loop
# def meow():
    # for i in [0,1,2]:
    # for _ in range(3):
    #     print("meow")


# while loop
# def meow():
#     i=3
#     while i>0:
#         print("meow")
#         i-=1



if __name__ == "__main__":
    main()