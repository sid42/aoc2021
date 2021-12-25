class Column: 
    def __init__(self): 
        self.zeroes = 0
        self.ones = 0 
        self.starts_with_zero = []
        self.starts_with_one = []

def part1(): 
    f = open('input.txt', 'r')
    lines = f.readlines()
    
    columns = []
    for i in range(len(lines[0])): 
        if lines[0][i] == '0' or lines[0][i] == '1': 
            columns.append(Column())    

    for line in lines: 
        for i in range(len(line)): 
            if line[i] == '0':
                columns[i].zeroes += 1
            elif line[i] == '1':
                columns[i].ones += 1

    gamma, epsilon = '', ''
    for column in columns: 
        if column.zeroes > column.ones: 
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))

def part2(): 
    f = open('input.txt', 'r')
    lines = f.readlines()  

    oxygen_scan, c02_scan = lines, lines
    oxygen_idx, c02_idx = 0, 0

    while len(oxygen_scan) != 1:
        c = Column()
        for line in oxygen_scan: 
            if line[oxygen_idx] == '0':
                c.zeroes += 1
                c.starts_with_zero.append(line)
            elif line[oxygen_idx] == '1':
                c.ones += 1
                c.starts_with_one.append(line)
        
        if c.zeroes > c.ones: 
            oxygen_scan = c.starts_with_zero
        elif c.ones >= c.zeroes: 
            oxygen_scan = c.starts_with_one

        oxygen_idx += 1

    while len(c02_scan) != 1:
        c = Column()
        for line in c02_scan: 
            if line[c02_idx] == '0':
                c.zeroes += 1
                c.starts_with_zero.append(line)
            elif line[c02_idx] == '1':
                c.ones += 1
                c.starts_with_one.append(line)
        
        if c.zeroes > c.ones: 
            c02_scan = c.starts_with_one
        elif c.ones >= c.zeroes: 
            c02_scan = c.starts_with_zero

        c02_idx += 1
    # while len(co2_scan) != 1: 

    print(int(oxygen_scan[0], 2) * int(c02_scan[0], 2))

if __name__ == "__main__":
    # part1()
    part2()