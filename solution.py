def rgb_to_grayscale(color):
    
    vector=[]
    
    # Hex to Decimal
    
    for element in color:
        match element:
            case 'A':
                vector.append(10)
            case 'B':
                vector.append(11)
            case 'C':
                vector.append(12)
            case 'D':
                vector.append(13)
            case 'E':
                vector.append(14)
            case 'F':
                vector.append(15)
            case _:
                vector.append(element)

    R= 16*int(vector[1])+int(vector[2])
    G= 16*int(vector[3])+int(vector[4])
    B= 16*int(vector[5])+int(vector[6])
    
    # calculating Y decimal 0 to 255
    
    Y = int(round(0.299 * R + 0.587 * G + 0.114 * B))
    
    # going back to hex, removing the 0x at the begining
    
    Y=hex(Y).replace('0x','')

    if len(Y) < 2:
        Y='#'+3*('0'+Y)
    else:
        Y='#'+3*Y
    
    return Y
