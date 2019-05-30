import sys
import numpy as np

if __name__ == '__main__':
    string = sys.argv[1]

    vlist = []
    lvllist = []
    cnt = 0
    d = {}
    for s in string:
        if s.isdigit():
            vlist.append(int(s))
            lvllist.append(cnt)
            if cnt in d:
                d[cnt].append(int(s))
            else:
                d[cnt] = [int(s)]
            cnt = 0
        elif s == '-':
            cnt += 1
    
    print(vlist)
    print(lvllist)
        
    print(d)