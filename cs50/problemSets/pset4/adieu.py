### ADIEU, ADIEU
# https://cs50.harvard.edu/python/2022/psets/4/adieu/

# Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one [and], three names with two commas and one [and], and [n] names with [n-1] commas and one [and], as in the below:

#     Adieu, adieu, to Liesl
#     Adieu, adieu, to Liesl and Friedrich
#     Adieu, adieu, to Liesl, Friedrich, and Louisa
#     Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

def main():
    names = []
    
    while True:
        try:
            name = input("name: ").capitalize()
            
            if name == "..":
                raise Exception("EOF Error")
            else:
                names.append(name)
        
        except Exception:
            print(bidAdieu(names))
            break

def bidAdieu(names):
    
    adieu = ""
    
    if len(names) < 2:
        adieu = f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        adieu = f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        notlast, last =  ", ".join(names[0:len(names)-1]), names[-1]
        adieu = f"Adieu, adieu, to {notlast} and {last}"
    return adieu

if __name__ == "__main__":
    main()