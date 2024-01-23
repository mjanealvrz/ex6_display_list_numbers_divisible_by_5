# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Pseudocode

# Paste the given list
given_list =  [10, 20, 33, 46, 55]

# Print the given list
print("Given List is ", str(given_list)[1:-1])

# Create a for loop to determine the number in list that is divisible by 5
for number in given_list:
    if  number % 5 == 0:
        print ("Numbers divisible by 5 are ", number)