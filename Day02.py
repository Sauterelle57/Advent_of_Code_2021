##
## EPITECH PROJECT, 2021
## Advent Code
## File description:
## Day01
##

pos = [0, 0] #horizontal pos, depth

with open("/home/Marie/Advent_of_Code_2021/input_day02.txt", "r") as file:
    new_pos = file.readline()
    while new_pos != "":
        if "forward" in new_pos:
            pos[0] += int(new_pos[-2])
        if "down" in new_pos:
            pos[1] += int(new_pos[-2])
        if "up" in new_pos:
            pos[1] -= int(new_pos[-2])
        new_pos = file.readline()

print(pos[0] * pos[1])
file.close()
