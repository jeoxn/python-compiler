import sys

# Get the file path from command-line argument
filepath = sys.argv[1]

# Read the code from the file
with open(filepath, "r") as f:
    code = f.read()

# Execute the code
exec(code)
