def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    best = ""
    n = len(s)
    
    
    for i in range(n):
        for j in range(i+ 2, n + 1):
            sub = s[i:j]
            
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
                
                
    return best

