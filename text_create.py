import random

# Open the text file
file = open('english-words.txt', 'r')

# Read all lines from the file
lines = file.readlines()
list_item = []
mobile_item = []

# Choose random items from the lines
random_items = random.sample(lines, 44)  # Select 3 random items, you can change the number as needed

# Print the randomly selected items
for item in random_items:
    list_item.append(item.strip())

random_items_mobile = random.sample(lines, 35)  # Select 3 random items, you can change the number as needed

# Print the randomly selected items
for item in random_items:
    mobile_item.append(item.strip())

# Close the file
file.close()