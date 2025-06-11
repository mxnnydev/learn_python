# 🔍 Searching and Replacing

text = "Manny"

# using find() ~ we can find where 'a' is located in 'Manny'

subscript = 'a'

print(text.find(subscript)) # found at index 👉 1

text.index(subscript) # same as find but throw error if not found

new_subscript = 'x'

text = text.replace(subscript, new_subscript) # allow us to replace subscript of text ( it returns a new string, but doesn't modify the original one. )

print(text) # checking for the difference

sub = 'n'

count_of_n = text.count(sub) # Count how many times sub appears

print(count_of_n) # will return the occurance