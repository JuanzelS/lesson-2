     # Get the unit of measurement
    units = input("Input units (e.g., inches, cm, meters): ")

    # Get the height, width, and length as float inputs
    height = float(input(" "))
    width = float(input(""))
    length = float(input(""))
    
    # Calculate the volume
    volume = height * width * length

    # Print the formatted result
    print(f"A rectangular prism with a height of {height} {units}, width of {width} {units}, and length of {length} {units} has a volume of {volume} cubic {units}.")
    
# Call the function
calculate_volume()



