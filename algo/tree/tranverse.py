r"""

















"""

class Node:
    # value = None

    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right


import unittest


def pre_order_recur(root):
    if root is None:
        return

    print(root.value + " ")
    pre_order_recur(root.left)
    pre_order_recur(root.right)


def in_order_recur(root):
    if root is None:
        return

    in_order_recur(root.left)
    print(root.value + " ")
    in_order_recur(root.right)



def pos_order_recur(root):
    if root is None:
        return

    pos_order_recur(root.left)
    pos_order_recur(root.right)
    print(root.value + " ")


def pre_order_iter(root):
    pass


def in_order_iter(root):
    pass


def pos_order_iter(root):
    pass

r"""
         a
      /      \
     b         c
   /   \     /   \
  d     e   f      g

"""

class TestRecur(unittest.TestCase):
    def test(self):
        print('aaa')
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        a.left = b
        a.right = c


        pre_order_recur(a)

        print('================')

        in_order_recur(a)

        print('================')

        pos_order_recur(a)


        # self.assertEqual(
        #     [1, 1, 2, 3, 5, 8, 13, 21],
        #     fib(8),
        # )


class TestIter(unittest.TestCase):
    def test(self):
        print('aaa')
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        a.left = b
        a.right = c


if __name__ == '__main__':
    unittest.main()
