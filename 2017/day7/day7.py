import os
import re
import collections

def main():

    ws = os.path.dirname(__file__)
    with open(os.path.join(ws, "day7.txt"), 'r') as f:
        lines = [x.strip() for x in list(f)]
        # build_parent_graph(lines)
        build_child_graph(lines)

def build_parent_graph(lines):
    graph = {}
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
            print(parent) # root node

def build_child_graph(lines):
    graph = {}
    weights = {}
    for line in lines:
        sides = line.split("->")
        node = get_node_and_weight(sides[0])
        weights[node[0]] = node[1]
        if len(sides) > 1:
            graph[node[0]] = [x.strip() for x in sides[1].strip().split(",")]
    print(weights["apjxafk"])
    print(graph["apjxafk"])
    for child in graph["apjxafk"]:
        get_subtree_weight(graph, weights, child)

def get_subtree_weight(graph, weights, node):
    weight = weights[node]
    queue = collections.deque()
    if node in graph:
        queue.extend(graph[node])
        while len(queue) > 0:
            val = queue.popleft()
            weight += weights[val]
            if val in graph:
                queue.extend(graph[val])
            else:
                print("leaf: ", val, weights[val])
        print(weight)
    else:
        print("no child for ", node, weights[node])

def get_node_and_weight(node):
    regex = re.compile("(\w+) \((\d+)\)")
    capture = re.match(regex, node)
    return (capture.group(1), int(capture.group(2)))
        

if __name__ == '__main__':
    main()