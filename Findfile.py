# -*- coding: utf-8 -*-
import os
os.chdir('C:/Users/pdxgs/desktop/python')
def findfile():
    pathname=input('please enter the path you want to search')
    filename=input('please enter the filename you want to search')
    global  findresult,pathnamef
    findresult=[]
    if pathname.find('/')==-1 and pathname.find('\\')==-1:
        pathh='.'
    else:
        pathh=pathname
    pathnamef = pathh
    pathname_len=len(pathh)
    def find(filename,pathh):
        f=[x for x in os.listdir(pathh) if os.path.isfile(os.path.join(pathh,x))]
        f_subdir=[x for x in os.listdir(pathh) if os.path.isdir(os.path.join(pathh,x))]
        f_file=list(map(onlyname,f))
        for x in f_file:
            if x[0].find(filename) != -1:
                findresult.append(pathh[len(pathnamef):]+x[0]+x[1])

        for s in f_subdir:
            find(filename,os.path.join(pathh,s))


    find(filename,pathh)
    return findresult

def onlyname(str):
    return [os.path.splitext((os.path.split(str)[1]))[0],os.path.splitext((os.path.split(str)[1]))[1]]
    pass


c=findfile()


for x in c:
    print(x)
print(c)
len(c)

find('tes','.')

















f=[x for x in os.listdir(pathh) if os.path.isfile(x)]
f_subdir=[x for x in os.listdir(pathh) if os.path.isdir(x)]
f_file=list(map(onlyname,f))
f_file
filename='test'
for x in f_file:
    if x.find(filename) != -1:
        findresult.append(x)
    elif len(f_subdir)==0 and len(findresult)==0:
        print('Not Found!')
    elif len(f_subdir)==0 and len(findresult)!=0:
        print(findresult)
        pass
print(findresult)
