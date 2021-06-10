#=================================#
# Creating new itterating Pattern #
#=================================#

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, .5):
    print(n)
"""
0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
"""

#====================#
# Iterator Protocol  #
#====================#


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r})'.format(self.value)

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
"""
Node(0)
Node(1)
Node(3)
Node(4)
Node(2)
Node(5)
"""
