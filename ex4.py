# the number of cars
cars = 100
# the number of seats in car`
space_in_a_car = 4
# the number of drivers
drivers = 30
# the number of passengers`
passengers = 90
# the number of car which not have driver
cars_not_driven = cars - drivers
# the number of car which have driver
cars_driven = drivers
# the maximize number of passengers which could be taken
carpool_capacity = cars_driven * space_in_a_car
# the average number of the passengers in the car
average_passengers_per_car = passengers / cars_driven
# if average_passengers_per_car is not a decimals, changing it to integer
if average_passengers_per_car%1 == 0:
    average_passengers_per_car = int(average_passengers_per_car)

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
