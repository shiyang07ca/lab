r"""








"""


def main():
    l = [0, 4, 50, 7, 55, 90, 87]
    heap = r"""
     4
   /   \
  50    7
 / \   /
55 90 87
"""
    print(heap)
    print([f"{i:2}" for i, _ in enumerate(l)])
    print([f"{i:2}" for i in l])
    for i, item in enumerate(l):
        print(i, i // 2, item, l[i // 2])


if __name__ == '__main__':
    main()
