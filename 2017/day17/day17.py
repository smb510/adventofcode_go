class Node:
    def __init__(self, value):
        self.value = value
        self.next = self

    # Inserts new_node between self and self.next
    def insert(self, new_node):
        after = self.next
        self.next = new_node
        new_node.next = after



def main():
    part_1()
    part_2()

def part_2():
    first = Node(0)
    curr = first
    steps = 394
    for i in range(1,50000001):
        if i % 100000 == 0:
            print(i)
        for x in range(steps):
            curr = curr.next
        curr.insert(Node(i))
        curr = curr.next
    print(first.next.value)

def part_1():
    first = Node(0)
    curr = first
    steps = 394
    for i in range(1,2018):
        for x in range(steps):
            curr = curr.next
        curr.insert(Node(i))
        curr = curr.next
    while curr.value != 2017:
        curr = curr.next
    print(curr.next.value)


if __name__ == '__main__':
    main()