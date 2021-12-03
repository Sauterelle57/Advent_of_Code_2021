##
## EPITECH PROJECT, 2021
## Advent Code
## File description:
## Day01
##


with open("input.txt", "r") as file:
    data = file.readline()
    while data != "":
        print(data)
        data = file.readline()

file.close()
