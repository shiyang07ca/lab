"""
# Ref: https://gist.github.com/eatonphil/51b91bb30bc7dbebd9bfb3c33248e563


Resources that helped out:
https://webdocs.cs.ualberta.ca/~holte/T26/ins-b-tree.html
https://www.cs.usfca.edu/~galles/visualization/BTree.html
https://sites.radford.edu/~nokie/classes/360/trees.b.tree.html
http://carlosproal.com/ir/papers/p121-comer.pdf
https://w6113.github.io/files/papers/btreesurvey-graefe.pdf


TODO:
B Tree

B树的以下特性:
- 所有叶子节点都在同一层
- 节点中的键是有序的
- 每个节点的子节点数量不超过阶数
- 非根节点至少半满
- 所有的数据都存储在叶子节点中


假设B树的阶数（order）为 M

1. 节点的最大元素数是 M-1
2. 节点的最大子节点数是 M
3. 非根节点的最小元素数是 ⌈M/2⌉-1
4. 当节点中的元素数达到 M 时，需要进行分裂操作

例如：如果阶数为3，则非根节点至少要有1个键，最多有2个键
"""

import math
import uuid


class BTreeNode:
    def __init__(self, order=3):
        self.id = str(uuid.uuid4())[:8]
        self.order = order
        if order < 3:
            raise ValueError("BTree node must have at least 2 children")
        self.elements = [None for _ in range(order - 1)]
        self.children = [None for _ in range(order)]

    def contains(self, key):
        for i, e in enumerate(self.elements):
            if key == e["key"]:
                return True

            # 在左子树中查找
            if key < e["key"]:
                # 如果有子节点，继续在子节点中查找
                if len(self.children) > i:
                    return self.children[i].contains(key)
                # 如果没有子节点，说明未找到
                return False

        # 如果遍历完当前节点都没找到，且键值比所有项都大
        # 则在最右边的子节点中查找（如果存在的话）
        if len(self.children) > len(self.elements):
            return self.children[-1].contains(key)

        return False

    def insert(self, toinsert):
        is_leaf = self.children.count(None) == len(self.children)
        if is_leaf:
            return self.insert_leaf(toinsert)
        else:
            for i, child in enumerate(self.children):
                if i < len(self.elements):
                    if (
                        self.elements[i] is None
                        or toinsert["key"] < self.elements[i]["key"]
                    ):
                        return self.insert_child(toinsert, i, child)
                elif child is not None:
                    return self.insert_child(toinsert, i, child)

        assert False, "Should never happen"

    def split(self, copy, children_copy):
        pass

    def insert_leaf(self, toinsert):
        pass

    def insert_child(self, toinsert, i, child):
        new_self = BTreeNode(self.order)
        new_self.elements = self.elements.copy()
        new_self.children = self.children.copy()

        ret, middle, left, right = child.insert(toinsert)
        if middle is None:
            new_self.children[i] = ret
            return new_self, None, None, None

        # No space, must split
        location_to_insert = 0
        for ele in new_self.elements:
            if ele is None or toinsert["key"] < ele["key"]:
                break
            location_to_insert += 1

        new_self.elements.insert(location_to_insert, middle)
        assert sorted(
            [x["key"] if x is not None else math.inf for x in new_self.elements]
        ) == [x["key"] if x is not None else math.inf for x in new_self.elements]

        new_self.children.insert(location_to_insert, None)
        new_self.children[location_to_insert] = left
        new_self.children.insert(location_to_insert + 1, right)

        has_space = self.elements.count(None) > 0
        if has_space:
            assert new_self.elements[-1] is None
            new_self.elements.pop()
            assert len(new_self.elements) == new_self.order - 1

            assert new_self.children[-1] is None
            new_self.children.pop()
            assert len(new_self.children) == new_self.order

            return new_self, None, None, None
        else:  # No space, split
            return self.split(new_self.elements, new_self.children)

    def walk(self, fn, level=0, parent_id=None):
        assert len(self.children) == self.order
        assert len(self.elements) == self.order - 1
        assert self.order >= 3

        for i, child in enumerate(self.children):
            if child is not None:
                child.walk(fn, level + 1, self.id)

            if i < len(self.elements):
                ele = self.elements[i]
                if ele is not None:
                    fn(ele, level, self.id, parent_id)

    def list(self):
        lst = []
        self.walk(lambda x: lst.append(x), 0, None)
        return lst


class BTree:
    def __init__(self, order):
        self.root = BTreeNode(order)

    # TODO:
    def insert(self, toinsert):
        all_elements = self.list()

        new_self = BTree(self.root.order)
        new_node, middle, left, right = self.root.insert(toinsert)
        if middle is not None:  # Split at root
            new_self.root.elements[0] = middle
            new_self.root.children[0] = left
            new_self.root.children[1] = right
        else:
            assert new_node is not None
            new_self.root = new_node

        all_elements.append(toinsert)
        for ele in all_elements:
            assert new_self.contains(
                ele["key"]
            ), f"Expected {ele} in {new_self.list()}\n{new_self.print()}"

        return new_self

    def contains(self, key):
        return self.root.contains(key)

    def list(self):
        return self.root.list()

    def print(self):
        def _print(node, level, self_id, parent_id):
            print([self_id, parent_id], " " * (level + 1) + str(node))

        print("[")
        self.root.walk(_print)
        print("]")
