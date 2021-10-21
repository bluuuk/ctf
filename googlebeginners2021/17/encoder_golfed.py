c=[];k=P=1
while k<10e3:
    if P%k>0:c+=[k&255]
    P*=k*k;k+=1
def encode(e):
    x=bytearray;a=x(range(65,91));z=x([0,0,0,26]);d=x(b'BEGN'+z+a.lower()+b'DATA'+len(e).to_bytes(4,"big")+e+b'END.'+z+a);return x(u^i for u,i in zip(d,c))
#END

"""

we did start with:

def encode(e):
    x=bytearray;a=x(range(65,91));z=x([0,0,0,26]);k=P=1;v=0
    d=x(b'BEGN'+z+a.lower()+b'DATA'+len(e).to_bytes(4,"big")+e+b'END.'+z+a)
    while v<len(d):
        if P%k>0:d[v]^=k&255;v+=1
        P*=k*k;k+=1
    return d


- To improve performance, we pre-calculate all the xor values. 
- bytearray reference save
- alphabet with range
- google prime gen => stackoverflow => https://codegolf.stackexchange.com/questions/5977/list-of-primes-under-a-million/5993
- one-lining with ;;;



"""