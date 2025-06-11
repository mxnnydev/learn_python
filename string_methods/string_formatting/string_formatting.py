# 🔧 Old Style: % Formatting
name = "Emmanuel"
age = 25
print("My name is %s and I am %d years old" % (name, age))

# 🧱 str.format() Method
name = "Emmanuel"
score = 98.456

print("Hello {}, your score is {:.2f}".format(name, score))
# → Hello Emmanuel, your score is 98.46

# ✨ modern way 
name = "Emmanuel"
score = 98.456

print(f"Hello {name}, your score is {score:.2f}")
# → Hello Emmanuel, your score is 98.46
