import random

def assign_groups(names, group_size=3):
    # Shuffle the list of names
    random.shuffle(names)
    
    # Calculate the number of groups
    num_groups = len(names) // group_size
    
    # Create groups
    groups = []
    for i in range(num_groups):
        group = names[i*group_size:(i+1)*group_size]
        groups.append(group)
    
    # Add any remaining students to the last group
    if len(names) % group_size != 0:
        groups[-1].extend(names[num_groups*group_size:])
    
    return groups

# Get names from user input
print("Enter the names of your classmates (one per line). Press Enter twice when you're done:")
names = []
while True:
    name = input()
    if name == "":
        break
    names.append(name)

# Assign groups
assigned_groups = assign_groups(names)

# Print the groups
for i, group in enumerate(assigned_groups, 1):
    print(f"Group {i}: {', '.join(group)}")
