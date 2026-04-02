def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    while True:
        new = ""
        i = 0
        changed = False
        
        

        while i < len(s):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                i += 2
                changed = True
            else:
                new += s[i]
                i += 1



        if not changed:
            return s

        s = new
        
        