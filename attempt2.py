from treelib import Node, Tree
tree = Tree()
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()

sub_t = tree.subtree('diane')
sub_t.show()

test = "mississippi river"

def dic_to_tree(dic):
    list = []
    for i in dic.keys():
        new_tree = Tree()
        tree.create_node(i, )

def get_dic(text):
    dic = {}
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dict(sorted(dic.items(), key=lambda item: item[1]))

print(get_tree(test))

