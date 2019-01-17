def compare(a, b):
    a = str(a)
    b = str(b)
    i = 0
    while i < len(a) and i < len(b):
        if int(a[i]) > int(b[i]):
            print("T")
            return True
        elif int(a[i]) < int(b[i]):
            print("F")
            return False
        else:
            print(i)
            i += 1
    if i==len(a) and i==len(b):
        return True
    else:
        if len(a) > i:
            return True
        if len(b) > i:
            return False    