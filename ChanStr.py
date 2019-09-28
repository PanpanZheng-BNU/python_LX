from functools import reduce
def change(x,y):
    return  10*x+y
    pass

def str2L(str):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'0'}
    return  digits[str]
    pass

def str2int(str):
    return reduce(change,map(str2L,str))
    pass


def str2float(str):
    dot=0
    L1=[]
    L2=[]
    for x in map(str2L,str):
        if x == '0':
            dot = 1
        if dot == 0:
            L1.append(float(x))
        else:
            L2.append(float(x))
    L2.pop(0)
    return float(reduce(lambda x,y:x+10**(-len(L2))*y,[float(reduce(lambda x,y:10*x+y,L1)),float(reduce(lambda x,y:10*x+y,L2))]))
    pass
