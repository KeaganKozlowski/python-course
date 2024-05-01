import os

directory = "/path/to/directory"

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        print("Processing file:", filename)
        with open(os.path.join(directory, filename), 'r') as file:
            first_line = file.readline()
            print("First line:", first_line)