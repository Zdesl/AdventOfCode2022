import os
with open(os.path.join(os.getcwd(), "Day1", "input"), 'r') as f:
    input = f.read()
lines = input.split("\n")
elf = []
elves = []
calories = []
for line in lines:
    if line == "":
        elves.append(elf)
        calories.append(sum(elf))
        elf = []
    else:
        elf.append(int(line))
calories.sort()
print(calories[-1])  # answer 1
print(sum(list(calories[-3:])))  # answer 2
