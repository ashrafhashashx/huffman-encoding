import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, letters='', label=0):
        self.label = label
        self.letters = letters

    def set_label(self, label):
        self.label = label


class Tree:
    def __init__(self, vertex=None, left=None, right=None):
        self.vertex = vertex
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

    def insert_vertex(self, vertex):
        self.vertex = vertex

    def __lt__(self, other):
        return self.vertex.label < other.vertex.label

    def __str__(self):
        def indent(n):
            return ' ' * n

        def f(n, t):
            result = t.vertex.letters + str(t.vertex.label)
            if t.left:
                result += '\n' + indent(n) + f(n + 2, t.left)
            if t.right:
                result += '\n' + indent(n) + f(n + 2, t.right)
            return result

        return f(0, self)

    def __repr__(self):
        return self.__str__()

    def merge(self, other):
        vertex1 = self.vertex
        vertex2 = other.vertex
        merged_vertex = Vertex(vertex1.letters + vertex2.letters)
        merged_vertex.set_label(vertex1.label + vertex2.label)
        return Tree(merged_vertex, self, other)

    def encode_letter(self, one_letter):
        if one_letter not in self.vertex.letters:
            raise Exception('Error not found in given tree!')

        def f(tree, encoding, letter):
            left = tree.left
            if left and letter in left.vertex.letters:
                return f(left, encoding + '0', letter)
            right = tree.right
            if right and letter in right.vertex.letters:
                return f(right, encoding + '1', letter)
            else:
                return encoding

        return f(self, '', one_letter)


def treeing(text):
    dic = {}
    for i in text:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    trees = []
    for i in dic.keys():
        new_vertex = Vertex(i)
        new_vertex.set_label(dic[i])
        new_tree = Tree()
        new_tree.insert_vertex(new_vertex)
        trees.append(new_tree)
    return trees


def unify(trees):
    if not trees:
        raise Exception('No trees in this list!')
    while len(trees) > 1:
        trees = sorted(trees)
        a = trees[0]
        b = trees[1]
        trees = trees[2:]
        trees.append(a.merge(b))
    return trees[0]


def encode(text):
    tree = treeing(text)
    tree = unify(tree)
    print(tree)
    result = ''
    print('---------------------------')
    for i in text:
        enc = tree.encode_letter(i)
        print(i, enc)
        result += enc
    return result, tree


def decode(text, tree0):
    def tail(some_list):
        return some_list[1:]

    def f(current, remaining_text):
        if current.is_leaf():
            return current.vertex.letters, remaining_text
        bit = remaining_text[0]
        remaining_text = tail(remaining_text)
        if bit == '1':
            return f(current.right, remaining_text)
        elif bit == '0':
            return f(current.left, remaining_text)

    remaining = text
    final_result = ''
    while remaining:
        l, remaining = f(tree0, remaining)
        final_result += l
    return final_result


def display_tree(original_tree):
    g = nx.Graph()
    positions = {}

    # creates a node and connects us to it with an edge and returns the number of that node.
    def f(tree):
        n = len(g.nodes.items()) + 1
        if tree.is_leaf():
            g.add_node(n, label=tree.vertex.letters + '(' + str(tree.vertex.label) + ')')
        else:
            g.add_node(n, label=tree.vertex.letters + '(' + str(tree.vertex.label) + ')')
            g.add_edge(n, f(tree.left))
            g.add_edge(n, f(tree.right))
        return n

    f(original_tree)
    print('size=', g.size())
    print(g)
    return g


test1 = "mississippi river"
test2 = "ab"
test3 = "These are short, famous texts in English from classic sources like the Bible or Shakespeare. Some texts have word definitions and explanations to help you. Some of these texts are written in an old style of English. Try to understand them, because the English that we speak today is based on what our great, great, great, great grandparents spoke before! Of course, not all these texts were originally written in English. The Bible, for example, is a translation. But they are all well known in English today, and many of them express beautiful thoughts."

test = test1
enc, tree = encode(test)
display_tree(tree)
print(enc)
dec = decode(enc, tree)
print(dec)
print(dec == test)
