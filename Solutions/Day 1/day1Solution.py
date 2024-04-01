# Reading in the file
input = open("input.txt", "r")
result = 0

# Getting the lines
Lines = input.readlines()

# For every line, add spaces to each character (so that split() and isnumeric() works) 
# Then store each value in it's own array
for line in Lines:
    line_numbers = []
    line = " ".join(line)
    numbers = line.split()
    for num in numbers:
        if num.isnumeric():
            line_numbers.append(int(num))

    # Add the first and last numbers to an array and concat them
    concatenated_array = []
    concatenated_array.append(line_numbers[0])
    concatenated_array.append(line_numbers[-1])
    concatenated_number = ''.join([str(line_numbers[0]), str(line_numbers[-1])])
    
    # Add them to the result then print it
    result = result + int(concatenated_number)

print(result)
