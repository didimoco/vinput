def input_diferenciado(typeout:type,textinput:str,verify:list = False,uppercase:bool = False,stripinput:bool = False,faillmss:str = ''):
    
    while True:

        try:

            x = input(textinput)

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
    

    print(input_diferenciado(str,'digite A ou B: ',['A','B'],True,True,'digite um dos valores validos'))

