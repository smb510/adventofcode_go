import os

def main():

    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day7.txt"), 'r') as f:
        graph = {}
        lines = [x.strip() for x in list(f)]
        for line in lines:
            sides = line.split("->")
            if len(sides) == 1:
                # leaf nodes
                node = sides[0].split(" ")[0].strip()
                # print node
                graph[node] = []
            else:
                children = [x.strip() for x in sides[1].strip().split(",")]
                parent = sides[0].split(" ")[0].strip()
                for child in children:
                    if child not in graph:
                        graph[child] = [parent]
                    else:
                        graph[child].append(parent)
        for child, parents in graph.iteritems():
            if len(parents) == 0:
                pass
            else:
                parent = parents[0]
                while parent in graph:
                    parent = graph[parent][0]
                print parent # root node

        

if __name__ == '__main__':
    main()