import os

def main():
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day7.txt"), 'r') as f:
        lines = [x.strip() for x in list(f)]
        print lines

if __name__ == '__main__':
	main()