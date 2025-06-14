# indexing = accessing elements of a sequence using [] (indexing, operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"


# credit_number[0] # get first item

# list slicing ~ starting index is inclusive & ending index is exclusive

# get the first four items:
# print(credit_number[0:4]) # start and end before 4 index 
# print(credit_number[5:9]) # start from index 5 and end before index 9
# print(credit_number[5:])  # start at index -> go to the end
# print(credit_number[-2]) # get the second last item
# print(credit_number[::2]) # print every second character 
# print(credit_number[::3]) # print every third character 

# last_digit = credit_number[-4:] # start from last 4 and go to the end
# print(f"XXXX-XXXX-XXXX-{last_digit}")

# credit_number = credit_number[::-1] # will reverse the string
# print(credit_number)