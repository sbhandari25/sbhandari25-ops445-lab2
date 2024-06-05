#!/usr/bin/env python3
import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit(0)

# Assign the arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the required output
print(f"Hi {name}, you are {age} years old.")



