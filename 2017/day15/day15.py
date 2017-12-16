def main():
    start_a = 277
    start_b = 349
    count = 0
    for i in range(5000000):    
        print(i)
        start_a = generate_a(start_a)
        start_b = generate_b(start_b)
        if start_a & 0xffff == start_b & 0xffff:
            count += 1
    print(count)


def generate_a(prev):
    next_val = (prev * 16807) % 2147483647
    while next_val % 4 != 0:
        next_val =  (next_val * 16807) % 2147483647
    return next_val

def generate_b(prev):
    next_val = (prev * 48271) % 2147483647
    while next_val % 8 != 0:
        next_val = (next_val * 48271) % 2147483647
    return next_val

if __name__ == '__main__':
    main()