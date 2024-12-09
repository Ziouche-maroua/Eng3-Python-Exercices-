def compare_runners():
    
    name1 = input("Runner 1 - Name: ")
    time1 = float(input("Runner 1 - Time (in seconds): "))
    
    name2 = input("Runner 2 - Name: ")
    time2 = float(input("Runner 2 - Time (in seconds): "))
    
 
    if time1 < time2:
        print(f"The faster runner is {name1}")
    elif time2 < time1:
        print(f"The faster runner is {name2}")
    else:
        print(f"Both {name1} and {name2} have the same time.")

# Run the function
compare_runners()
