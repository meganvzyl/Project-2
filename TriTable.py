# Introduction to Programming, Task 15: CapStone Project II
# Megan van Zyl, 23/04/2019
# Python code to make use of nested loops to create a number pyramid

for i in range (1, 10):             #number of rows
    for j in range(1, i + 1):       #number of columns
        print(i * j, end=" ")       
    print("\n")                     #program prints a new line
        

