from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Ctrl-C (^C).")
print("If you want that, hit Return.")

input("?")

print("Opening the file...")
target = open(filename,'a+')

print("Truncating the file. Goodbye!")
target.seek(0)
target.truncate()   # delete the bits after the ".seek(n)" location (n).
# so if open(,'w'), it will not work or isn't neccessary.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("And finally, we close it.")

# read the final txt
target = open(filename, 'r')
final_txt=target.read()
print(final_txt)
target.close()
