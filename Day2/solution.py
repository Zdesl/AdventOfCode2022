import os

def play1(elf, self):
    iscore = ord(self) - 87
    escore = ord(elf) - 64
    score = [6,0,3,6,0]
    return score[iscore - escore + 2] + iscore


def play2(elf, self):
    iscore = ord(self) - 87
    escore = ord(elf) - 64
    match escore:
        case 1:
            match iscore:
                case 1: iscore = 3
                case 2: iscore = 1
                case 3: iscore = 2
        case 3:
            match iscore:
                case 1: iscore = 2
                case 2: iscore = 3
                case 3: iscore = 1
    score = [6,0,3,6,0]
    return score[iscore - escore + 2] + iscore


answer1 = 0
answer2 = 0
with open(os.path.join(os.getcwd(), "Day2", "input"), 'r') as f:
    input = f.readlines()
for line in input:
    round = line[:-1].split(" ")
    answer1 += play1(round[0], round[1])
    answer2 += play2(round[0], round[1])
print(answer1)
print(answer2)