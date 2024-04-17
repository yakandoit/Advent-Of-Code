# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 
# 13 green cubes 
# 14 blue cubes. 
# What is the sum of the IDs of those games?
import re

def check_games(input_lines, expected_red, expected_green, expected_blue):
    possible_games = []
    
    for line in input_lines:
        game_info = line.split(": ")[1].split("; ")
        total_red = 0
        total_green = 0
        total_blue = 0
        
        for info in game_info:
            cubes = info.split(", ")
            for cube in cubes:
                count_match = re.match(r'\d+', cube)  # Use regex to extract the count
                if count_match:
                    count = int(count_match.group())
                    if "red" in cube:
                        total_red += count
                    elif "green" in cube:
                        total_green += count
                    elif "blue" in cube:
                        total_blue += count
        
        if total_red == expected_red and total_green == expected_green and total_blue == expected_blue:
            possible_games.append(int(line.split(":")[0].split()[1]))
    
    return possible_games

def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

expected_red = 12
expected_green = 13
expected_blue = 14

# Input file path 
input_file = "input.txt"
input_lines = read_input_file(input_file)

possible_games = check_games(input_lines, expected_red, expected_green, expected_blue)
print("Game Sums: ", sum(possible_games))

