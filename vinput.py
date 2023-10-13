def vinput(typeout:type , textinput:str , verify:list = False , uplow:int = 0, stripinput:bool = False , failmss:str = None,
           minlen:int = 0 , maxlen:int = None , minnum:float = None , maxnum:float = None):


    fail = lambda mss:print(mss) if mss != None else None

    while True:

        try:


            x = input(textinput)


            if len(x) < minlen:
                fail(failmss)
                continue

            if maxlen != -1 and maxlen != None and len(x) > maxlen:
                faill(failmss)
                continue

            match uplow:

                case 1: x = x.upper()

                case 2: x = x.lower()

            if stripinput: x = x.strip()
             
            x = typeout(x)

            if minnum != None and x < minnum:
                fail(failmss)
                continue

            if maxnum != None and x > maxnum:
                fail(failmss)
                continue
            
            if verify:

                if x not in verify:
                    fail(failmss)
                    continue 

        except ValueError:
            fail(failmss)
            continue

        return x

if __name__ == "__main__":

# exemple of getting an int variable defined

    number = vinput(typeout = int , textinput = 'enter an int number between 0 and 10: ',verify = range(0,11),failmss = 'enter a valid number !')

