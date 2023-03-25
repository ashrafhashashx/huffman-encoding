import heapq
from collections import defaultdict

class Node:
    def __init__(self, value=None, freq=0, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1
    return freq_dict

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, parent)

    return heap[0]

def build_codewords_table(tree):
    codewords_table = {}
    def traverse(node, codeword):
        if node is None:
            return
        if node.value is not None:
            codewords_table[node.value] = codeword
            return
        traverse(node.left, codeword + "0")
        traverse(node.right, codeword + "1")
    traverse(tree, "")
    return codewords_table

def huffman_encode(data):
    freq_dict = build_frequency_dict(data)
    huffman_tree = build_huffman_tree(freq_dict)
    codewords_table = build_codewords_table(huffman_tree)

    encoded_data = ""
    for char in data:
        encoded_data += codewords_table[char]
    return encoded_data, huffman_tree

def huffman_decode(encoded_data, huffman_tree):
    decoded_data = ""
    node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.value is not None:
            decoded_data += node.value
            node = huffman_tree
    return decoded_data

test = "mississippi river"
encod = huffman_encode(test)

print(encod[0])
decod = huffman_decode(encod[0], encod[1])
print(decod)