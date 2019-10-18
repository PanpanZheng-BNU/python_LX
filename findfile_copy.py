# -*- coding: utf-8 -*-
import os
def findfile():
    str = input('Please enter the name you want to search:')
    path_name = input('Please enter the path you want to search:')
    if path_name.strip()=='':
        path_name='.'
    minus = len(path_name)

    def list_file(str,path):
        list_all = os.listdir(path)
        for name_f in list_all:
            path_c = os.path.join(path,name_f)
            if os.path.isfile(path_c) and str in os.path.splitext(name_f)[0]:
                print(path_c[minus:])
            elif os.path.isdir(path_c):
                list_file(str,path_c)

    list_file(str,path_name)

findfile()
