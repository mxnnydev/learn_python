# Task 2: File Reader
# Ask the user for a filename and print all its content.

filename = input("what is the file name: ")

with open(filename, 'r') as file:
    print(f"\n📁 FILE CONTENT:\{file.read()}\n\n")