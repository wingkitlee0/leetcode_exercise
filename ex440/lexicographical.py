def compare(a, b):
    """
    True if b>a
    """
    a = str(a)
    b = str(b)
    i = 0
    while i < len(a) and i < len(b):
        if int(a[i]) == int(b[i]):
            i += 1
        else:
            if int(a[i]) < int(b[i]):
                return True
            else:
                return False
            
    if i==len(a) or i==len(b):
        if i==len(a) and i==len(b):
            return True
        else:
            return len(b) > len(a)