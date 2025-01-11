def main():

    name=input("What is your name? ")
    print(house(name))

def house(name):
    # if name == "Harry" or name == "Hermione" or name == "Ron":
    #     return "Gryffindor!"
    # elif name == "Draco":
    #     return "Slytherin!"
    # else:
    #     return "Who?"
    
# match, equivalent to switch in other languages 
    match name:
        case "Harry" | "Hermione" | "Ron":
            return "Gryffindor!"
        case "Draco":
            return "Slytherin!"
    # default case
        case _:
            return "Who?"
    

main()