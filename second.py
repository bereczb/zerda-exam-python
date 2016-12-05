# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def write_to_file(name_of_file, string_to_write):

    try:
        file_work_with = open(name_of_file, 'w')
        for i in range(10):
            file_work_with.write(string_to_write)
        file_work_with.close()
        return True

    except:
        return False

print(write_to_file('tree.txt', 'apple'))
