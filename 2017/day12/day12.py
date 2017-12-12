import os
from collections import defaultdict, deque

def main():
    pipes = defaultdict(set)
    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day12.txt"), 'r') as f:
        for line in f:
            split = line.split("<->")
            lhs_split = split[0].strip()
            rhs_split = [x.strip() for x in split[1].split(",")]
            for rhs in rhs_split:
                pipes[lhs_split].add(rhs)
                pipes[rhs].add(lhs_split)
    component = set()
    queue = deque()

    components = 0
    while len(pipes) > 0:
        next_ = pipes.keys()[0]
        queue.append(next_)
        component.add(next_)
        while len(queue) > 0:
            val = queue.popleft()
            component.add(val)
            neighbors = filter(lambda x: x not in component, pipes[val])
            queue.extend(neighbors)
        components += 1
        print components
        for x in component:
            if x in pipes:
                del pipes[x]



if __name__ == "__main__":
    main()
