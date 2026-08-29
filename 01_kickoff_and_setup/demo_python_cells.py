"""A small file for practicing Python in VS Code."""

# %% Imports

from datetime import date
import random



# %% A first edit
student_name = "YOUR NAME"  # TODO 1: replace this with your name
print(f"Hello, {student_name}!")
print("Today's date is:", date.today())


# %% Lists and loops

animals = ["dik-dik", "pangolin", "albatross"]
animals.append("YOUR SPECIES")  # TODO 2: replace with a species you study or like

for animal in animals:
    print("Animal:", animal)


# %% A tiny function

def describe_number(value):
    """Return a short description of a numeric value."""
    return f"The number is {value:.3f}"


n_numbers = 5  # TODO 3: change the number of values generated
random_numbers = [random.random() for _ in range(n_numbers)]

for number in random_numbers:
    print(describe_number(number))

print("Sum:", sum(random_numbers))

