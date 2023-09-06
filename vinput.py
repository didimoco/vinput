def vinput(typeout:type,textinput:str,verify:list = False,uppercase:bool = False,stripinput:bool = False,faillmss:str = ''):
    
    while True:

        try:

            x = typeout(input(textinput))

            if uppercase: x = x.upper()

            if stripinput: x = x.strip()

            if verify:

                if x not in verify:
                    if faillmss != '' :print(faillmss)
                    continue


        except ValueError:
            if mss_error != '':print(faillmss)
            continue

        return x



if __name__ == "__main__":

# exemple of getting an int variable defined
    
    
    #faillmss is optional for the loop

    number = vinput(typeout = int , textinput = 'enter an int number between 0 and 10: ',verify = range(0,11),faillmss = 'enter a valid number !')

