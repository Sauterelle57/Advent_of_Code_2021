##
## EPITECH PROJECT, 2021
## Advent Code
## File description:
## Day01
##

nb_col = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
gamma_rate = "0b"
epsilon_rate = "0b"

with open("/home/Marie/Advent_of_Code_2021/input_day03.txt", "r") as file:
    binary = file.readline()
    while binary != "":
        for i in range(0, 12):
            if binary[i] == "1":
                nb_col[i][1] += 1
            else:
                nb_col[i][0] += 1
        binary = file.readline()

for i in range(0, 12):
    if nb_col[i][0] > nb_col[i][1]:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate*epsilon_rate)
file.close()
