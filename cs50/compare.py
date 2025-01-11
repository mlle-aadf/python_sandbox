# convention is to def main(), then call main() at the end
def main():
    x=int(input("What's x? "))
    y=int(input("What's y? "))
# if, elif, else
    def compare1():
        if x<y:
            print("x is less than y")
        elif x>y:
            print("x is greater than y")
        else:
            print("x is equal to y")
    compare1()    

    def compare2():
# or    
#       if x<y or x>y:
# != 
        # if x!=y:
# ==
        if x==y:
            print("x it not equal to y")
        else:
            print("x is equal to y")
    compare2()    

main()