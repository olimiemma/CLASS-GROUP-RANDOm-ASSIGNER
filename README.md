# Random Group Assignment Scripts

This repository contains two Python scripts for randomly assigning students into groups. These scripts are useful for educators, event organizers, or anyone who needs to quickly and fairly divide a set of individuals into groups.

## Scripts

1. `group_assignment_names.py`: Assigns students to groups based on their names.
2. `group_assignment_numbers.py`: Assigns students to groups using numbers instead of names.

Both scripts create groups of 3 by default, but this can be easily modified in the code.

## Features

- Randomly assign students/numbers to groups
- Handle cases where the total number of students isn't evenly divisible by the group size
- Simple command-line interface for input
- Clear output displaying the assigned groups

## Usage

### group_assignment_names.py

This script allows you to input student names and then randomly assigns them to groups.

1. Run the script: `python group_assignment_names.py`
2. Enter student names, one per line
3. Press Enter twice when you're done entering names
4. The script will output the randomly assigned groups

Example output:
```
Group 1: Alice, Bob, Charlie
Group 2: David, Eve, Frank
Group 3: George, Hannah, Ivy, Jack
```

### group_assignment_numbers.py

This script asks for the total number of students and then assigns numbers to groups.

1. Run the script: `python group_assignment_numbers.py`
2. Enter the total number of students when prompted
3. The script will output the randomly assigned groups

Example output:
```
Group 1: 7, 2, 11
Group 2: 9, 4, 1
Group 3: 8, 3, 6
Group 4: 13, 5, 10, 12
```

## Customization

You can easily modify the group size by changing the `group_size` parameter in the `assign_groups` function call in either script.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements or bug fixes. You can also open issues if you find any problems or have suggestions for improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
