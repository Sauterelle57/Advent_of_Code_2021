##
## EPITECH PROJECT, 2021
## Advent Code
## File description:
## Day01
##

increase = 0

with open("/home/Marie/Advent_of_Code_2021/input.txt", "r") as file:
    data1 = int(file.readline())
    data2 = int(file.readline())
    data3 = int(file.readline())
    somme = data1 + data2 + data3
    while data3 != "":
        if somme < data1 + data2 + data3:
            increase += 1
        somme = data1 + data2 + data3
        data1 = data2
        data2 = data3
        data3 = file.readline()
        if data3 != "":
            data3 = int(data3)
        else:
            break

print(increase)
file.close()
