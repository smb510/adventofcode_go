import os
def main():
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day10.txt"), 'r') as f:
        for line in f:
            print line.strip()

if __name__ == '__main__':
    main()
