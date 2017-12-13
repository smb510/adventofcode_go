import os

def main():
    layers = {}
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day13.txt"), 'r') as f:
        lines = [[int(y) for y in x.strip().split(": ")] for x in f]
        layers = [x[0] for x in lines]
        depths = [[x[1], 0, True] for x in lines]
        firewalls = dict(zip(layers, depths))
        adjusted_firewalls = [(x[0], x[1]) for x in lines]
        delay = 0
        snuck_through = False
        while not snuck_through:
            print "Trying ", delay
            delay += 1
            snuck_through = did_sneak_through(delay, adjusted_firewalls)
        print "Delay is ", delay
        max_layer = max(layers)
        position = 0
        severity = 0
        while position <= max_layer:
            if position in firewalls:
                if firewalls[position][1] == 0:
                    severity += position * firewalls[position][0]
            for key in firewalls.iterkeys():
                val = firewalls[key]
                if val[2]:
                    # moving down
                    if val[1] < val[0] - 1:
                        val[1] += 1
                    elif val[1] == val[0] - 1:
                        val[1] -= 1
                        val[2] = False
                else:
                    # moving up
                    if val[1] > 0:
                        val[1] -= 1
                    elif val[1] == 0:
                        val[1] += 1
                        val[2] = True
            position += 1
        print "Severity is", severity


def did_sneak_through(delay, firewalls):
    positions = filter(lambda x: (x[0] + delay) % ((x[1] - 1) * 2) == 0, firewalls)
    return len(positions) == 0


if __name__ == '__main__':
    main()