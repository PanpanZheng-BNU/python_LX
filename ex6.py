type_of_people = 10
# 1
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
# 2 & 3
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# 4
print(f"I said: {x}")
# 5
print(f"I also said: '{y}'")

hilarious = True
joke_evaluation = "Is't that joke '{}' so funny?! {}"

# 6
print(joke_evaluation.format(hilarious,y))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
