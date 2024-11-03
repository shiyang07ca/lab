"""
# TODO:

跳表

https://epaperpress.com/sortsearch/download/skiplist.pdf

https://cmps-people.ok.ubc.ca/ylucet/DS/SkipList.html

"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.forward = []

    @property
    def level(self):
        return len(self.forward)


class SkipList:
    def __init__(self, max_level=16):
        self.head = Node(None, None)
        self.level = 0
        self.max_level = max_level

    def find(self, k):
        pass

    def insert(self, key, value):
        # node = Node(k, v)
        update = [-1] * self.max_level
        n = self.head
        for i in range(self.level, -1, -1):
            if not node.forward:
                break

            while n.forward[i].key <= key:
                n = n.forward[i]
            update[i] = n

        if n.key == key:
            n.value = value
        else:
            # TODO: random level
            level = 3
            if level > self.level:
                for i in range(self.level, level):
                    update[i] = self.head
                self.level = level - 1
            new_node = Node(key, value)
            for i in range(level):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, k):
        pass


def test_insert():
    skip_list = SkipList()
    skip_list.insert("Key1", 3)
    skip_list.insert("Key2", 12)
    skip_list.insert("Key3", 41)
    skip_list.insert("Key4", -19)

    node = skip_list.head
    all_values = {}
    while node.level != 0:
        node = node.forward[0]
        all_values[node.key] = node.value

    assert len(all_values) == 4
    # assert all_values["Key1"] == 3
    # assert all_values["Key2"] == 12
    # assert all_values["Key3"] == 41
    # assert all_values["Key4"] == -19


# def test_insert_overrides_existing_value():
#     skip_list = SkipList()
#     skip_list.insert("Key1", 10)
#     skip_list.insert("Key1", 12)

#     skip_list.insert("Key5", 7)
#     skip_list.insert("Key7", 10)
#     skip_list.insert("Key10", 5)

#     skip_list.insert("Key7", 7)
#     skip_list.insert("Key5", 5)
#     skip_list.insert("Key10", 10)

#     node = skip_list.head
#     all_values = {}
#     while node.level != 0:
#         node = node.forward[0]
#         all_values[node.key] = node.value

#     if len(all_values) != 4:
#         print()
#     assert len(all_values) == 4
#     assert all_values["Key1"] == 12
#     assert all_values["Key7"] == 7
#     assert all_values["Key5"] == 5
#     assert all_values["Key10"] == 10


# def test_searching_empty_list_returns_none():
#     skip_list = SkipList()
#     assert skip_list.find("Some key") is None


# def test_search():
#     skip_list = SkipList()

#     skip_list.insert("Key2", 20)
#     assert skip_list.find("Key2") == 20

#     skip_list.insert("Some Key", 10)
#     skip_list.insert("Key2", 8)
#     skip_list.insert("V", 13)

#     assert skip_list.find("Y") is None
#     assert skip_list.find("Key2") == 8
#     assert skip_list.find("Some Key") == 10
#     assert skip_list.find("V") == 13


# def test_deleting_item_from_empty_list_do_nothing():
#     skip_list = SkipList()
#     skip_list.delete("Some key")

#     assert len(skip_list.head.forward) == 0


# def test_deleted_items_are_not_founded_by_find_method():
#     skip_list = SkipList()

#     skip_list.insert("Key1", 12)
#     skip_list.insert("V", 13)
#     skip_list.insert("X", 14)
#     skip_list.insert("Key2", 15)

#     skip_list.delete("V")
#     skip_list.delete("Key2")

#     assert skip_list.find("V") is None
#     assert skip_list.find("Key2") is None


# def test_delete_removes_only_given_key():
#     skip_list = SkipList()

#     skip_list.insert("Key1", 12)
#     skip_list.insert("V", 13)
#     skip_list.insert("X", 14)
#     skip_list.insert("Key2", 15)

#     skip_list.delete("V")
#     assert skip_list.find("V") is None
#     assert skip_list.find("X") == 14
#     assert skip_list.find("Key1") == 12
#     assert skip_list.find("Key2") == 15

#     skip_list.delete("X")
#     assert skip_list.find("V") is None
#     assert skip_list.find("X") is None
#     assert skip_list.find("Key1") == 12
#     assert skip_list.find("Key2") == 15

#     skip_list.delete("Key1")
#     assert skip_list.find("V") is None
#     assert skip_list.find("X") is None
#     assert skip_list.find("Key1") is None
#     assert skip_list.find("Key2") == 15

#     skip_list.delete("Key2")
#     assert skip_list.find("V") is None
#     assert skip_list.find("X") is None
#     assert skip_list.find("Key1") is None
#     assert skip_list.find("Key2") is None


# def test_delete_doesnt_leave_dead_nodes():
#     skip_list = SkipList()

#     skip_list.insert("Key1", 12)
#     skip_list.insert("V", 13)
#     skip_list.insert("X", 142)
#     skip_list.insert("Key2", 15)

#     skip_list.delete("X")

#     def traverse_keys(node):
#         yield node.key
#         for forward_node in node.forward:
#             yield from traverse_keys(forward_node)

#     assert len(set(traverse_keys(skip_list.head))) == 4


# def test_iter_always_yields_sorted_values():
#     def is_sorted(lst):
#         for item, next_item in zip(lst, lst[1:]):
#             if next_item < item:
#                 return False
#         return True

#     skip_list = SkipList()
#     for i in range(10):
#         skip_list.insert(i, i)
#     assert is_sorted(list(skip_list))
#     skip_list.delete(5)
#     skip_list.delete(8)
#     skip_list.delete(2)
#     assert is_sorted(list(skip_list))
#     skip_list.insert(-12, -12)
#     skip_list.insert(77, 77)
#     assert is_sorted(list(skip_list))


def pytests():
    for i in range(1):
        # Repeat test 100 times due to the probabilistic nature of skip list
        # random values == random bugs
        test_insert()
        # test_insert_overrides_existing_value()

        # test_searching_empty_list_returns_none()
        # test_search()

        # test_deleting_item_from_empty_list_do_nothing()
        # test_deleted_items_are_not_founded_by_find_method()
        # test_delete_removes_only_given_key()
        # test_delete_doesnt_leave_dead_nodes()

        # test_iter_always_yields_sorted_values()


if __name__ == "__main__":
    pass
