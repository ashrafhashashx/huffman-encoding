test = "mississippi river"

class Vertex:
    def __init__(self, freq=0):
        self.freq = freq
        self.label = None

    def set_label(self, label):
        self.label = label


class BinTree:
    def __init__(self, vertex, left=None, right=None):
        self.vertex = vertex
        self.left = left
        self.right = right

    def insert_vertex(self, vertex):
        self.vertex = vertex

    def delete_vertex(self, vertex):
        self.vertex = None

    def find_letter(self, letter):
        if letter in self.left.vertex.label:
            return '0' + self.left.find_letter(letter)
        elif letter in self.right.vertex.label:
            return '1' + self.right.find_letter(letter)
        else:
            return 'the letter does not exist in the tree'

    # def merge(self, other_tree):
    #     result = BinTree(left=self, right=other_tree)
    #     left_vertex = self.vertex
    #     right_vertex = other_tree.vertex
    #     result.insert_vertex(Vertex(left_vertex.freq + right_vertex.freq))
    #     result.vertex.set_label(left_vertex.label + right_vertex.label)
    #     return result


    def __str__(self):
        return self.vertex.label + str(self.vertex.freq)

    def __repr__(self):
        return self.__str__()

def get_trees(text):
    d = {}
    for i in text:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    list = []
    for i in d.keys():
        if i == ' ':
            l = '_'
        else:
            l = i
        v = Vertex(freq=d[i])
        v.set_label(l)
        list.append(BinTree(v))
    return list

print(get_trees(test))

def decode(text):
    pass


def encode(text):
    pass





