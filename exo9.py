def city_population():
    cities = []
    
    # Ask for city names until 'stop' is entered
    while True:
        city_name = input("Enter the name of a city (or type 'stop' to end): ")
        
        if city_name.lower() == 'stop':
            break
        
        # Calculate the population based on the length of the city's name
        population = len(city_name)
        
        # Add the city and its population to the list
        cities.append((city_name, population))
    
    # Sort the cities by population (from largest to smallest) 
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            if cities[i][1] < cities[j][1]:
                cities[i], cities[j] = cities[j], cities[i]  # Swap the cities if out of order
    
    # Print the cities and their populations in order
    print("\nCities and their populations (from largest to smallest):")
    for city, population in cities:
        print(f"{city}: {population} people")

# Run the function
city_population()
