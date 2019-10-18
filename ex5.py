my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_height_cm = my_height * 2.54 # covert inches to cm
my_weight_kg = my_weight * 453.59237 /1000 # covert lbs to kg

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_height_cm} cm tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"He's {round(my_weight_kg)} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exatly right
total = my_age + my_height + my_weight
print(f"if I add {my_age}, {my_height}, {my_weight} i get {total}.")
