# Not just run this script!!!!!!!!!!!!!!!!!!!!
# But enter such as "python ex13.py first 2nd 3rd" (the last third variable coud be determined by self)in the CMD !!!!!!!
from sys import argv
# read the WYSS section for how to run this
script, first, second,third = argv


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("The sum number is:"int(first) + int(second) + int(third))
