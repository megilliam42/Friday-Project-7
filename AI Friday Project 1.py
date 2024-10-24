def mad_libs():
    print("Welcome to the Mad Libs Game!")
    print("Please provide the following words:")

    large_object = input("A large object: ")
    large_objects_plural = input("Large objects (plural): ")
    adjective = input("An adjective: ")
    body_part = input("A body part: ")
    restaurant = input("A restaurant: ")
    food_1 = input("A food: ")
    food_2 = input("Another food: ")

    story = f"""I’ve had a very {adjective} day.
This morning, I dropped a box of {large_objects_plural} on my {body_part}.
Then, at lunch, I went to {restaurant} for their delicious {food_1},
But the waiter brought me {food_2}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."""

    print("\nHere’s your story:")
    print(story)

if __name__ == "__main__":
    mad_libs()