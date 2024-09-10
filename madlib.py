def madlib():
    print("Let's create a fun story! Please provide the following words:")

    # Collect inputs from the user
    name = input("")
    adjective = input(" ")
    animal = input(" ")
    place = input(" ")
    verb = input(" ")
    food = input(" ")

    # Create the story using an f-string
    story = (f"One day, {name} was walking through the {place} when they saw a very {adjective} {animal}. "
             f"{name} decided to {verb} right away, but the {animal} surprised them by offering some {food} to share! "
             f"Together, they had a wonderful time enjoying the meal in the middle of the {place}.")

    # Display the story
    print("\nHere is your madlib story:")
    print(story)
