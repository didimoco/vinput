def vinput(typeout:type,textinput:str,verify:list = False,uppercase:bool = False,stripinput:bool = False,faillmss:str = '',minlen:int = 0,maxlen:int = -1,
           minnum:float = False , maxnum:float = False):
    
    while True:

        try:

            x = input(textinput)


            if len(x) < minlen:
                continue

            if maxlen != -1 and len(x) > maxlen:
                continue

            if uppercase: x = x.upper()

            if stripinput: x = x.strip()
             
            x = typeout(x)

            if minnum and x < minnum:
                continue

            if maxnum and x > maxnum:
                continue
            
            if verify:

                if x not in verify:
                    if faillmss != '' :print(faillmss)
                    continue 

        except ValueError:
            if faillmss != '':print(faillmss)
            continue

        return x

if __name__ == "__main__":

# exemple of getting an int variable defined
    
    
    #faillmss is optional for the loop

    number = vinput(typeout = int , textinput = 'enter an int number between 0 and 10: ',verify = range(0,11),faillmss = 'enter a valid number !')

