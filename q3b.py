def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    
    a = a[2:]
    b = b[2:]



    while len(a) < len(b):
        a = "0" + a
        
    while len(b) < len(a):
        b = "0" + b

    c = 0
    out = ""

    idx = len(a) - 1
    
    
    while idx >= 0:
        t = int(a[idx]) + int(b[idx]) + c

        if t == 0:
            out = "0" + out
            c = 0
        elif t == 1:
            out = "1" + out
            c = 0
        elif t == 2:
            out = "0" + out
            c = 1
        else:
            out = "1" + out
            c = 1

        idx -= 1




    if c == 1:
        out = "1" + out




    p = 0
    while p < len(out) - 1 and out[p] == "0":
        p += 1

    return "0b" + out[p:]