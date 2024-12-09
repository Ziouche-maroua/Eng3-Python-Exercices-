number_of_people = int(input("How many people need a ride? "))
number_of_people_per_taxi = int(input("How many people fit in one taxi? "))


number_of_taxi = number_of_people // number_of_people_per_taxi


if number_of_people % number_of_people_per_taxi != 0:
    number_of_taxi += 1

print("Number of taxis needed:", number_of_taxi)
