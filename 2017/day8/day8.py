import os

comparators = {
    "==": (lambda a, b: a == b),
    "!=": (lambda a, b: a != b),
    ">": (lambda a, b: a > b),
    "<": (lambda a, b: a < b),
    "<=": (lambda a,b: a <= b),
    ">=": (lambda a, b: a >= b)}

def main():
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day8.txt"), 'r') as f:
        max_val = 0
        lines = list(f)
        parsed_lines = [parse_line(line) for line in lines]
        registers = dict.fromkeys([x[0] for x in parsed_lines], 0)
        for line in parsed_lines:
            if should_execute(line, registers):
                val = execute(line, registers)
                if val > max_val:
                    max_val = val
        print("Part 1", max(registers.values()))
        print("Part 2", max_val)
    

def get_registers(line, registers):
    reg_name = line.split(' ')[0]
    registers[reg_name] = 0

def parse_line(line):
    split = line.split(' ')
    split[1] = 1 if split[1] == "inc" else -1
    split[2] = int(split[2])
    split[5] = comparators[split[5]]
    split[6] = int(split[6])
    return split

def should_execute(line, registers):
    register = registers[line[4]]
    value = line[6]
    return line[5](register, value)

def execute(line, registers):
    register = line[0]
    increment = line[1]
    val = line[2]
    registers[register] = registers[register] + (val * increment)
    return registers[register]

if __name__ == '__main__':
    main()
