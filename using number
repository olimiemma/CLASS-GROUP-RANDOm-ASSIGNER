import random

def assign_groups(num_students, group_size=3):
    # Create a list of student numbers
    students = list(range(1, num_students + 1))
    
    # Shuffle the list of student numbers
    random.shuffle(students)
    
    # Calculate the number of groups
    num_groups = len(students) // group_size
    
    # Create groups
    groups = []
    for i in range(num_groups):
        group = students[i*group_size:(i+1)*group_size]
        groups.append(group)
    
    # Add any remaining students to the last group
    if len(students) % group_size != 0:
        groups[-1].extend(students[num_groups*group_size:])
    
    return groups

# Get number of students from user input
while True:
    try:
        num_students = int(input("Enter the total number of students: "))
        if num_students > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

# Assign groups
assigned_groups = assign_groups(num_students)

# Print the groups
for i, group in enumerate(assigned_groups, 1):
    print(f"Group {i}: {', '.join(map(str, group))}")
