### DEFINING FUNCTIONS >>> def functionName(parameter):
def bonjour():
    name = input("C'est quoi ton nom? ")
    print(f"Bonjour, {name} :)")

bonjour()

def bye(name="default"):
    print(f"Bye, {name}!")

bye()

name=input("Remind me what your name is again? ")
bye(name)