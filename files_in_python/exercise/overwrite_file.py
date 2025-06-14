# ✅ Task 3: Overwrite a File
# Let the user enter text and completely overwrite notes.txt.

# overwriting written file
filename = 'journal.txt'
text = input("what is new text you want to write into file: ")
with open(filename, 'w') as file:
    file.write(text)
