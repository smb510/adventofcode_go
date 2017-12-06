import os

def main():
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day4.txt"), 'r') as f:
        valid = 0
        lines = list(f)
        for line in lines:
            words = [''.join(sorted(word)) for word in line.strip().split(" ")]
            print words
            if len(set(words)) == len(words):
                valid += 1
    print valid

if __name__ == '__main__':
    main()