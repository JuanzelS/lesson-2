# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

# Function to calculate the volume of a rectangular prism
def calculate_volume():
    print("Enter the height, width, and length to calculate the volume of a rectangular prism.")
    
    # Get the unit of measurement
    units = input("Input units (e.g., inches, cm, meters): ")

    # Get the height, width, and length as float inputs
    height = float(input("Height: "))
    width = float(input("Width: "))
    length = float(input("Length: "))
    
    # Calculate the volume
    volume = height * width * length

    # Print the formatted result
    print(f"A rectangular prism with a height of {height} {units}, width of {width} {units}, and length of {length} {units} has a volume of {volume} cubic {units}.")
    
# Call the function
calculate_volume()



