
# 🔹 Create and Write (overwrite everything)
with open("./myfile.txt", "w") as file:
    file.write("Hello world!\n")
    file.write("Writing to a file is easy.")

# 🔹 Read the file
with open("myfile.txt", "r") as file:
    content = file.read() # entire file as one string
    print("📄 Content:\n", content)

# 🔹 Append to file (don’t overwrite)
with open("myfile.txt", "a") as file:
    file.write("\nThis line was appended later.")

# 🔹 Read as lines (into a list)
with open("myfile.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    print("here is the content: \n")
    for i,value in enumerate(lines,1):
        print(f"{i}.{value}")
    
