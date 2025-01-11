def parity(n):
# ternary : [on_true] if [condition] else [on_false]
    return "odd" if n % 2 == 1 else "even"

def main():
    n = int(input("Enter a number: "))
    print(f"The parity of {n} is {parity(n)}")

main()
