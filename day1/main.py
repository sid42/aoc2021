def part1(): 
    f = open('input.txt', 'r')
    lines = f.readlines()
    increase_count = 0
    prev = 100000000

    for line in lines: 
        num = int(line)
        if num > prev: 
            increase_count += 1

        prev = num

    print(increase_count)


def part2(): 
    f = open('input.txt', 'r')
    lines = f.readlines()
    increase_count = 0
    prev = 100000000

    for i in range(len(lines) - 2): 
        sliding_window_sum = 0
        for j in range(3): 
            sliding_window_sum += int(lines[i + j])
        
        if sliding_window_sum > prev: 
            increase_count += 1

        prev = sliding_window_sum

    print(increase_count)

if __name__ == "__main__":
    # part1()
    part2()

