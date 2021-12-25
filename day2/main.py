def part1(): 
    f = open('input.txt', 'r')
    lines = f.readlines()
    horizontal = 0
    vertical = 0

    for line in lines: 
        op, value = line.split(' ')
        if op == 'forward': 
            horizontal += int(value)
        elif op == 'down': 
            vertical += int(value)
        elif op == 'up': 
            vertical -= int(value)

    print(horizontal * vertical)

def part2(): 
    f = open('input.txt', 'r')
    lines = f.readlines()
    horizontal = 0
    vertical = 0
    aim = 0

    for line in lines: 
        op, value = line.split(' ')
        if op == 'forward': 
            horizontal += int(value)
            vertical += aim * int(value)
        elif op == 'down': 
            aim += int(value)
        elif op == 'up': 
            aim -= int(value)

    print(horizontal * vertical)

if __name__ == "__main__":
    # part1()
    part2()