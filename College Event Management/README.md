# College Event Management

A Python application for managing college events and student registrations. As in our college every next day has an event, i have built this program to get help with storing event data as well as registered student data, It can be linked with a google form or deployed as a website to automate the registration process.

## Functional Modules
1. Event Management
2. Student Registration and Registered Student List
3. Reports and Algorithms

## Run
```bash
python main.py
```
## Working
## Pseudocode
```
START
Create empty event dictionary
WHILE application is running
    Display menu
    Read choice
    IF create event
        Store event in dictionary
    ELSE IF register
        Validate event
        Add student to participant list
    ELSE IF display
        Traverse events and display details
    ELSE IF view registered students
        Validate event
        Sort participant list
        Display students
    ELSE IF report
        Count registrations and find maximum
    ELSE IF exit
        BREAK
    ELSE
        CONTINUE
END WHILE
END
```

## Concepts Used
1. Variables and data types
2. Boolean values
3. if / elif / else
4. while / for / break / continue
5. Functions
6. Lists
7. Tuples and dictionaries
8. List methods
9. Counting and maximum
10. Sorting
11. Modular Python programs
