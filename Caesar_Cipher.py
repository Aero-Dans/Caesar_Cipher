# Daniel Zhang 349523548

def encryptor(istring, svalue):
    '''
    encryptor functions uses the caeser cipher algorithm to encrypt a given string and the shift value

    argument:
    -- istring is the given string
    -- svalue is the shift value
    '''
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypted = ''



    for i in range(len(istring)):
        alphabet_index = 0
        while not istring[i] == alphabet[alphabet_index]:
            alphabet_index += 1

        encrypted += alphabet[alphabet_index + svalue]

    return encrypted


            

        






print(encryptor(input(), int(input())))

