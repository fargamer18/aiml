import random

def display(room):
    print(room)

# Initialize the room as a 4x4 grid filled with 1s (representing dirty spaces)
room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

print("All the rooom are dirty")
display(room)

# Randomly assign dirt (0 or 1) to each cell in the room
x = 0
y = 0
while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y += 1
    x += 1
    y = 0

print("Before cleaning the room I detect all of these random dirts")
display(room)

# Clean the room by removing dirt
x = 0
y = 0
z = 0  # Counter for cleaned spaces
while x < 4:
    while y < 4:
        if room[x][y] == 1:  # If the space is dirty
            print("Vaccum in this location now,", x, y)
            room[x][y] = 0  # Clean the space
            print("cleaned", x, y)
            z += 1  # Increment cleaned spaces counter
        y += 1
    x += 1
    y = 0

# Calculate performance (percentage of spaces cleaned)
pro = (100 - ((z/16)*100))

print("Room is clean now, Thanks for using")
display(room)
print('performance=', pro, '%')
