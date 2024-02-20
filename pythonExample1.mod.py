#!/usr/bin/env python3


a=6

mm = [ list(range(i*a+1, (i+1)*a+1)) for i in range(a) ] 
def v(m):
    print("M:=", *m, sep='\n')
    if len(m) > 1: return m.pop(0)+[i.pop() for i in m[:-1]]+list(reversed(m.pop()))+list(reversed([i.pop(0) for i in m[1:]]))+v(m)
    else: return list(m)


print(v(mm))
